// Đo tương phản chữ trong hero và các khối đổi màu, kể cả chữ nằm trên ảnh:
//   HTML=dist/phfm-website-r5a.html PAGES="about vnshine member" LANGS=vi WIDTHS="1440 390" node qa/r5contrast.js [out.json]
// Với mỗi phần tử chữ trong hero/khối: lấy màu chữ, ẩn toàn bộ chữ (color:transparent), chụp vùng chữ, tính tương phản
// giữa màu chữ và từng pixel nền; ghi giá trị xấu nhất (phân vị 2%) và trung vị. Chữ lớn (>=24px, hoặc >=18.66px đậm) cần >=3:1, còn lại >=4.5:1.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const F=path.resolve(process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
const pages=(process.env.PAGES||'about vnshine member').split(' ');const langs=(process.env.LANGS||'vi').split(' ');
const widths=(process.env.WIDTHS||'1440 390').split(' ').map(Number);
const SEL=process.env.SEL||'section.hero-sub, .nm-sbar, .ab-j, .fit, .pd-cell';
(async()=>{const b=await chromium.launch();const res=[];
for(const W of widths){const H=W>500?900:844;
 const ctx=await b.newContext({viewport:{width:W,height:H},isMobile:W<500,hasTouch:W<500});const p=await ctx.newPage();
 for(const L of langs)for(const pg of pages){
  await p.goto('file://'+F+'#/'+L+'/'+pg);await p.reload();await p.waitForTimeout(1800);
  await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=500){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,30))}document.querySelectorAll('.cr').forEach(e=>e.classList.add('in'));document.documentElement.style.scrollSnapType='none';window.scrollTo(0,0)});
  await p.waitForTimeout(300);
  // thu thập phần tử chữ (lá) trong các khối cần đo
  const items=await p.evaluate((SEL)=>{
    const out=[];const seen=new Set();
    document.querySelectorAll(SEL).forEach((blk,bi)=>{
      const walker=document.createTreeWalker(blk,NodeFilter.SHOW_TEXT);let n;
      while(n=walker.nextNode()){
        const t=n.textContent.trim();if(!t)continue;const el=n.parentElement;if(seen.has(el))continue;
        const cs=getComputedStyle(el);if(cs.visibility==='hidden'||cs.display==='none')continue;
        const r=document.createRange();r.selectNodeContents(n);const rc=r.getBoundingClientRect();if(rc.width<4||rc.height<4)continue;
        const top=rc.top+scrollY;seen.add(el);
        el.setAttribute('data-r5m',out.length);
        out.push({blk:blk.className.toString().split(' ')[0]||blk.tagName.toLowerCase(),id:blk.id||'',text:t.slice(0,32),color:cs.color,fs:parseFloat(cs.fontSize),fw:parseInt(cs.fontWeight)||400,x:rc.left,y:top,w:rc.width,h:rc.height});
      }});
    return out},SEL);
  // ẩn chữ, chụp từng khối chữ
  await p.addStyleTag({content:'html body *:not(#r5a):not(#r5b){color:transparent!important;-webkit-text-fill-color:transparent!important;text-shadow:none!important}'});
  await p.waitForTimeout(200);
  for(const it of items){
    if(it.y>6000||it.w>W)continue;
    await p.evaluate(y=>window.scrollTo(0,Math.max(0,y-300)),it.y);
    const sy=await p.evaluate(()=>window.scrollY);
    const clip={x:Math.max(0,it.x),y:Math.max(0,it.y-sy),width:Math.min(it.w,W-Math.max(0,it.x)),height:it.h};
    if(clip.width<2||clip.height<2||clip.y+clip.height>H)continue;
    const buf=await p.screenshot({clip,type:'png'});
    const m=await p.evaluate(async([b64,color])=>{
      const im=new Image();im.src='data:image/png;base64,'+b64;await im.decode();const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const x=c.getContext('2d');x.drawImage(im,0,0);
      const d=x.getImageData(0,0,c.width,c.height).data;
      const lin=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};
      const L=(r,g,b)=>.2126*lin(r)+.7152*lin(g)+.0722*lin(b);
      const m=color.match(/[\d.]+/g).map(Number);const lt=L(m[0],m[1],m[2]);
      const cr=[];for(let i=0;i<d.length;i+=4){const lb=L(d[i],d[i+1],d[i+2]);const a=Math.max(lt,lb),b2=Math.min(lt,lb);cr.push((a+.05)/(b2+.05))}
      cr.sort((a,b)=>a-b);return {min:cr[Math.floor(cr.length*.02)],med:cr[Math.floor(cr.length*.5)]}},[buf.toString('base64'),it.color]);
    const large=it.fs>=24||(it.fs>=18.66&&it.fw>=700);
    res.push({page:pg,lang:L,W,blk:it.blk+(it.id?'#'+it.id:''),text:it.text,color:it.color,fs:it.fs,large,min:+m.min.toFixed(2),med:+m.med.toFixed(2),pass:m.min>=(large?3:4.5)});
  }
  console.log(pg,L,W,'đo',res.filter(r=>r.page===pg&&r.W===W&&r.lang===L).length);
 }
 await ctx.close();}
await b.close();
fs.writeFileSync(process.argv[2]||path.join(__dirname,'out','r5contrast.json'),JSON.stringify(res,null,1));
const bad=res.filter(r=>!r.pass);console.log('DẠT',res.length-bad.length,'/',res.length,'KHÔNG DẠT',bad.length);
bad.slice(0,40).forEach(r=>console.log(' !',r.page,r.W,r.blk,JSON.stringify(r.text),r.color,r.fs+'px','min',r.min,'med',r.med));
})();
