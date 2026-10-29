"""Nén một ảnh gốc thành WebP cho web và ghi nguồn vào specs/image-sources.json.

Cách dùng:
  python3 tools/add_image.py <ảnh gốc> <khoá> <rộng tối đa> [--crop x0,y0,x1,y1] [--q 84]
Ví dụ:
  python3 tools/add_image.py assets/source/generated/about_hero.png ab_hero 1920
Quy ước: hero/dải ngang 1920px, thẻ/ảnh bài 960px (khoảng 2x khung hiển thị lớn nhất).
"""
import sys, os, json, argparse
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('key'); ap.add_argument('maxw', type=int)
ap.add_argument('--crop'); ap.add_argument('--q', type=int, default=84)
a = ap.parse_args()
im = Image.open(a.src)
im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB')
crop = [float(x) for x in a.crop.split(',')] if a.crop else None
if crop:
    W, H = im.size; im = im.crop((int(crop[0]*W), int(crop[1]*H), int(crop[2]*W), int(crop[3]*H)))
if im.width > a.maxw:
    im = im.resize((a.maxw, round(im.height * a.maxw / im.width)), Image.LANCZOS)
for f in os.listdir(os.path.join(ROOT, 'assets', 'img')):
    if f.rsplit('.', 1)[0] == a.key: os.remove(os.path.join(ROOT, 'assets', 'img', f))
out = os.path.join(ROOT, 'assets', 'img', a.key + '.webp')
im.save(out, 'WEBP', quality=a.q, method=6)
p = os.path.join(ROOT, 'specs', 'image-sources.json')
m = json.load(open(p)) if os.path.exists(p) else {}
m[a.key] = {'source': os.path.relpath(a.src, os.path.join(ROOT, 'assets', 'source')), 'maxw': a.maxw, 'crop': crop}
json.dump(m, open(p, 'w'), ensure_ascii=False, indent=1)
print('OK', out, os.path.getsize(out) // 1024, 'KB')
