"""So từng điểm ảnh các ảnh chụp giữa hai thư mục: python3 qa/r5pixdiff.py <thu_muc_goc> <thu_muc_so> [hậu tố, mặc định .full.png]
In số điểm ảnh khác nhau của từng ảnh. Khác 0 -> thoát mã 1."""
import sys, os
from PIL import Image, ImageChops
a, b = sys.argv[1], sys.argv[2]
suf = sys.argv[3] if len(sys.argv) > 3 else '.full.png'
bad = 0
for n in sorted(os.listdir(a)):
    if not n.endswith(suf) or not os.path.exists(os.path.join(b, n)):
        continue
    x = Image.open(os.path.join(a, n)).convert('RGB'); y = Image.open(os.path.join(b, n)).convert('RGB')
    if x.size != y.size:
        print('KHÁC KÍCH THƯỚC', n, x.size, y.size); bad += 1; continue
    d = ImageChops.difference(x, y); bb = d.getbbox()
    cnt = sum(1 for p in d.convert('L').getdata() if p) if bb else 0
    print('%-28s %dx%d  điểm ảnh khác: %d' % (n, x.size[0], x.size[1], cnt), '' if not bb else 'bbox=%s' % (bb,))
    bad += 1 if cnt else 0
print('GIỐNG HỆT' if not bad else 'CÓ KHÁC BIỆT %d' % bad)
sys.exit(1 if bad else 0)
