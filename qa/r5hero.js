// Đo cỡ chữ hero các trang con: node qa/r5hero.js <file.html> <out.json>  (biến PAGES, LANGS, WIDTHS như qa.js)
// Mỗi hero ghi: breadcrumb (mục đầu, mục cuối), eyebrow, h1, mô tả, nút. Giá trị: font-size, line-height, letter-spacing, font-weight, word-spacing, text-align.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const F=path.resolve(process.argv[2]||process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
const pages=(process.env.PAGES||'about phvsf vnshine member portfolio advisory academy careers guidePhvsf guideVnshine').split(' ');
const langs=(process.env.LANGS||'vi').split(' ');const widths=(process.env.WIDTHS||'1440 1024 390').split(' ').map(Number);
(async()=>{const b=await chromium.launch();const res=[];
for(const W of widths){const ctx=await b.newContext({viewport:{width:W,height:900},isMobile:W<500});const p=await ctx.newPage();
 for(const L of langs)for(const pg of pages){
  await p.goto('file://'+F+'#/'+L+'/'+pg);await p.reload();await p.waitForTimeout(1500);
  await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});
  await p.evaluate(()=>{document.querySelectorAll('.cr').forEach(e=>e.classList.add('in'))});await p.waitForTimeout(200);
  const r=await p.evaluate(()=>{
    const hero=document.querySelector('section.hero-sub')||document.querySelector('.nm-ghero');if(!hero)return null;
    const st=(e,role)=>{const cs=getComputedStyle(e);const r=e.getBoundingClientRect();return {role,text:(e.textContent||'').trim().replace(/\s+/g,' ').slice(0,28),fs:cs.fontSize,lh:cs.lineHeight,ls:cs.letterSpacing,fw:cs.fontWeight,ws:cs.wordSpacing,ta:cs.textAlign,w:Math.round(r.width),h:Math.round(r.height)}};
    const out=[];const h1=hero.querySelector('h1');
    const vis=e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&getComputedStyle(e).visibility!=='hidden'};
    // breadcrumb: các span/a ngắn ở đầu hero trước eyebrow
    const bc=[...hero.querySelectorAll('span,a')].filter(e=>vis(e)&&!e.querySelector('*')&&e.compareDocumentPosition(h1)&Node.DOCUMENT_POSITION_FOLLOWING&&e.getBoundingClientRect().top<(h1.getBoundingClientRect().top-30));
    if(bc.length){out.push(st(bc[0],'breadcrumb-đầu'));out.push(st(bc[bc.length-1],'breadcrumb-cuối'))}
    // eyebrow: phần tử chữ hoa có letter-spacing, nằm ngay trước h1
    const eb=[...hero.querySelectorAll('div,span,p')].filter(e=>vis(e)&&!e.querySelector('div,span,p,h1')&&e.compareDocumentPosition(h1)&Node.DOCUMENT_POSITION_FOLLOWING&&getComputedStyle(e).textTransform==='uppercase'&&e.textContent.trim().length>2);
    if(eb.length)out.push(st(eb[eb.length-1],'eyebrow'));
    if(h1)out.push(st(h1,'h1'));
    const ps=[...hero.querySelectorAll('p')].filter(e=>vis(e)&&e.textContent.trim().length>30&&e.compareDocumentPosition(h1)&Node.DOCUMENT_POSITION_PRECEDING);
    if(ps.length)out.push(st(ps[0],'mô tả'));
    [...hero.querySelectorAll('a,button')].filter(e=>vis(e)&&!e.closest('.px-row,[data-keepgrid]')).forEach((e,i)=>{if(!e.compareDocumentPosition(h1)&Node.DOCUMENT_POSITION_FOLLOWING||true)out.push(st(e,'nút'+i))});
    return out});
  res.push({page:pg,lang:L,W,items:r||[]});
 }
 await ctx.close()}
await b.close();fs.writeFileSync(process.argv[3]||path.join(__dirname,'out','r5hero.json'),JSON.stringify(res,null,1));console.log('ok',res.length)})();
