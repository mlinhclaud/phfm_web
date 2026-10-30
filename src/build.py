# Build: phương án C + B -> 1 file HTML độc lập (VI/EN), homepage Teal Vanguard, retheme teal, sửa lỗi đã duyệt.
import json, re, sys, os, base64
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from patches import apply_all          # các bản vá template/logic/css
from images import image_table         # bảng ảnh: key -> data URI

src = open(os.path.join(HERE, 'src_o8.html'), encoding='utf-8').read()
s = apply_all(src)

# ảnh: mỗi ảnh chỉ nhúng 1 lần trong window.__I, các chỗ dùng tham chiếu theo khoá
IMG = image_table()
used = sorted(set(re.findall(r'__I\.(\w+)', s)) | set(re.findall(r'img\.(\w+) \}\}', s)))
missing = [k for k in used if k not in IMG]
if missing:
    print('THIEU ANH:', missing); sys.exit(1)
reg = '<script>window.__I={' + ','.join('%s:"%s"' % (k, IMG[k]) for k in used) + '};</script>'
s = s.replace('<!--@@IMGREG@@-->', reg, 1)
left = re.findall(r'@@IMG:\w+@@', s)
if left:
    print('CON SOT @@IMG:', left[:5]); sys.exit(1)

# React UMD nhúng sẵn: không phụ thuộc CDN, mở offline được
VENDOR = os.path.join(HERE, '..', 'vendor', 'react')
react = open(os.path.join(VENDOR, 'react.production.min.js'), encoding='utf-8').read()
rdom = open(os.path.join(VENDOR, 'react-dom.production.min.js'), encoding='utf-8').read()
inline = '<script>' + react.replace('</script', '<\\/script') + '</script>\n<script>' + rdom.replace('</script', '<\\/script') + '</script>\n'
s = s.replace('<script>// GENERATED from dc-runtime', inline + '<script>// GENERATED from dc-runtime', 1)

os.makedirs(os.path.join(HERE, '..', 'dist'), exist_ok=True)
# R5=a|b: bản xem trước phối màu, ghi ra file riêng, không đè bản chính
r5 = os.environ.get('R5', '').strip().lower()
out = os.path.normpath(os.path.join(HERE, '..', 'dist', 'phfm-website-r5%s.html' % r5 if r5 in ('a', 'b') else 'phfm-website.html'))
open(out, 'w', encoding='utf-8').write(s)
print('OK', out, round(len(s.encode('utf-8')) / 1024 / 1024, 2), 'MB')
