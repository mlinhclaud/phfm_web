// Quét thứ tự section và màu nền thực tế của từng trang con (kể cả ảnh nền, đo bằng điểm ảnh):
//   HTML=dist/phfm-website.html LANGS=vi WIDTHS="1440 390" PAGES="about phvsf" node qa/r5sections.js [out.json]
// Mỗi trang in một dòng: thứ tự khối, nhóm nền khai báo (tên màu brief). Cờ =SAME khi hai khối kề nhau cùng nhóm nền (ảnh không tính).
// File JSON có thêm màu trung bình và màu mép trái đo từ ảnh chụp.
// Hero và thanh mục con được tách riêng (thanh mục con nằm cùng cấp với hero và section).
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const F=path.resolve(process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
const pages=(process.env.PAGES||'about funds phvsf vnshine member portfolio advisory ir news academy careers contact guidePhvsf guideVnshine faq glossary forms terms privacy').split(' ');
const langs=(process.env.LANGS||'vi').split(' ');const widths=(process.env.WIDTHS||'1440 390').split(' ').map(Number);
const NAMES={'#ffffff':'trắng','#e3eef0':'mist','#dceef0':'mist','#dcebee':'mist2','#0a3440':'teal đậm','#0b6274':'teal','#d8e7ea':'viền'};
(async()=>{const b=await chromium.launch();const res=[];
for(const W of widths){const H=W>500?900:844;
 const ctx=await b.newContext({viewport:{width:W,height:H},isMobile:W<500,hasTouch:W<500});const p=await ctx.newPage();
 for(const L of langs)for(const pg of pages){
  await p.goto('file://'+F+'#/'+L+'/'+pg);await p.reload();await p.waitForTimeout(1500);
  await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=500){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,30))}document.querySelectorAll('.cr').forEach(e=>e.classList.add('in'));document.documentElement.style.scrollSnapType='none';window.scrollTo(0,0)});
  await p.waitForTimeout(300);
  const secs=await p.evaluate(()=>{
    const hex=c=>{const m=c.match(/[\d.]+/g).map(Number);if(m.length>3&&m[3]<.5)return null;return '#'+m.slice(0,3).map(v=>Math.round(v).toString(16).padStart(2,'0')).join('')};
    const main=document.querySelector('main')||document.body;
    const isBand=e=>/^(SECTION|NAV)$/.test(e.tagName)||e.classList.contains('nm-sbar');
    const flat=el=>{const o=[];[...el.children].forEach(c=>{if(isBand(c))o.push(c);else if(/^(DIV|MAIN)$/.test(c.tagName)&&!c.classList.contains('nm-sbar')&&c.querySelector(':scope>section,:scope>nav,:scope>main,:scope>.nm-sbar')&&[null,'#ffffff'].includes(hex(getComputedStyle(c).backgroundColor||'rgba(0,0,0,0)')))o.push(...flat(c))});return o};
    let kids=flat(main);if(!kids.length)kids=[...main.children].filter(e=>e.getBoundingClientRect().height>=20);
    const out=[];
    kids.forEach(e=>{const cs=getComputedStyle(e);if(cs.display==='none'||cs.position==='fixed')return;const r=e.getBoundingClientRect();if(r.height<20)return;
      let cls=e.tagName.toLowerCase();if(e.id)cls+='#'+e.id;else if(e.classList.length)cls+='.'+[...e.classList].slice(0,2).join('.');
      let cover=false;e.querySelectorAll(':scope>img,:scope>div>img').forEach(im=>{const ir=im.getBoundingClientRect();if(ir.width>=r.width*.5&&ir.height>=r.height*.7)cover=true});
      out.push({txt:(e.textContent||'').trim().replace(/\s+/g,' ').slice(0,36),sel:cls,top:Math.round(r.top+scrollY),h:Math.round(r.height),bg:hex(cs.backgroundColor),grad:cs.backgroundImage.includes('gradient'),bgimg:cs.backgroundImage.includes('url('),cover});
    });
    return out});
  const shot=await p.screenshot({fullPage:true,type:'png'});
  const px=await p.evaluate(async([b64,secs])=>{const im=new Image();im.src='data:image/png;base64,'+b64;await im.decode();const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const x=c.getContext('2d');x.drawImage(im,0,0);
    const h2=v=>Math.round(v).toString(16).padStart(2,'0');
    return secs.map(s=>{const w=im.width,y0=Math.max(0,s.top),hh=Math.max(1,Math.min(s.h,im.height-y0));const d=x.getImageData(0,y0,w,hh).data;let r=0,g=0,bl=0,n=0;for(let i=0;i<d.length;i+=16){r+=d[i];g+=d[i+1];bl+=d[i+2];n++}
      const e=x.getImageData(0,y0+2,Math.min(w,24),Math.max(1,Math.min(hh-4,40))).data;let er=0,eg=0,eb=0,en=0;for(let i=0;i<e.length;i+=4){er+=e[i];eg+=e[i+1];eb+=e[i+2];en++}
      return {mean:'#'+h2(r/n)+h2(g/n)+h2(bl/n),edge:'#'+h2(er/en)+h2(eg/en)+h2(eb/en)}})},[shot.toString('base64'),secs]);
  secs.forEach((s,i)=>{Object.assign(s,px[i]);
    const nm=s.bg?(NAMES[s.bg]||s.bg):(s.cover||s.bgimg?'ảnh':s.grad?'gradient':'nền trang');s.name=nm;
    let g=nm;if(nm==='nền trang')g='trắng';if(nm==='mist2')g='mist';if(nm==='ảnh'||nm==='gradient')g='ảnh:'+s.mean;s.group=g});
  secs.forEach((s,i)=>{const pv=secs[i-1];s.same=!!(pv&&pv.group===s.group&&!s.group.startsWith('ảnh'))});
  res.push({page:pg,lang:L,W,secs});
  console.log(`${pg} ${L} ${W}: ${secs.map(s=>s.sel.split('.')[0]+'['+s.name+(s.same?' =SAME':'')+']').join(' > ')}`);
 }
 await ctx.close();}
await b.close();fs.mkdirSync(path.join(__dirname,'out'),{recursive:true});fs.writeFileSync(process.argv[2]||path.join(__dirname,'out','r5sections.json'),JSON.stringify(res,null,1));})();
