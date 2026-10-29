// Liệt kê mọi dòng chữ VI/EN trong PHFM_DATA (dữ liệu cho bảng 'Nội dung website PHFM').
// Chạy: node tools/content_flat.js dist/phfm-website.html  -> build/content.json
const fs=require('fs');const path=require('path');
const mid=fs.readFileSync(process.argv[2]||path.join(__dirname,'..','dist','phfm-website.html'),'utf8');const i=mid.indexOf('window.PHFM_B=b;');const st=mid.lastIndexOf('<script>',i)+8;const code=mid.slice(st,mid.indexOf('</script>',i));
global.window={__I:new Proxy({},{get:(t,k)=>'@img:'+String(k)})};global.document={};eval(code);
const D=window.PHFM_DATA;const out=[];
function walk(o,p){if(o==null)return;if(typeof o==='string'){if(o.length>1&&!/^@img:|^data:|^https?:|^#|^\d[\d.,\/ -]*$/.test(o))out.push({p,vi:o});return}
 if(typeof o!=='object')return;if(o.__b){out.push({p,vi:o.vi,en:o.en});return}
 if(Array.isArray(o)){o.forEach((x,j)=>walk(x,p+'.'+j));return}
 for(const k of Object.keys(o)){if(/^(img|heroImg|src|icon|ic|href|url|dm|logo|code|c|v|seed|vol)$/.test(k))continue;walk(o[k],p?p+'.'+k:k)}}
walk(D,'');
console.log(out.length, JSON.stringify(out).length);
const tops={};out.forEach(e=>{const t=e.p.split('.')[0];tops[t]=(tops[t]||0)+1});console.log(tops);
fs.mkdirSync(path.join(__dirname,'..','build'),{recursive:true});fs.writeFileSync(path.join(__dirname,'..','build','content.json'),JSON.stringify(out));
