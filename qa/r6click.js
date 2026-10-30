// Bấm thẻ phương thức thứ N (0/1) ở Hướng dẫn VNSHINE rồi chụp màn hình: node qa/r6click.js /en/guideVnshine 1440 1 out.jpg
const {chromium}=require('playwright');const path=require('path');const F=path.resolve(process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
const [route,W,idx,out]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:+W,height:900},isMobile:+W<500})).newPage();
await p.goto('file://'+F+'#'+route);await p.waitForTimeout(2500);
const c=p.locator('main a',{hasText:/View details|Xem chi tiết|查看詳情/}).nth(+idx);await c.scrollIntoViewIfNeeded();await c.click();await p.waitForTimeout(1500);
console.log(await p.evaluate(()=>location.hash+' y='+Math.round(scrollY)));await p.screenshot({path:out,type:'jpeg',quality:70});await b.close()})();
