// Đo cột năm của Lịch sử hình thành (Về chúng tôi): có xuống dòng không, có tràn sang chữ bên cạnh không. node qa/r5year.js
const {chromium}=require('playwright');const path=require('path');
const F=path.resolve(process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
(async()=>{const b=await chromium.launch();let nbad=0;
for(const W of [1440,1280,1024,768,390,360])for(const L of ['vi','en','zh']){
 const p=await (await b.newContext({viewport:{width:W,height:900}})).newPage();
 await p.goto('file://'+F+'#/'+L+'/about');await p.waitForTimeout(1800);
 const r=await p.evaluate(()=>[...document.querySelectorAll('.ab-j-y')].map(e=>{const bb=e.getBoundingClientRect(),n=e.nextElementSibling.getBoundingClientRect(),rg=document.createRange();rg.selectNodeContents(e);const tw=rg.getBoundingClientRect().width;return {t:e.textContent.trim(),w:Math.round(bb.width),h:Math.round(bb.height),sw:Math.round(tw),cw:Math.round(bb.width),gap:Math.round(n.left-(bb.left+tw))}}));
 const bad=r.filter(x=>x.h>24||x.sw>x.cw||x.gap<8);nbad+=bad.length;
 console.log(W,L,'n',r.length,'cao max',Math.max(...r.map(x=>x.h)),'khoảng cách tối thiểu tới chữ',Math.min(...r.map(x=>x.gap)),'chữ rộng nhất',JSON.stringify(r.reduce((a,x)=>x.sw>a.sw?x:a,r[0])),'lỗi',bad.length);
 await p.close();}
await b.close();console.log(nbad?'CÓ LỖI':'OK');process.exit(nbad?1:0)})();
