"""Dựng qa/review/r5-color-a/xem-truoc.html (trước | sau, ảnh JPG nhúng base64): python3 qa/r5preview.py
Đọc các ảnh trong qa/review/r5-color-a (do qa/out/mkreview.py hoặc chụp tay tạo)."""
import base64, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'review', 'r5-color-a')

def b64(n):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(D, n), 'rb').read()).decode()

PAGES = [
    ('Về chúng tôi', 've-chung-toi', 'Hero chéo teal đậm và teal chính, ảnh trong khung bo góc. Thanh mục con mist, chữ teal. Lịch sử hình thành nền mist, chữ nhỏ lại. Xen kẽ nền: Trụ sở mist, Ban lãnh đạo trắng, Đối tác mist.'),
    ('PHVSF', 'phvsf', 'Hero chéo, ảnh cắt theo cạnh chéo và mờ 60%. Thanh mục con mist. Khối "Quỹ phù hợp" nền mist. Lịch sử NAV đổi sang mist để không liền với Kết quả (trắng); Ban điều hành trắng.'),
    ('VNSHINE', 'vnshine', 'Hero chéo. Ô chênh lệch giá/NAV teal chính. Nền section xen kẽ trắng và mist từ Tổng quan đến Hướng dẫn.'),
    ('Quỹ thành viên', 'quy-thanh-vien', 'Hero chéo, ảnh trong khung bo góc có bóng. Đoạn mô tả căn trái, không còn bị ép chữ.'),
    ('Tuyển dụng', 'tuyen-dung', 'Sửa vòng 1: mảng chéo và vòng vàng nằm gọn trong hero (trước: bám khung trang, phủ header và che thẻ Văn hoá; ở 390 dải teal tràn quá đáy hero). Ảnh vào khung bo 20px có bóng.'),
    ('Học viện', 'hoc-vien', 'Hero chéo. Ba section: trắng, mist, trắng.'),
    ('Hướng dẫn PHVSF', 'huong-dan-phvsf', 'Thanh bước trắng, bước 1 mist, bước 2 trắng, bước 3 mist, bước 4 trắng, khối đại lý mist.'),
]
FULL = [('Về chúng tôi', 've-chung-toi'), ('PHVSF', 'phvsf'), ('VNSHINE', 'vnshine'), ('Hướng dẫn PHVSF', 'huong-dan-phvsf')]
h = ['<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Vòng 5 · Màu trang con, trước và sau</title>',
     '<style>body{font:15px/1.55 Inter,system-ui,sans-serif;color:#16262B;margin:0;background:#fff}main{max-width:1500px;margin:0 auto;padding:24px}h1{font-size:28px;margin:0 0 6px;color:#0A3440}h2{font-size:21px;margin:40px 0 6px;color:#0A3440;border-top:3px solid #E9C46A;padding-top:14px}',
     'p.n{margin:0 0 12px;color:#4D6066;max-width:900px}.g{display:grid;grid-template-columns:1fr 1fr;gap:16px}.g.m{grid-template-columns:repeat(4,minmax(0,1fr))}.g figure{margin:0}',
     'figcaption{font-weight:600;font-size:13px;letter-spacing:.06em;text-transform:uppercase;margin:0 0 6px}.b figcaption{color:#4D6066}.a figcaption{color:#0B6274}img{width:100%;height:auto;border:1px solid #D8E7EA;border-radius:8px;display:block}',
     '.mist{background:#E3EEF0;padding:16px;border-radius:12px}@media(max-width:800px){.g,.g.m{grid-template-columns:1fr}}</style><main>',
     '<h1>Vòng 5 · Màu trang con theo phương án A</h1><p class="n">Trước là bản main, sau là nhánh r5/color-a. Màn hình đầu ở 1440 và 390, VI. Trang chủ và chân trang không đổi (0 điểm ảnh khác).</p>']
for t, k, note in PAGES:
    h.append('<h2>%s</h2><p class="n">%s</p>' % (t, note))
    h.append('<div class="g"><figure class="b"><figcaption>Trước · 1440</figcaption><img src="%s" alt=""></figure><figure class="a"><figcaption>Sau · 1440</figcaption><img src="%s" alt=""></figure></div>' % (b64('%s-truoc-1440.jpg' % k), b64('%s-sau-1440.jpg' % k)))
    h.append('<div class="g m" style="margin-top:14px;grid-template-columns:repeat(4,minmax(0,260px));justify-content:start"><figure class="b"><figcaption>Trước · 390</figcaption><img src="%s" alt=""></figure><figure class="a"><figcaption>Sau · 390</figcaption><img src="%s" alt=""></figure></div>' % (b64('%s-truoc-390.jpg' % k), b64('%s-sau-390.jpg' % k)))
