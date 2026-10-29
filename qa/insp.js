// Đọc nhanh DOM một trang: node qa/insp.js /vi/phvsf 1440 "document.title"
const {chromium}=require('playwright');const path=require('path');const F=path.join(__dirname,'..','dist','phfm-website.html');
const [route,W,js]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:+W,height:900},isMobile:+W<500})).newPage();
await p.goto('file://'+F+'#'+route);await p.waitForTimeout(2500);console.log(JSON.stringify(await p.evaluate(js),null,1));await b.close()})();
