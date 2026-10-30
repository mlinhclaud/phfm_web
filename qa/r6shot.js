// Chụp một dải trang bắt đầu từ phần tử: node qa/r6shot.js /vi/guidePhvsf 1440 "#buoc-04" 0 1100 out.jpg   (HTML=... để chụp bản khác)
const {chromium}=require('playwright');const path=require('path');const F=path.resolve(process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
const [route,W,sel,off,h,out]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:+W,height:900},isMobile:+W<500})).newPage();
await p.goto('file://'+F+'#'+route);await p.waitForTimeout(2500);
await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,40))}document.querySelectorAll('.cr').forEach(e=>e.classList.add('in'));window.scrollTo(0,0)});
await p.waitForTimeout(1800);
const top=await p.evaluate(s=>{const e=document.querySelector(s);return e?Math.round(e.getBoundingClientRect().top+scrollY):-1},sel);
if(top<0){console.log('Không thấy',sel);process.exit(1)}
await p.screenshot({path:out,type:'jpeg',quality:72,fullPage:true,clip:{x:0,y:Math.max(0,top+(+off)),width:+W,height:+h}});await b.close();console.log('OK',out)})();