h.append('<h2>Sửa vòng 1: 1024px, hero hai cột giữ mảng chéo và vòng vàng</h2><p class="n">Trước: nền phẳng teal đậm, không mảng chéo, không vòng vàng ở 761-1100px. Sau: giữ phương án A. Trang quỹ xếp dọc: dải teal có ảnh bắt đầu dưới hàng nút, nút không bị cắt, chữ hero trên nền teal đậm phẳng.</p>')
for t, k in [('Quỹ thành viên', 'quy-thanh-vien'), ('Tuyển dụng', 'tuyen-dung'), ('PHVSF', 'phvsf'), ('VNSHINE', 'vnshine')]:
    h.append('<p class="n"><b>%s · 1024</b></p><div class="g" style="grid-template-columns:repeat(2,minmax(0,520px));justify-content:start"><figure class="b"><figcaption>Trước · 1024</figcaption><img src="%s" alt=""></figure><figure class="a"><figcaption>Sau · 1024</figcaption><img src="%s" alt=""></figure></div>' % (t, b64('%s-truoc-1024.jpg' % k), b64('%s-sau-1024.jpg' % k)))
h.append('<p class="n"><b>VNSHINE · 768</b></p><div class="g" style="grid-template-columns:repeat(2,minmax(0,400px));justify-content:start"><figure class="b"><figcaption>Trước · 768</figcaption><img src="%s" alt=""></figure><figure class="a"><figcaption>Sau · 768</figcaption><img src="%s" alt=""></figure></div>' % (b64('vnshine-truoc-768.jpg'), b64('vnshine-sau-768.jpg')))
h.append('<h2>Hướng dẫn đầu tư: số bước vàng đậm</h2><p class="n">Số 01-04 đổi từ #C0962D (2,3:1 trên mist) sang #7D5F1A (5,0:1 trên mist, 6,0:1 trên trắng). Hàng trên VNSHINE, hàng dưới PHVSF.</p><div class="g"><figure class="b"><figcaption>Trước</figcaption><img src="%s" alt=""></figure><figure class="a"><figcaption>Sau</figcaption><img src="%s" alt=""></figure></div>' % (b64('huong-dan-so-buoc-truoc.jpg'), b64('huong-dan-so-buoc-sau.jpg')))
h.append('<h2>Lịch sử hình thành: "2012 - 2013" một dòng (390)</h2><p class="n">Cột năm 96px, không xuống dòng. Trái: trước. Phải: sau.</p><img src="%s" alt="" style="max-width:804px">' % b64('lich-su-truoc-sau-390.jpg'))
h.append('<h2>Thứ tự nền section (toàn trang, 1440)</h2><p class="n">Không còn hai section liền nhau cùng màu nền. Trước: thanh mục con teal đậm liền hero, nhiều cặp trắng-trắng. Sau: trắng và mist xen kẽ.</p>')
for t, k in FULL:
    n = k if k != 've-chung-toi' else 've-chung-toi'
    h.append('<p class="n"><b>%s</b></p><div class="g" style="grid-template-columns:repeat(2,minmax(0,360px));justify-content:start"><figure class="b"><figcaption>Trước</figcaption><img src="%s" alt=""></figure><figure class="a"><figcaption>Sau</figcaption><img src="%s" alt=""></figure></div>' % (t, b64('%s-toan-trang-truoc.jpg' % k), b64('%s-toan-trang-sau.jpg' % k)))
h.append('<h2>Menu header: một gạch vàng mỗi mục</h2><p class="n">Trước: gạch mục đang chọn (vàng đậm, thấp) và gạch hover (vàng sáng, cao hơn) hiện cùng lúc, vòng focus đen sát gạch. Sau: một gạch vàng cùng vị trí; focus là vòng teal cách chữ 4px. Hàng 1: rê chuột vào mục đang chọn. Hàng 2: mở dropdown. Hàng 3: focus bàn phím.</p><img src="%s" alt="">' % b64('menu-2-gach-truoc-sau.jpg'))
h.append('<h2>Chữ không còn bị ép</h2><p class="n">Trước: mô tả hero bị word-spacing âm (tới -1,6px) và căn đều hai lề. Sau: căn trái, khoảng cách chữ mặc định. Hàng 1: VNSHINE. Hàng 2: Về chúng tôi. Hàng 3: Quỹ thành viên.</p><div class="mist" style="background:#0A3440"><img src="%s" alt=""></div>' % b64('chu-dinh-sat-truoc-sau.jpg'))
h.append('</main></html>')
out = os.path.join(D, 'xem-truoc.html')
open(out, 'w', encoding='utf-8').write('\n'.join(h))
print(out, round(os.path.getsize(out) / 1024 / 1024, 2), 'MB')
