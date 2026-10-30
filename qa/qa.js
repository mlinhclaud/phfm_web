// QA toàn site: chụp 20 trang × VI/EN × 1440/390, đo tràn ngang, chữ lỗi (undefined/NaN/{{ }}), link chết, lỗi console.
// Chạy: node qa/qa.js   (biến môi trường: PAGES="phvsf about", LANGS="vi", WIDTHS="390")
// Kết quả: qa/out/audit.json, qa/out/shots/*.png. Lệnh trả mã 1 nếu có trang tràn ngang hoặc lỗi JS.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const F=path.join(__dirname,'..','dist','phfm-website.html');const OUT=path.join(__dirname,'out');fs.mkdirSync(OUT+'/shots',{recursive:true});
const map={};
const pages=(process.env.PAGES||'home about funds phvsf vnshine member portfolio advisory ir news academy careers contact guidePhvsf guideVnshine faq glossary forms terms privacy').split(' ');
const langs=(process.env.LANGS||'vi en').split(' ');const widths=(process.env.WIDTHS||'1440 390').split(' ').map(Number);
(async()=>{
 const b=await chromium.launch();const res=[];
 for(const W of widths){
 const ctx=await b.newContext({viewport:{width:W,height:W>500?900:844},isMobile:W<500,hasTouch:W<500});
 const ext=new Set();
 await ctx.route('**/*',r=>{const u=r.request().url();if(/^(file|data|blob|about):/.test(u))return r.continue();
   const k=Object.keys(map).find(k=>u.includes(k));if(k)return r.fulfill({path:map[k],contentType:'application/javascript'});
   ext.add(u.slice(0,120));return r.abort();});
 const p=await ctx.newPage();let errs=[];p.on('console',m=>{if(m.type()==='error'||m.type()==='warning')errs.push(m.type()+': '+m.text().slice(0,180))});p.on('pageerror',e=>errs.push('pageerror: '+e.message.slice(0,180)));
 for(const L of langs)for(const pg of pages){errs=[];
  await p.goto('about:blank');await p.goto('file://'+F+'#/'+L+'/'+pg);await p.waitForTimeout(2500);
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,50))}window.scrollTo(0,0)});
  await p.waitForTimeout(600);
  const info=await p.evaluate((W)=>{
   const vis=e=>{const r=e.getBoundingClientRect();const cs=getComputedStyle(e);return r.width>0&&r.height>0&&cs.visibility!=='hidden'&&cs.display!=='none'&&+cs.opacity!==0};
   const path=e=>{let s=[];while(e&&e!==document.body&&s.length<4){s.unshift(e.tagName.toLowerCase()+(e.id?'#'+e.id:'')+(e.classList.length?'.'+[...e.classList].slice(0,2).join('.'):''));e=e.parentElement}return s.join('>')};
   const out={};out.title=document.title;out.h1=[...document.querySelectorAll('h1')].filter(vis).map(h=>h.textContent.trim().slice(0,60));
   out.sw=document.documentElement.scrollWidth;out.h=document.documentElement.scrollHeight;
   const over=[];document.querySelectorAll('main *, header *, footer *').forEach(e=>{if(!vis(e))return;const r=e.getBoundingClientRect();if(r.right>W+2&&r.width<W*3){let a=e.parentElement,clip=false;while(a&&a!==document.body){const o=getComputedStyle(a).overflowX;if(o!=='visible'){clip=true;break}a=a.parentElement}if(!clip)over.push(path(e)+' right='+Math.round(r.right)+' "'+(e.textContent||'').trim().slice(0,40)+'"')}});
   out.over=over.slice(0,8);out.overN=over.length;
   const tw=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);const bad=[];let n;while(n=tw.nextNode()){const t=n.textContent;if((/\bNaN\b/.test(t)||/undefined|\{\{|\bnull\b|\[object|Lorem/i.test(t))&&n.parentElement&&vis(n.parentElement)&&!/SCRIPT|STYLE/.test(n.parentElement.tagName))bad.push(path(n.parentElement)+': '+t.trim().slice(0,80))}
   out.bad=bad.slice(0,10);
   document.querySelectorAll('[title],[alt],[placeholder],[aria-label]').forEach(e=>{for(const a of ['title','alt','placeholder','aria-label']){const v=e.getAttribute(a);if(v&&(/\bNaN\b/.test(v)||/undefined|\{\{/.test(v)))out.bad.push('@'+a+' '+path(e)+': '+v.slice(0,60))}});
   out.deadLinks=[...document.querySelectorAll('a')].filter(a=>vis(a)&&(a.getAttribute('href')==='#'||a.getAttribute('href')===''||(!a.hasAttribute('href')))).map(a=>(a.textContent||a.getAttribute('aria-label')||'').trim().slice(0,40)).slice(0,30);
   const dpr=W<500?2:1.5;out.imgs=[...document.querySelectorAll('img')].filter(vis).map(i=>{const r=i.getBoundingClientRect();const src=i.currentSrc||i.src;return {src:src.startsWith('data:')?'data:'+src.length:src.slice(0,90),nat:i.naturalWidth+'x'+i.naturalHeight,disp:Math.round(r.width)+'x'+Math.round(r.height),broken:i.complete&&i.naturalWidth===0,low:i.naturalWidth>0&&i.naturalWidth<r.width*dpr*0.75,alt:i.getAttribute('alt')}});
   const bgs=[];document.querySelectorAll('main *,header *,footer *,section').forEach(e=>{if(!vis(e))return;const bi=getComputedStyle(e).backgroundImage;if(bi&&bi.startsWith('url(')){const r=e.getBoundingClientRect();bgs.push({src:bi.slice(4,60),disp:Math.round(r.width)+'x'+Math.round(r.height)})}});out.bgs=bgs.slice(0,30);
   const col={};const add=(c,k)=>{if(!c||c==='rgba(0, 0, 0, 0)'||c==='transparent')return;const key=k+' '+c;col[key]=(col[key]||0)+1};
   document.querySelectorAll('body *').forEach(e=>{if(!vis(e))return;const cs=getComputedStyle(e);add(cs.backgroundColor,'bg');add(cs.color,'fg');if(parseFloat(cs.borderTopWidth)>0)add(cs.borderTopColor,'bd');if(cs.backgroundImage.includes('gradient'))add(cs.backgroundImage.slice(0,120),'grad')});
   out.colors=col;out.fonts=[...new Set([...document.querySelectorAll('body *')].slice(0,3000).map(e=>getComputedStyle(e).fontFamily.split(',')[0]))];
   out.lang=document.documentElement.lang;return out},W);
  await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});await p.evaluate(()=>{document.querySelectorAll('.cr').forEach(e=>e.classList.add('in'));document.documentElement.style.scrollSnapType='none'});await p.waitForTimeout(300);const name=`${pg}.${L}.${W}`;await p.screenshot({path:OUT+'/shots/'+name+'.png',fullPage:true});
  info.errs=[...new Set(errs)];info.name=name;res.push(info);console.log(name,info.h,info.sw,'over',info.overN,'bad',info.bad.length,'dead',info.deadLinks.length,'err',info.errs.length);
 }
 res.push({ext:[...ext],W});await ctx.close();}
 fs.writeFileSync(OUT+'/audit.json',JSON.stringify(res,null,1));await b.close();
 const fail=res.filter(r=>r.name&&(r.overN>0||r.errs.some(e=>e.startsWith('pageerror'))));
 if(fail.length){console.log('FAIL',fail.map(r=>r.name).join(', '));process.exit(1)}console.log('QA OK',res.filter(r=>r.name).length,'lượt');})();
