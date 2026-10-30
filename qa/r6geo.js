// Đo hình học trang con để so hai build: node qa/r6geo.js <file.html> <out.json>
// Biến môi trường: PAGES, LANGS (mặc định vi), WIDTHS (mặc định "1440 1024 390").
// Mỗi trang ghi: khối cấp 1 của <main> (và thanh mục con) gồm top/height/padding/margin; các phần tử chữ (h1-h4, p, a, button, li, span lá)
// gồm toạ độ tương đối với khối chứa, rộng/cao, cỡ chữ, line-height, giãn chữ; ảnh (img) gồm toạ độ và kích thước.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const F=path.resolve(process.argv[2]||process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
const pages=(process.env.PAGES||'about funds phvsf vnshine member portfolio advisory ir news academy careers contact guidePhvsf guideVnshine faq glossary forms terms privacy').split(' ');
const langs=(process.env.LANGS||'vi').split(' ');const widths=(process.env.WIDTHS||'1440 1024 390').split(' ').map(Number);
(async()=>{const b=await chromium.launch();const res=[];
for(const W of widths){const ctx=await b.newContext({viewport:{width:W,height:900},isMobile:W<500});const p=await ctx.newPage();
 for(const L of langs)for(const pg of pages){
  await p.goto('about:blank');await p.goto('file://'+F+'#/'+L+'/'+pg);await p.reload();await p.waitForTimeout(1600);
  await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=500){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,30))}window.scrollTo(0,0);document.querySelectorAll('.cr').forEach(e=>e.classList.add('in'))});await p.waitForTimeout(400);
  const r=await p.evaluate(()=>{
    const R=e=>{const r=e.getBoundingClientRect();return {x:Math.round(r.left*10)/10,y:Math.round((r.top+scrollY)*10)/10,w:Math.round(r.width*10)/10,h:Math.round(r.height*10)/10}};
    const vis=e=>{const r=e.getBoundingClientRect();const cs=getComputedStyle(e);return r.width>0&&r.height>0&&cs.visibility!=='hidden'&&cs.display!=='none'};
    const main=document.querySelector('main');const out={h:document.documentElement.scrollHeight,blocks:[],texts:[],imgs:[]};
    const hdr=document.querySelector('header');out.header=hdr?R(hdr):null;
    // khối cấp 1: anh em của main và con của main nằm giữa header và footer
    const kids=[];const nm=[...document.querySelectorAll('.nm-sbar,.nm-gnav,.nm-ghero')];
    const top=[...(main?main.children:[])];
    const all=[...new Set([...nm,...top])].filter(e=>vis(e)&&!/^(SCRIPT|STYLE)$/.test(e.tagName)).sort((a,b)=>a.getBoundingClientRect().top-b.getBoundingClientRect().top);
    all.forEach((e,i)=>{const cs=getComputedStyle(e);const g=R(e);
      const inner=e.firstElementChild&&vis(e.firstElementChild)?getComputedStyle(e.firstElementChild):null;const ig=e.firstElementChild&&vis(e.firstElementChild)?R(e.firstElementChild):null;
      out.blocks.push({i,id:e.id||'',cls:(e.className&&e.className.baseVal===undefined?e.className:'').toString().split(' ').filter(c=>/^(nm-|fh|dh|hero|ab-)/.test(c)).join(' '),...g,
        pad:[cs.paddingTop,cs.paddingRight,cs.paddingBottom,cs.paddingLeft].map(parseFloat),mar:[cs.marginTop,cs.marginBottom].map(parseFloat),
        inner:ig?{x:ig.x,y:Math.round((ig.y-g.y)*10)/10,w:ig.w,h:ig.h,pad:[inner.paddingTop,inner.paddingRight,inner.paddingBottom,inner.paddingLeft].map(parseFloat),mar:[inner.marginTop,inner.marginBottom].map(parseFloat)}:null});
      e.__bi=i;e.__top=g.y});
    const blockOf=e=>{let a=e;while(a){if(a.__bi!==undefined)return a;a=a.parentElement}return null};
    const seen={};
    const els=[...document.querySelectorAll('header h1, main h1,main h2,main h3,main h4,main p,main a,main button,main li,main label,main td,main th,main span,main div,.nm-sbar button,.nm-gnav button,.nm-gnav a,.nm-ghero *')];
    const uniq=[...new Set(els)];
    uniq.forEach(e=>{if(!vis(e))return;if(e.closest('[data-hm]')&&false)return;
      // phần tử lá chữ: có node chữ trực tiếp, không con khối chứa chữ
      let direct='';e.childNodes.forEach(n=>{if(n.nodeType===3)direct+=n.textContent});direct=direct.trim().replace(/\s+/g,' ');
      if(!direct)return;const bl=blockOf(e);if(!bl)return;const cs=getComputedStyle(e);const g=R(e);
      const key=(bl.id||('b'+bl.__bi))+'|'+e.tagName+'|'+direct.slice(0,36);seen[key]=(seen[key]||0)+1;
      out.texts.push({k:key+'|'+seen[key],dx:g.x,dy:Math.round((g.y-bl.__top)*10)/10,w:g.w,h:g.h,fs:parseFloat(cs.fontSize),lh:cs.lineHeight==='normal'?'normal':parseFloat(cs.lineHeight),ls:cs.letterSpacing==='normal'?0:parseFloat(cs.letterSpacing),fw:cs.fontWeight})});
    document.querySelectorAll('main img').forEach((e,i)=>{if(!vis(e))return;const bl=blockOf(e);const g=R(e);out.imgs.push({k:(bl?(bl.id||('b'+bl.__bi)):'-')+'|img|'+i,dx:g.x,dy:bl?Math.round((g.y-bl.__top)*10)/10:g.y,w:g.w,h:g.h})});
    return out});
  res.push({page:pg,lang:L,W,...r});
 }
 await ctx.close()}
await b.close();fs.writeFileSync(process.argv[3]||path.join(__dirname,'out','r6geo.json'),JSON.stringify(res));console.log('ok',res.length)})();
