"""Cắt ảnh trước/sau/gốc cho qa/review/r6-01 từ thư mục ảnh chụp của qa/r5shots.js.
python3 qa/r6review.py <thư_mục_gốc_chứa_ref_main_pr> : đọc <thư mục>/{ref,main,pr}/<trang>.vi.<rộng>.full.png
Ra qa/review/r6-01/<trang>-{goc,truoc,sau}-<rộng>.jpg (<= 300 KB). goc = 3131e7e, truoc = main, sau = PR."""
import os, sys
from PIL import Image
S = sys.argv[1].rstrip('/') + '/'
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'review', 'r6-01') + '/'
os.makedirs(O, exist_ok=True)
pages = {'about': 've-chung-toi', 'phvsf': 'phvsf', 'vnshine': 'vnshine', 'member': 'quy-thanh-vien', 'academy': 'hoc-vien', 'guidePhvsf': 'huong-dan-phvsf'}
H = {1440: 1500, 390: 1700}
tot = 0
for pg, name in pages.items():
    for W in (1440, 390):
        for b, lab in (('ref', 'goc'), ('main', 'truoc'), ('pr', 'sau')):
            im = Image.open('%s%s/%s.vi.%d.full.png' % (S, b, pg, W)).convert('RGB')
            im = im.crop((0, 0, W, min(H[W], im.height)))
            if W == 1440:
                im = im.resize((960, round(im.height * 960 / 1440)), Image.LANCZOS)
            f = '%s%s-%s-%d.jpg' % (O, name, lab, W)
            for q in (80, 72, 64, 56, 48):
                im.save(f, quality=q, optimize=True)
                if os.path.getsize(f) <= 290 * 1024: break
            tot += os.path.getsize(f)
            if os.path.getsize(f) > 300 * 1024: print('QUÁ LỚN', f)
print('tổng', tot // 1024, 'KB')
