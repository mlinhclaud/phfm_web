const {chromium}=require('playwright');const path=require('path');
const F=path.resolve(process.argv[2]);
(async()=>{const b=await chromium.launch();
for(const W of [1440,390]) for(const pg of ['guideVnshine','guidePhvsf']) for(const L of ['vi','en','zh']){
 const p=await (await b.newContext({viewport:{width:W,height:900},isMobile:W<500})).newPage();
 await p.goto('file://'+F+'#/'+L+'/'+pg);await p.waitForTimeout(2200);
 const n=await p.evaluate(()=>[...document.querySelectorAll('a')].filter(a=>{const h=a.getAttribute('href');return h&&h[0]=='#'&&h.slice(0,2)!='#/'}).map(a=>a.getAttribute('href')+'|'+a.textContent.replace(/\s+/g,' ').trim().slice(0,30)));
 const noh=await p.evaluate(()=>[...document.querySelectorAll('main a:not([href])')].map(a=>a.textContent.replace(/\s+/g,' ').trim().slice(0,30)));
 const res=[];
 for(let i=0;i<n.length+noh.length;i++){
  const els=await p.$$('main a');
  const arr=[];for(const e of els){const h=await e.getAttribute('href');if(h===null||(h[0]=='#'&&h.slice(0,2)!='#/'))arr.push(e)}
  if(!arr[i])break;
  const before=await p.evaluate(()=>location.hash);
  await arr[i].scrollIntoViewIfNeeded();await arr[i].click();await p.waitForTimeout(900);
  const after=await p.evaluate(()=>({h:location.hash,y:Math.round(scrollY)}));
  res.push((await arr[i].textContent()).replace(/\s+/g,' ').trim().slice(0,22)+' => '+after.h+' y'+after.y+(before===after.h?'':' ROUTE?'));
  await p.evaluate(h=>{location.hash=h},before);await p.waitForTimeout(500);
 }
 console.log(W,L,pg,'hash-anchors:',n.length,'nohref:',noh.length,JSON.stringify(res));
 await p.context().close();
}
await b.close()})();
