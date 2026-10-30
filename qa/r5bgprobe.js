// Liệt kê phần tử con có nền riêng trong một section (để biết đổi nền section thì chỗ nào chìm): node qa/r5bgprobe.js <file.html> /vi/vnshine "#sec-nav" 1440
const {chromium}=require('playwright');const path=require('path');
const [file,route,sel,W]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:+W||1440,height:900}})).newPage();
await p.goto('file://'+path.resolve(file)+'#'+route);await p.reload();await p.waitForTimeout(1800);
console.log(JSON.stringify(await p.evaluate((sel)=>{const root=document.querySelector(sel);if(!root)return 'không thấy';const out={};
 [root,...root.querySelectorAll('*')].forEach(e=>{const cs=getComputedStyle(e);const r=e.getBoundingClientRect();if(r.width<20||r.height<10)return;
  const bg=cs.backgroundColor;if(/rgba\(0, 0, 0, 0\)/.test(bg)&&!cs.backgroundImage.includes('gradient'))return;
  const k=(e.tagName.toLowerCase()+(e.className?'.'+[...e.classList].slice(0,2).join('.'):''))+' '+bg+(cs.backgroundImage.includes('gradient')?' +gradient':'')+' border:'+cs.borderTopColor.replace(/\s/g,'')+'/'+cs.borderTopWidth;
  out[k]=(out[k]||0)+1});return out},sel),null,1));await b.close()})();
