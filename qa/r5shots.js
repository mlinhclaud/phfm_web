// Chụp trang cho bản xem trước R5: HTML=dist/phfm-website-r5a.html OUT=qa/out/r5a PAGES="about vnshine member" LANGS="vi en" WIDTHS="1440 390" node qa/r5shots.js
// Mỗi trang ra 2 ảnh: <page>.<lang>.<W>.full.png (cả trang) và <page>.<lang>.<W>.top.png (màn hình đầu).
// SBAR_ON=1: gán class r5-on cho mục đầu của thanh mục con để mô phỏng trạng thái "đang chọn" (bản chính chưa có scroll-spy).
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const F=path.resolve(process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
const OUT=process.env.OUT||path.join(__dirname,'out','r5');fs.mkdirSync(OUT,{recursive:true});
const pages=(process.env.PAGES||'home about vnshine member').split(' ');
const langs=(process.env.LANGS||'vi en').split(' ');const widths=(process.env.WIDTHS||'1440 390').split(' ').map(Number);
(async()=>{const b=await chromium.launch();
for(const W of widths){const H=W>500?900:844;
 const ctx=await b.newContext({viewport:{width:W,height:H},isMobile:W<500,hasTouch:W<500});const p=await ctx.newPage();
 for(const L of langs)for(const pg of pages){
  await p.goto('file://'+F+'#/'+L+'/'+pg);await p.reload();await p.waitForTimeout(1800);
  await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});
  await p.evaluate(async(on)=>{window.scrollTo(0,0);if(on){const b=document.querySelector('.nm-sbar button');if(b)b.classList.add('r5-on')}
    for(let y=0;y<document.body.scrollHeight;y+=500){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,30))}
    document.querySelectorAll('.cr').forEach(e=>e.classList.add('in'));document.documentElement.style.scrollSnapType='none';window.scrollTo(0,0)},!!process.env.SBAR_ON);
  if(W>500)await p.mouse.move(W/2,400); // giữ banner trang chủ đứng yên ở slide 1
  await p.waitForTimeout(400);
  const n=`${pg}.${L}.${W}`;
  await p.screenshot({path:`${OUT}/${n}.top.png`});
  await p.screenshot({path:`${OUT}/${n}.full.png`,fullPage:true});
  // khối đổi màu: Lịch sử hình thành (about), Thông tin giao dịch (vnshine), ảnh từng khối cho bản so sánh
  for(const [pp,sel,nm] of [['about','#ab-journey','journey'],['vnshine','#sec-trading','trading'],['phvsf','#sec-overview .fit','fit']]){
    if(pp!==pg)continue;const e=await p.$(sel);if(!e)continue;await e.scrollIntoViewIfNeeded();await p.waitForTimeout(200);await e.screenshot({path:`${OUT}/${n}.${nm}.png`});}
  console.log(n);
 }
 await ctx.close();}
await b.close()})();
