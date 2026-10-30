// Khảo sát nền teal đậm #0A3440: node qa/survey-teal.js [file.html]  ->  qa/out/teal-survey-<TAG>.json
// Mỗi trang × 1440/390 (VI): liệt kê phần tử có nền #0A3440 (phẳng, gradient, lớp phủ rgba(10,52,64,>=.3)),
// diện tích ở màn hình đầu, và tỉ lệ pixel của màn hình đầu:
//   "phẳng" = pixel gần #0A3440 (sai số <= 10 mỗi kênh); "tối" = độ sáng tương đối < 0.06 (gồm cả ảnh giờ xanh tối).
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const F=path.resolve(process.argv[2]||path.join(__dirname,'..','dist','phfm-website.html'));
const OUT=path.join(__dirname,'out');fs.mkdirSync(OUT,{recursive:true});
const pages=(process.env.PAGES||'home about funds phvsf vnshine member portfolio advisory ir news academy careers contact guidePhvsf guideVnshine faq glossary forms terms privacy').split(' ');
const lang=process.env.LANG2||'vi';
(async()=>{const b=await chromium.launch();const res=[];
for(const W of [1440,390]){const H=W>500?900:844;
 const ctx=await b.newContext({viewport:{width:W,height:H},isMobile:W<500,hasTouch:W<500});
 const p=await ctx.newPage();
 for(const pg of pages){
  await p.goto('file://'+F+'#/'+lang+'/'+pg);await p.waitForTimeout(1800);
  await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});
  await p.evaluate(()=>{window.scrollTo(0,0);document.querySelectorAll('.cr').forEach(e=>e.classList.add('in'))});await p.waitForTimeout(300);
  const info=await p.evaluate((H)=>{
   const T=/rgb\(10, 52, 64\)/, TA=/rgba\(10, 52, 64, ([0-9.]+)\)/, G=/10, 52, 64/;
   const vis=e=>{const r=e.getBoundingClientRect();const cs=getComputedStyle(e);return r.width>40&&r.height>8&&cs.display!=='none'&&cs.visibility!=='hidden'};
   const path=e=>{const a=[];while(e&&e!==document.body&&a.length<4){let s=e.tagName.toLowerCase();if(e.id)s+='#'+e.id;else if(e.classList.length)s+='.'+[...e.classList].slice(0,2).join('.');a.unshift(s);e=e.parentElement}return a.join('>')};
   const out=[];document.querySelectorAll('body *').forEach(e=>{if(!vis(e))return;const cs=getComputedStyle(e);let kind=null;
    if(T.test(cs.backgroundColor))kind='nền phẳng';
    else if(cs.backgroundImage.includes('gradient')&&G.test(cs.backgroundImage))kind='gradient teal đậm';
    else {const m=cs.backgroundColor.match(TA);if(m&&+m[1]>=.3)kind='phủ rgba('+m[1]+')'}
    if(!kind)return;const r=e.getBoundingClientRect();
    const top=r.top+scrollY,bot=r.bottom+scrollY;const vh=Math.max(0,Math.min(bot,H)-Math.max(top,0));const vw=Math.max(0,Math.min(r.right,innerWidth)-Math.max(r.left,0));
    out.push({sel:path(e),kind,x:Math.round(r.left),y:Math.round(top),w:Math.round(r.width),h:Math.round(r.height),firstScreenArea:Math.round(vh*vw),text:(e.textContent||'').trim().replace(/\s+/g,' ').slice(0,40)})});
   return {els:out,docH:document.documentElement.scrollHeight}},H);
  const buf=await p.screenshot({type:'png'});
  const px=await p.evaluate(async(b64)=>{const im=new Image();im.src='data:image/png;base64,'+b64;await im.decode();const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const x=c.getContext('2d');x.drawImage(im,0,0);const d=x.getImageData(0,0,c.width,c.height).data;let flat=0,dark=0,n=d.length/4;
   const lin=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};
   for(let i=0;i<d.length;i+=4){const r=d[i],g=d[i+1],bl=d[i+2];if(Math.abs(r-10)<=10&&Math.abs(g-52)<=10&&Math.abs(bl-64)<=10)flat++;const L=.2126*lin(r)+.7152*lin(g)+.0722*lin(bl);if(L<.06)dark++}
   return {flat:flat/n,dark:dark/n}},buf.toString('base64'));
  res.push({page:pg,W,lang,flat:+px.flat.toFixed(3),dark:+px.dark.toFixed(3),docH:info.docH,els:info.els});
  console.log(W,pg,'phẳng',(px.flat*100).toFixed(1)+'%','tối',(px.dark*100).toFixed(1)+'%','khối',info.els.length);
 }
 await ctx.close();}
fs.writeFileSync(OUT+'/teal-survey-'+(process.env.TAG||'main')+'.json',JSON.stringify(res,null,1));await b.close();})();
