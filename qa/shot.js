// Chụp một phần tử: node qa/shot.js /vi/vnshine 1440 ".pd-cell" qa/out/pd.png
const {chromium}=require('playwright');const path=require('path');const F=path.join(__dirname,'..','dist','phfm-website.html');
const [route,W,sel,out]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:+W,height:900},isMobile:+W<500})).newPage();
await p.goto('file://'+F+'#'+route);await p.waitForTimeout(2500);
await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,40))}document.querySelectorAll('.cr').forEach(e=>e.classList.add('in'))});
const e=await p.$(sel);if(!e){console.log('Không thấy',sel);process.exit(1)}await e.scrollIntoViewIfNeeded();await p.waitForTimeout(500);await e.screenshot({path:out});await b.close();console.log('OK',out)})();
