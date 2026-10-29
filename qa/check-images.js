// Kiểm ảnh hero + ảnh bài Góc nhìn (R4-09): mỗi vị trí phải hiện đúng khoá ảnh, không trùng khoá giữa các vị trí.
// Chạy: node qa/check-images.js   (cần dist/phfm-website.html đã build). Trả mã 1 nếu sai.
const {chromium}=require('playwright');const path=require('path');
const F=path.join(__dirname,'..','dist','phfm-website.html');
// [mã, trang, selector ảnh (lấy phần tử nhìn thấy đầu tiên), khoá mong đợi]
const HERO=[
 ['H1','about','#ab-overview img[src^="data:"]','r5_about_hero'],
 ['H2','phvsf','.fh>img','r5_phvsf_hero'],['H3','vnshine','.fh>img','r5_vns_hero'],
 ['H4','member','img.hero-pic','r5_member_hero'],['H5','portfolio','img.hero-pic','r5_pf_hero'],['H6','advisory','img.hero-pic','r5_adv_hero'],
 ['H7','academy','.dh.hero-sub img[src^="data:"]:not([style*="opacity"])','r5_acad_hero'],
 ['H8','careers','.dh.hero-sub .hero-in img','r5_cr_hero'],
 ['H9','guidePhvsf','.nm-ghero>img.gh-pic','r5_gp_hero'],['H10','guideVnshine','.nm-ghero>img.gh-pic','r5_gv_hero']];
const NEWS=[['N1','r5_nw_msci'],['N2','r5_nw_rot'],['N3','r5_nw_macro'],['N4','r5_nw_rebal'],['N5','r5_nw_aug'],['N6','r5_nw_fund'],['N7','r5_nw_bank'],['N8','r5_nw_dca'],['N9','r5_nw_h2'],['N10','r5_nw_div']];
const ALT={H9:{vi:'Nhà đầu tư xem ứng dụng đầu tư trên điện thoại',en:'An investor checking an investing app on a phone',zh:'投資人在手機上查看投資應用程式'},
           H10:{vi:'Màn hình theo dõi giá và NAV của quỹ ETF',en:'Screens tracking ETF price and NAV',zh:'追蹤 ETF 價格與 NAV 的螢幕'}};
(async()=>{const b=await chromium.launch();const seen={};let bad=0;const rows=[];
 for(const W of [1440,390]){const p=await (await b.newContext({viewport:{width:W,height:900},isMobile:W<500})).newPage();
  for(const L of ['vi','en','zh']){
   for(const [id,pg,sel,key] of HERO){
    if(L==='zh'&&!/^guide/.test(pg))continue;
    await p.goto('about:blank');await p.goto('file://'+F+'#/'+L+'/'+pg);await p.waitForTimeout(1500);
    const r=await p.evaluate(([sel,key])=>{const e=[...document.querySelectorAll(sel)].find(e=>e.getBoundingClientRect().width>50);
     if(!e)return {ok:false,why:'không thấy ảnh'};return {ok:e.src===window.__I[key]&&e.complete&&e.naturalWidth>0,alt:e.getAttribute('alt'),w:Math.round(e.getBoundingClientRect().width)}},[sel,key]);
    let ok=r.ok;if(ALT[id]&&r.alt!==ALT[id][L])ok=false;if(!ALT[id]&&r.alt!=='')ok=false;
    (seen[id]=seen[id]||[]).push((ok?'OK ':'SAI ')+L+' '+W);if(!ok){bad++;console.log('SAI',id,pg,L,W,JSON.stringify(r))}
   }
   if(L==='zh')continue;
   await p.goto('about:blank');await p.goto('file://'+F+'#/'+L+'/news');await p.waitForTimeout(1800);
   for(const [id,key] of NEWS){const ok=await p.evaluate(key=>[...document.querySelectorAll('main img')].some(e=>e.src===window.__I[key]&&e.getBoundingClientRect().width>50&&e.naturalWidth>0),key);
    (seen[id]=seen[id]||[]).push((ok?'OK ':'SAI ')+L+' '+W);if(!ok){bad++;console.log('SAI',id,L,W)}}
  }}
 // không trùng khoá giữa các vị trí
 const keys=[...HERO.map(h=>h[3]),...NEWS.map(n=>n[1])];const dup=keys.filter((k,i)=>keys.indexOf(k)!==i);
 if(dup.length){bad++;console.log('TRÙNG KHOÁ',dup)}
 const keyOf=Object.fromEntries([...HERO.map(h=>[h[0],h[3]]),...NEWS]);const pos=Object.fromEntries([...HERO.map(h=>[h[0],h[1]]),...NEWS.map(n=>[n[0],'news'])]);
 console.log('| Vị trí | Trang | Khoá mới | VI 1440 | EN 1440 | VI 390 | EN 390 |\n|---|---|---|---|---|---|---|');
 for(const id of Object.keys(keyOf)){const s=seen[id]||[];const f=(l,w)=>s.some(x=>x==='OK '+l+' '+w)?'thấy':'SAI';console.log(`| ${id} | ${pos[id]} | \`${keyOf[id]}\` | ${f('vi',1440)} | ${f('en',1440)} | ${f('vi',390)} | ${f('en',390)} |`)}
 await b.close();console.log(bad?'FAIL '+bad:'CHECK OK');process.exit(bad?1:0)})();
