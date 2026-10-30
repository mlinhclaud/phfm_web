// Kiểm R6-03: nút Tải về (hiện thông báo, không đổi route), link sang trang Biểu mẫu, bước 03 cùng kiểu bước 01/02, tràn ngang.
// node qa/r6forms.js
const {chromium}=require('playwright');const path=require('path');const F=path.resolve(process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
(async()=>{const b=await chromium.launch();let bad=0;
for(const W of [1440,390])for(const L of ['vi','en','zh']){
 const p=await (await b.newContext({viewport:{width:W,height:900},isMobile:W<500})).newPage();
 const log=(ok,m)=>{if(!ok)bad++;console.log(W,L,ok?'OK ':'LOI',m)};
 // Hướng dẫn PHVSF
 await p.goto('file://'+F+'#/'+L+'/guidePhvsf');await p.waitForTimeout(2200);
 const n=await p.$$eval('.r6b-dl',e=>e.length);log(n===5,'guidePhvsf: số nút Tải về = '+n+' (4 biểu mẫu + 1 trong danh sách hồ sơ)');
 for(let i=0;i<n;i++){const el=p.locator('.r6b-dl').nth(i);await el.scrollIntoViewIfNeeded();await el.click();await p.waitForTimeout(250);
  const t=await p.$eval('.phfm-toast',e=>e.textContent+'|'+e.classList.contains('on')).catch(()=>'none');const h=await p.evaluate(()=>location.hash);
  log(/\|true$/.test(t)&&h==='#/'+L+'/guidePhvsf','nút '+i+' toast='+t+' hash='+h);await p.evaluate(()=>{const t=document.querySelector('.phfm-toast');t&&t.classList.remove('on')})}
 const sw=await p.evaluate(()=>document.documentElement.scrollWidth);log(sw<=W,'guidePhvsf scrollWidth='+sw);
 const lk=p.locator('#r6-forms a:not(.r6b-dl)');await lk.scrollIntoViewIfNeeded();const lt=(await lk.textContent()).trim();await lk.click();await p.waitForTimeout(800);
 log(await p.evaluate(()=>location.hash)==='#/'+L+'/forms','link "'+lt+'" -> '+await p.evaluate(()=>location.hash));
 // Học viện
 await p.goto('about:blank');await p.goto('file://'+F+'#/'+L+'/academy');await p.waitForTimeout(2200);
 const card=p.locator('.r6b-acard');log(await card.count()===1,'academy: có thẻ Biểu mẫu: '+(await card.innerText()).replace(/\s+/g,' ').slice(0,120));
 const cb=card.getByText('→');await cb.scrollIntoViewIfNeeded();await cb.click();await p.waitForTimeout(800);
 log(await p.evaluate(()=>location.hash)==='#/'+L+'/forms','academy thẻ -> '+await p.evaluate(()=>location.hash));
 await p.goto('about:blank');await p.goto('file://'+F+'#/'+L+'/academy');await p.waitForTimeout(2200);
 const sw2=await p.evaluate(()=>document.documentElement.scrollWidth);log(sw2<=W,'academy scrollWidth='+sw2);
 // Bước 03 VNSHINE: ba li cùng kiểu
 await p.goto('about:blank');await p.goto('file://'+F+'#/'+L+'/guideVnshine');await p.waitForTimeout(2200);
 const st=await p.$$eval('#thu-cap ol>li',lis=>lis.map(li=>{const sp=li.querySelectorAll('div>span');return [sp[0].textContent.trim(),getComputedStyle(sp[0]).backgroundColor,sp[1].getBoundingClientRect().width>60,sp.length].join('/')}));
 const nb=st[0].split('/').slice(1).join('/'),same=st.every((x,i)=>x.split('/').slice(1).join('/')===nb);log(same&&st[2].startsWith('03'),'VNSHINE bước: '+st.join(' | '));
 await p.context().close()}
await b.close();console.log(bad?('CO '+bad+' LOI'):'R6-03 OK');process.exit(bad?1:0)})();
