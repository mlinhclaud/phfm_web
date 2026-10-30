// Rà chữ bị ép/giãn trên các trang con: đoạn có word-spacing khác 0, letter-spacing âm ở chữ thân bài (< 24px), hoặc text-align:justify.
//   HTML=dist/phfm-website.html WIDTHS="1440 1024 768 390" LANGS="vi en zh" node qa/r5spacing.js [out.json]
// Trang chủ không quét (trang chủ không đổi). Ghi JSON: từng đoạn {page, lang, W, text, ws, ls, ta, fs}. Thoát mã 1 nếu còn đoạn nào bị ép.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const F=path.resolve(process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
const pages=(process.env.PAGES||'about funds phvsf vnshine member portfolio advisory ir news academy careers contact guidePhvsf guideVnshine faq glossary forms terms privacy').split(' ');
const langs=(process.env.LANGS||'vi en zh').split(' ');const widths=(process.env.WIDTHS||'1440 1024 768 390').split(' ').map(Number);
(async()=>{const b=await chromium.launch();const res=[];let pagesDone=0;
for(const W of widths){const ctx=await b.newContext({viewport:{width:W,height:900},isMobile:W<500});const p=await ctx.newPage();
 for(const L of langs)for(const pg of pages){
  await p.goto('file://'+F+'#/'+L+'/'+pg);await p.reload();await p.waitForTimeout(1300);
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,25))}window.scrollTo(0,0)});
  await p.waitForTimeout(1200);
  const r=await p.evaluate(()=>{
    const out=[];const root=document.querySelector('main');if(!root)return out;
    const seen=new Set();
    const tw=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let n;
    while(n=tw.nextNode()){const t=n.textContent.replace(/\s+/g,' ').trim();if(t.length<2)continue;const e=n.parentElement;if(!e||seen.has(e))continue;seen.add(e);
      const r=e.getBoundingClientRect();if(r.width<2||r.height<2)continue;const cs=getComputedStyle(e);if(cs.visibility==='hidden'||cs.display==='none')continue;
      const ws=parseFloat(cs.wordSpacing)||0,ls=parseFloat(cs.letterSpacing)||0,fs=parseFloat(cs.fontSize);
      // text-align của khối chứa
      let blk=e;while(blk&&getComputedStyle(blk).display.startsWith('inline'))blk=blk.parentElement;const ta=blk?getComputedStyle(blk).textAlign:cs.textAlign;
      const multi=blk&&blk.getBoundingClientRect().height>parseFloat(getComputedStyle(blk).lineHeight||'20')*1.6;
      const bad=[];if(ws!==0)bad.push('word-spacing '+ws.toFixed(2)+'px');if(ls<-0.01&&fs<24)bad.push('letter-spacing '+ls.toFixed(2)+'px');if(ta==='justify'&&multi)bad.push('căn đều 2 lề');
      if(bad.length)out.push({text:t.slice(0,40),tag:e.tagName.toLowerCase(),ws,ls,fs,ta,bad:bad.join(' + ')});
    }
    return out});
  r.forEach(x=>res.push(Object.assign({page:pg,lang:L,W},x)));pagesDone++;
  console.log(W,L,pg,r.length)
 }
 await ctx.close()}
await b.close();fs.mkdirSync(path.join(__dirname,'out'),{recursive:true});fs.writeFileSync(process.argv[2]||path.join(__dirname,'out','r5spacing.json'),JSON.stringify(res,null,1));
console.log('Quét',pagesDone,'trang; đoạn bị ép/giãn/căn đều:',res.length);process.exit(res.length?1:0)})();
