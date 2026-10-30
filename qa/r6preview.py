"""Dựng qa/review/r6-01/xem-truoc.html (gốc | trước | sau, ảnh JPG nhúng base64): python3 qa/r6preview.py
Gốc = build 3131e7e, trước = main (sau vòng 5), sau = nhánh r6/r6-01. Ảnh do qa/r6review.py tạo."""
import base64, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'review', 'r6-01')

def b64(n):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(D, n), 'rb').read()).decode()

PAGES = [
    ('Về chúng tôi', 've-chung-toi', 'Sau: hero cao 775px như bản gốc (trước 563px), chữ, khoảng cách và Lịch sử hình thành về khung thẻ gốc (3 thẻ trắng cao bằng nhau trên nền mist). Giữ màu A: hero chéo teal, ảnh trong khung bo góc, thanh mục con mist, chữ Hán 新 速 實 簡. Khung ảnh bo góc là khác biệt có chủ ý so với gốc (ảnh tràn nền). 390: khung ảnh dưới chữ cao 420px như gốc.'),
    ('PHVSF', 'phvsf', 'Sau: hero 775px, hàng nút và thẻ giá về vị trí gốc, thẻ giá không còn lưới cột đều (hàng chỉ số gốc). Giữ màu A và ảnh mới. 390: dải teal chính nằm sau thẻ giá (phần tử tuyệt đối), hero cao 996px như gốc (trước 1014px).'),
    ('VNSHINE', 'vnshine', 'Sau: hero 775px, hàng Giá đóng cửa / NAV / Ngày là hàng flex gốc. Ô chênh lệch giá/NAV màu A. Cột 3 tháng giữ như gốc (ô trống hiện "—").'),
    ('Quỹ thành viên', 'quy-thanh-vien', 'Sau: hero 795px, ảnh khung 4:5 như gốc (trước 10/9), đoạn mô tả không bị hẹp lại. Giữ mảng chéo màu A.'),
    ('Học viện', 'hoc-vien', 'Sau: hero 775px ở 1440; layout hẹp (ảnh dưới chữ) từ dưới 1400px như gốc (trước từ dưới 1280px). Giữ màu A.'),
    ('Hướng dẫn PHVSF', 'huong-dan-phvsf', 'Sau: hero 345px như gốc (trước 401px, tiêu đề hai dòng). Tiêu đề một dòng nên lớp mờ trắng kéo dài hơn để chữ tối trên ảnh mới đạt tương phản chữ lớn (>= 3:1).'),
]
h = ['<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>R6-01 · Bố cục trang con về bản gốc, màu A</title>',
     '<style>body{font:15px/1.55 Inter,system-ui,sans-serif;color:#16262B;margin:0;background:#fff}main{max-width:1500px;margin:0 auto;padding:24px}h1{font-size:28px;margin:0 0 6px;color:#0A3440}h2{font-size:21px;margin:40px 0 6px;color:#0A3440;border-top:3px solid #E9C46A;padding-top:14px}',
     'p.n{margin:0 0 12px;color:#4D6066;max-width:980px}.g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;align-items:start}.g.m{grid-template-columns:repeat(3,minmax(0,300px));justify-content:start;margin-top:14px}.g figure{margin:0}',
     'figcaption{font-weight:600;font-size:13px;letter-spacing:.06em;text-transform:uppercase;margin:0 0 6px;color:#4D6066}.a figcaption{color:#0B6274}img{width:100%;height:auto;border:1px solid #D8E7EA;border-radius:8px;display:block}',
     '@media(max-width:900px){.g,.g.m{grid-template-columns:1fr}}</style><main>',
     '<h1>R6-01 · Bố cục trang con về bản gốc, màu A</h1><p class="n">Ba cột: <b>Gốc</b> là build 3131e7e (bố cục chuẩn, màu cũ), <b>Trước</b> là main (vòng 4 + vòng 5), <b>Sau</b> là nhánh r6/r6-01. Màn hình đầu của mỗi trang ở 1440 và 390, bản VI. Trang chủ và chân trang không đổi (0 điểm ảnh khác).</p>']
for t, k, note in PAGES:
    h.append('<h2>%s</h2><p class="n">%s</p>' % (t, note))
    for W in (1440, 390):
        cls = 'g' if W == 1440 else 'g m'
        h.append('<div class="%s"><figure><figcaption>Gốc · %d</figcaption><img src="%s" alt=""></figure><figure><figcaption>Trước · %d</figcaption><img src="%s" alt=""></figure><figure class="a"><figcaption>Sau · %d</figcaption><img src="%s" alt=""></figure></div>'
                 % (cls, W, b64('%s-goc-%d.jpg' % (k, W)), W, b64('%s-truoc-%d.jpg' % (k, W)), W, b64('%s-sau-%d.jpg' % (k, W))))
h.append('</main></html>')
out = os.path.join(D, 'xem-truoc.html')
open(out, 'w', encoding='utf-8').write('\n'.join(h))
print(out, round(os.path.getsize(out) / 1024 / 1024, 2), 'MB')
