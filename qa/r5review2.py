"""Tạo ảnh trước/sau vòng 5 (sửa vòng 1) trong qa/review/r5-color-a từ qa/out/rb (main) và qa/out/ra (nhánh). JPG, <= 300 KB."""
import os
from PIL import Image
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'review', 'r5-color-a')


def save(im, name, maxw=None):
    if maxw and im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im = im.convert('RGB')
    q = 84
    p = os.path.join(D, name)
    while True:
        im.save(p, 'JPEG', quality=q, optimize=True)
        if os.path.getsize(p) <= 300 * 1024 or q <= 40:
            break
        q -= 6
    print(name, im.size, os.path.getsize(p) // 1024, 'KB')


def top(src, page, w):
    return Image.open(os.path.join(O, src, '%s.vi.%d.top.png' % (page, w)))


PAGES = {'tuyen-dung': 'careers', 'quy-thanh-vien': 'member', 'phvsf': 'phvsf', 'vnshine': 'vnshine'}
for k, pg in PAGES.items():
    for w in (1440, 1024, 390):
        for t, src in (('truoc', 'rb'), ('sau', 'ra')):
            save(top(src, pg, w), '%s-%s-%d.jpg' % (k, t, w), 1200 if w == 1440 else None)
for t, src in (('truoc', 'rb'), ('sau', 'ra')):
    save(top(src, 'vnshine', 768), 'vnshine-%s-768.jpg' % t)


def stack(a, b, gap=24):
    ia, ib = Image.open(a), Image.open(b)
    im = Image.new('RGB', (max(ia.width, ib.width), ia.height + ib.height + gap), (255, 255, 255))
    im.paste(ia, (0, 0))
    im.paste(ib, (0, ia.height + gap))
    return im


for t in ('truoc', 'sau'):
    n = 'before' if t == 'truoc' else 'after'
    save(stack(os.path.join(O, 'guide-vns-%s.png' % n), os.path.join(O, 'guide-phvsf-%s.png' % n)), 'huong-dan-so-buoc-%s.jpg' % t)
a, b = Image.open(os.path.join(O, 'lichsu-before.png')), Image.open(os.path.join(O, 'lichsu-after.png'))
im = Image.new('RGB', (a.width + b.width + 24, max(a.height, b.height)), (255, 255, 255))
im.paste(a, (0, 0))
im.paste(b, (a.width + 24, 0))
save(im, 'lich-su-truoc-sau-390.jpg')
