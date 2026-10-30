// Kiểm gạch chân vàng của menu header ở mọi trạng thái: rê chuột, mục đang chọn, focus bàn phím, dropdown, rê vào mục con.
//   HTML=dist/phfm-website.html OUT=qa/out/menu WIDTHS="1440 1024" node qa/r5menu.js
// Vòng focus không phải vàng không tính là gạch (in riêng sau chữ 'vòng').
// Với mỗi (trang, độ rộng, trạng thái) đếm số "gạch vàng" nhìn thấy trong từng mục menu: ::after có scaleX>0, phần tử con cao 2-3px nền vàng,
// border-bottom, text-decoration underline, outline. Mục nào có hơn 1 gạch thì in "HAI GẠCH". Chụp ảnh phóng to (x2) vùng menu vào OUT.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const F=path.resolve(process.env.HTML||path.join(__dirname,'..','dist','phfm-website.html'));
const OUT=process.env.OUT||path.join(__dirname,'out','menu');fs.mkdirSync(OUT,{recursive:true});
const widths=(process.env.WIDTHS||'1440 1024').split(' ').map(Number);
const routes=(process.env.ROUTES||'/vi/home /vi/about /vi/phvsf /vi/vnshine').split(' ');
const probe=()=>{
  const res=[];const ring=[];
  document.querySelectorAll('header .th-nav>div:not(.th-ntrade)').forEach((it,i)=>{
    const lines=[];
    const ir=it.getBoundingClientRect();
    const gold=c=>/rgb\(233, 196, 106\)|rgb\(192, 150, 45\)|rgb\(242, 210, 125\)/.test(c);
    const pa=getComputedStyle(it,'::after');
    if(pa.content!=='none'&&pa.display!=='none'){const m=pa.transform.match(/matrix\(([^)]+)\)/);const sx=m?parseFloat(m[1].split(',')[0]):1;
      if(gold(pa.backgroundColor)&&sx>0.05&&parseFloat(pa.height)>0)lines.push('::after '+pa.height+' scaleX '+sx.toFixed(2)+' bottom '+pa.bottom)}
    const pb=getComputedStyle(it,'::before');if(pb.content!=='none'&&pb.display!=='none'&&gold(pb.backgroundColor))lines.push('::before');
    it.querySelectorAll(':scope>div:not(.th-mega)').forEach(d=>{const r=d.getBoundingClientRect();const cs=getComputedStyle(d);if(r.height>0&&r.height<=4&&gold(cs.backgroundColor)&&cs.display!=='none')lines.push('div-active '+Math.round(r.height)+'px bottom '+cs.bottom)});
    const b=it.querySelector(':scope>button');
    if(b){const cs=getComputedStyle(b);
      if(parseFloat(cs.borderBottomWidth)>0&&cs.borderBottomStyle!=='none')lines.push('button border-bottom '+cs.borderBottomWidth+' '+cs.borderBottomColor);
      if(cs.textDecorationLine&&cs.textDecorationLine!=='none')lines.push('button text-decoration '+cs.textDecorationLine);
      if(cs.boxShadow&&cs.boxShadow!=='none'&&/inset|0px [1-3]px 0px/.test(cs.boxShadow))lines.push('button box-shadow '+cs.boxShadow);
      if(document.activeElement===b&&cs.outlineStyle!=='none'&&parseFloat(cs.outlineWidth)>0){if(gold(cs.outlineColor))lines.push('focus outline vàng');else ring.push(it.textContent.trim().slice(0,12)+' vòng '+cs.outlineWidth+' '+cs.outlineColor+' offset '+cs.outlineOffset)}
      const pba=getComputedStyle(b,'::after');if(pba.content!=='none'&&pba.display!=='none'&&gold(pba.backgroundColor))lines.push('button::after');}
    res.push({i,ring,text:(it.textContent||'').trim().slice(0,22),lines});
  });
  return res};
(async()=>{const br=await chromium.launch();const rows=[];let bad=0;
for(const W of widths){const ctx=await br.newContext({viewport:{width:W,height:900},deviceScaleFactor:2});const p=await ctx.newPage();
 for(const route of routes){
  await p.goto('file://'+F+'#'+route);await p.reload();await p.waitForTimeout(1800);
  await p.addStyleTag({content:'*,*::before,*::after{transition:none!important;animation:none!important}'});
  const burger=W<1280;
  const states=[];
  const items='header .th-nav>div:not(.th-ntrade)';
  const run=async(name,setup)=>{await p.mouse.move(5,600);if(!burger)await p.keyboard.press('Escape');await p.evaluate(()=>{if(document.activeElement)document.activeElement.blur()});await p.waitForTimeout(150);
    if(setup)await setup();await p.waitForTimeout(250);
    const r=await p.evaluate(probe);const hdr=await p.$('header');const bb=await hdr.boundingBox();
    const file=`${OUT}/${route.replace(/\W+/g,'_')}.${W}.${name}.png`;
    await p.screenshot({path:file,clip:{x:0,y:Math.max(0,bb.y),width:W,height:Math.min(bb.height+(name.startsWith('menu')||name.startsWith('sub')?330:6),900)}});
    const two=r.filter(x=>x.lines.length>1);bad+=two.length;
    rows.push({route,W,state:name,items:r.filter(x=>x.lines.length),two:two.map(x=>x.text)});
    console.log(`${route} ${W} ${name}:`,r.filter(x=>x.lines.length).map(x=>x.text+' ['+x.lines.join(' + ')+']').join(' | ')||'(không gạch)',two.length?'  <<< HAI GẠCH ở '+two.map(x=>x.text).join(', '):'')};
  if(burger){
    await run('idle-dong');
    await p.click('.th-burg button:last-child');await p.waitForTimeout(300);
    await run('burger-mo');
    const n=await p.locator(items).count();
    for(let i=0;i<n;i++){await run('rechuot-muc'+i,async()=>{await p.locator(items).nth(i).locator('>button').hover()})}
    await run('focus-muc0',async()=>{await p.locator(items).nth(0).locator('>button').focus()});
    await run('dropdown-mo',async()=>{await p.locator(items).nth(1).locator('>button').click()});
    await run('dropdown-sub-hover',async()=>{const m=p.locator('.th-mega [style*="cursor:pointer"]').first();if(await m.count())await m.hover()});
    continue}
  await run('idle');
  const n=await p.locator(items).count();
  for(let i=0;i<n;i++){
    const it=p.locator(items).nth(i);
    await run('rechuot-muc'+i,async()=>{await it.hover()});
  }
  await run('focus-muc0',async()=>{await p.keyboard.press('Tab');await p.locator(items).nth(0).locator('>button').focus()});
  await run('focus-muc1',async()=>{await p.locator(items).nth(1).locator('>button').focus()});
  await run('menu-mo',async()=>{await p.locator(items).nth(1).hover()});
  await run('sub-hover',async()=>{await p.locator(items).nth(1).hover();await p.waitForTimeout(200);const m=p.locator('.th-mega [style*="cursor:pointer"]').first();if(await m.count())await m.hover()});
  await run('menu-mo-roi-di-muc2',async()=>{await p.locator(items).nth(1).hover();await p.waitForTimeout(200);await p.locator(items).nth(2).hover()});
 }
 await ctx.close()}
await br.close();fs.writeFileSync(path.join(OUT,'menu.json'),JSON.stringify(rows,null,1));console.log('Số lần thấy hai gạch trong một mục:',bad);process.exit(bad?1:0)})();
