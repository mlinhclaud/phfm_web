"""Dựng file so sánh phối màu trang con: python3 qa/r5compare.py
Đọc ảnh trong qa/out/r5cur, r5a, r5b, home-main (do qa/r5shots.js tạo), ghi qa/review/r5-preview/so-sanh-A-B.html (ảnh JPG nhúng base64)."""
import base64, io, os, sys
from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OUT = os.path.join(ROOT, 'qa', 'review', 'r5-preview', 'so-sanh-A-B.html')
D = lambda *p: os.path.join(ROOT, 'qa', 'out', *p)


def lin(v):
    v /= 255
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def lum(h):
    h = h.lstrip('#')
    r, g, b = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def cr(fg, bg):
    a, b = sorted([lum(fg), lum(bg)], reverse=True)
    return (a + 0.05) / (b + 0.05)


def c(fg, bg, note=''):
    v = cr(fg, bg)
    return '<span class="%s">%s trên %s: <b>%.1f : 1</b>%s</span>' % ('ok' if v >= 4.5 else 'lg' if v >= 3 else 'no', fg, bg, v, note)


def jpg(path, w=None, q=72, crop=None):
    im = Image.open(path).convert('RGB')
    if crop:
        im = im.crop(crop)
    if w and im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()


def sw(h):
    return '<i class="sw" style="background:%s"></i>%s' % (h, h)


# ---- bảng màu từng phương án (Khối | Nền | Chữ | Nhấn | Tương phản)
TA = [
    ('Hero (About, VNSHINE, Quỹ thành viên)', sw('#0A3440') + ' trái, mảng chéo ' + sw('#0B6274') + ' phải (skewX -16°, mốc 55% như trang chủ); ảnh trong khung bo 20px hoặc cắt theo mảng chéo (VNSHINE)',
     'Tiêu đề ' + sw('#FFFFFF') + '; mô tả ' + sw('#E3EEF0') + '; đường dẫn ' + sw('#D8E7EA'), 'Nhãn, gạch tiêu đề, vòng tròn ' + sw('#E9C46A'),
     [c('#FFFFFF', '#0A3440'), c('#E3EEF0', '#0A3440'), c('#D8E7EA', '#0A3440'), c('#E9C46A', '#0A3440', ' (nhãn)'), c('#FFFFFF', '#0B6274', ' (chữ chạm mảng chéo)')]),
    ('Nút trong hero', sw('#E9C46A') + ' (nút chính); nút phụ viền trắng', 'Chữ nút chính ' + sw('#16181A') + '; nút phụ ' + sw('#FFFFFF'), 'Hover ' + sw('#F2D27D'),
     [c('#16181A', '#E9C46A'), c('#FFFFFF', '#0A3440')]),
    ('Thẻ giá hero VNSHINE', 'Trắng 94%', 'Chữ ' + sw('#16262B') + '; nhãn ' + sw('#4D6066'), 'Số tăng ' + sw('#15897D'),
     [c('#16262B', '#FFFFFF'), c('#4D6066', '#FFFFFF'), c('#15897D', '#FFFFFF', ' (màu của brief, chưa đủ 4,5; bản hiện tại cũng vậy)')]),
    ('Thanh mục con', sw('#FFFFFF') + ', viền ' + sw('#D8E7EA'), 'Chữ ' + sw('#0B6274') + '; mục đang chọn ' + sw('#0A3440') + ' đậm', 'Gạch chân ' + sw('#E9C46A') + ' 3px (khi chọn, rê, focus)',
     [c('#0B6274', '#FFFFFF'), c('#0A3440', '#FFFFFF')]),
    ('Lịch sử hình thành (About)', sw('#E3EEF0'), 'Tiêu đề, tên giai đoạn ' + sw('#0A3440') + '; năm lớn, năm mốc ' + sw('#0B6274') + '; mô tả ' + sw('#16262B'), 'Trục ngang và chấm mốc ' + sw('#E9C46A'),
     [c('#0A3440', '#E3EEF0'), c('#0B6274', '#E3EEF0'), c('#16262B', '#E3EEF0')]),
    ('Ô chênh lệch giá/NAV (VNSHINE)', sw('#0B6274'), 'Số ' + sw('#FFFFFF') + '; nhãn ' + sw('#D8E7EA'), 'Vạch trên ' + sw('#E9C46A') + ' 3px',
     [c('#FFFFFF', '#0B6274'), c('#D8E7EA', '#0B6274')]),
    ('Nhãn nhỏ viết hoa trên nền sáng', sw('#FFFFFF') + ' hoặc ' + sw('#E3EEF0'), sw('#7D5F1A'), '—', [c('#7D5F1A', '#FFFFFF'), c('#7D5F1A', '#E3EEF0')]),
    ('Quỹ phù hợp với bạn (PHVSF, ngoài 3 trang mẫu)', sw('#E3EEF0'), 'Tiêu đề ' + sw('#0A3440') + '; nội dung ' + sw('#16262B'), 'Dấu tích ' + sw('#0B6274') + ' trên tròn trắng', [c('#0A3440', '#E3EEF0'), c('#16262B', '#E3EEF0')]),
    ('Chữ Hán 新速實簡', 'Nền trắng (giữ nguyên)', sw('#C0962D'), '—', [c('#C0962D', '#FFFFFF', ' (chữ lớn 60px, cần ≥3)')]),
]
TB = [
    ('Hero (About, VNSHINE, Quỹ thành viên)', sw('#E3EEF0') + ', viền dưới ' + sw('#D8E7EA') + '; ảnh bên phải không phủ tối (About, VNSHINE: ảnh tràn, mờ mist ở mép trái; Quỹ thành viên: khung bo 20px)',
     'Tiêu đề ' + sw('#0A3440') + '; mô tả ' + sw('#16262B') + '; đường dẫn ' + sw('#4D6066'), 'Nhãn ' + sw('#7D5F1A') + '; gạch tiêu đề ' + sw('#E9C46A'),
     [c('#0A3440', '#E3EEF0'), c('#16262B', '#E3EEF0'), c('#4D6066', '#E3EEF0'), c('#7D5F1A', '#E3EEF0', ' (nhãn)')]),
    ('Nút trong hero', 'Nút chính ' + sw('#E9C46A') + '; nút phụ viền ' + sw('#0B6274'), 'Chữ nút chính ' + sw('#16181A') + '; nút phụ ' + sw('#0B6274'), 'Hover ' + sw('#F2D27D'),
     [c('#16181A', '#E9C46A'), c('#0B6274', '#E3EEF0')]),
    ('Thẻ giá hero VNSHINE', 'Trắng 94%, viền ' + sw('#D8E7EA'), 'Chữ ' + sw('#16262B') + '; nhãn ' + sw('#4D6066'), 'Số tăng ' + sw('#15897D'),
     [c('#16262B', '#FFFFFF'), c('#4D6066', '#FFFFFF'), c('#15897D', '#FFFFFF', ' (màu của brief, chưa đủ 4,5; bản hiện tại cũng vậy)')]),
    ('Thanh mục con', sw('#FFFFFF') + ', viền ' + sw('#D8E7EA'), 'Chữ ' + sw('#0B6274') + '; mục đang chọn ' + sw('#0A3440') + ' đậm', 'Gạch chân ' + sw('#E9C46A') + ' 3px (khi chọn, rê, focus)',
     [c('#0B6274', '#FFFFFF'), c('#0A3440', '#FFFFFF')]),
    ('Lịch sử hình thành (About) = dải teal đậm duy nhất của About', sw('#0A3440'), 'Tiêu đề ' + sw('#FFFFFF') + '; mô tả ' + sw('#E3EEF0'), 'Năm lớn ' + sw('#E9C46A') + '; trục và chấm mốc ' + sw('#E9C46A'),
     [c('#FFFFFF', '#0A3440'), c('#E3EEF0', '#0A3440'), c('#E9C46A', '#0A3440')]),
    ('Ô chênh lệch giá/NAV (VNSHINE) = dải nhấn duy nhất của VNSHINE', sw('#0A3440'), 'Số ' + sw('#FFFFFF') + '; nhãn ' + sw('#D8E7EA'), 'Vạch trên ' + sw('#E9C46A') + ' 3px',
     [c('#FFFFFF', '#0A3440'), c('#D8E7EA', '#0A3440')]),
    ('Quỹ thành viên: không có dải teal đậm', 'Các khối dưới hero giữ nguyên (mist, trắng)', '—', '—', []),
    ('Nhãn nhỏ viết hoa trên nền sáng', sw('#FFFFFF') + ' hoặc ' + sw('#E3EEF0'), sw('#7D5F1A'), '—', [c('#7D5F1A', '#FFFFFF'), c('#7D5F1A', '#E3EEF0')]),
    ('Quỹ phù hợp với bạn (PHVSF, ngoài 3 trang mẫu)', sw('#E3EEF0'), 'Tiêu đề ' + sw('#0A3440') + '; nội dung ' + sw('#16262B'), 'Dấu tích ' + sw('#0B6274') + ' trên tròn trắng', [c('#0A3440', '#E3EEF0'), c('#16262B', '#E3EEF0')]),
]


def table(rows):
    h = '<table><thead><tr><th>Khối</th><th>Nền</th><th>Chữ</th><th>Nhấn</th><th>Tương phản (WCAG)</th></tr></thead><tbody>'
    for blk, bg, tx, ac, crs in rows:
        h += '<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (blk, bg, tx, ac, '<br>'.join(crs) or '—')
    return h + '</tbody></table>'


PAGES = [('about', 'Về chúng tôi', 'journey', 'Lịch sử hình thành'), ('vnshine', 'VNSHINE ETF', 'trading', 'Thông tin giao dịch'), ('member', 'Quỹ thành viên', None, None)]
NAMES = [('cur', 'Hiện tại (bản chính)'), ('a', 'Phương án A · chéo như trang chủ'), ('b', 'Phương án B · sáng')]


def figs(page, lang, W, kind, crop=None, w=None):
    h = '<div class="g3">'
    for k, nm in NAMES:
        p = D('r5' + k, '%s.%s.%d.%s.png' % (page, lang, W, kind))
        if not os.path.exists(p):
            h += '<figure><figcaption>%s</figcaption><div class="miss">không có ảnh</div></figure>' % nm
            continue
        src = jpg(p, w=w, crop=crop)
        h += '<figure><figcaption>%s</figcaption><img src="%s" alt="%s, %s, %s, %dpx" loading="lazy"></figure>' % (nm, src, page, nm, lang, W)
    return h + '</div>'


css = '''
body{font-family:Inter,system-ui,sans-serif;margin:0;background:#FFFFFF;color:#16262B;line-height:1.5}
.w{max-width:1600px;margin:0 auto;padding:24px}
h1{color:#0A3440;font-size:30px;margin:8px 0}h2{color:#0A3440;font-size:24px;margin:48px 0 8px;border-top:3px solid #E9C46A;padding-top:16px}h3{color:#0B6274;font-size:18px;margin:28px 0 8px}
p,li{font-size:15px;color:#16262B}.mut{color:#4D6066}
.g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;align-items:start}
figure{margin:0;background:#E3EEF0;border-radius:12px;padding:8px}figcaption{font-weight:600;font-size:14px;color:#0A3440;padding:4px 6px 8px}
figure img{width:100%;display:block;border-radius:8px;cursor:zoom-in}.miss{padding:40px;color:#4D6066}
.m390 .g3{grid-template-columns:repeat(3,390px);justify-content:start}.m390 figure img{width:390px}
table{border-collapse:collapse;width:100%;font-size:13px;margin:8px 0 16px}th,td{border:1px solid #D8E7EA;padding:8px 10px;text-align:left;vertical-align:top}th{background:#E3EEF0;color:#0A3440}
.sw{display:inline-block;width:12px;height:12px;border:1px solid #86B4BE;border-radius:3px;margin-right:4px;vertical-align:-1px}
.ok b{color:#0B6274}.lg b{color:#7D5F1A}.no b{color:#7D5F1A;text-decoration:underline}
.tag{display:inline-block;background:#E9C46A;color:#16181A;font-weight:700;font-size:12px;border-radius:999px;padding:2px 10px;margin-right:6px}
details{margin:12px 0}summary{cursor:pointer;font-weight:600;color:#0B6274;font-size:15px}
.home img{max-width:100%;border-radius:8px;border:1px solid #D8E7EA}.hg{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,1fr);gap:16px;align-items:start}
.zoom{position:fixed;inset:0;background:rgba(10,52,64,.92);z-index:9;overflow:auto;display:none;padding:16px}.zoom img{display:block;margin:0 auto;max-width:none;width:auto}.zoom.on{display:block}
@media(max-width:1100px){.g3{grid-template-columns:1fr}.hg{grid-template-columns:1fr}}
'''

h = ['<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PHFM · Xem trước phối màu trang con: A và B</title><style>%s</style></head><body><div class="w">' % css]
h.append('<h1>Xem trước phối màu trang con: A và B</h1>')
h.append('<p class="mut">Ba trang mẫu: Về chúng tôi, VNSHINE, Quỹ thành viên (VI và EN). Mỗi hàng là Hiện tại | A | B. Bấm vào ảnh để xem lớn. Chưa merge, chỉ để chọn.</p>')
h.append('<ul><li><span class="tag">A</span>Chéo như trang chủ: hero chia chéo #0A3440 / #0B6274, ảnh trong khung bo góc, thanh mục con trắng, Lịch sử hình thành nền mist.</li><li><span class="tag">B</span>Sáng: hero nền mist, ảnh bên phải không phủ tối, tiêu đề #0A3440, mỗi trang tối đa một dải teal đậm.</li><li>Ảnh hero chưa đổi. Bản chụp mô phỏng trạng thái "đang chọn" của thanh mục con ở mục đầu (bản chính chưa có chuyển mục theo cuộn).</li></ul>')
h.append('<h2>Trang chủ để so độ khớp màu (không đổi ở cả A và B)</h2><div class="home hg"><div><img src="%s" alt="Trang chủ 1440"></div><div><img src="%s" alt="Trang chủ 390"></div></div>' % (
    jpg(D('home-main', 'home.vi.1440.top.png'), q=74), jpg(D('home-main', 'home.vi.390.top.png'), q=74)))
for pg, title, extra, extra_t in PAGES:
    h.append('<h2>%s</h2>' % title)
    for lang, lt in (('vi', 'Tiếng Việt'), ('en', 'English')):
        h.append('<details %s><summary>%s · 1440 px</summary>%s' % ('open' if lang == 'vi' else '', lt, figs(pg, lang, 1440, 'top', w=1100)))
        if extra:
            h.append('<h3>%s</h3>' % extra_t + figs(pg, lang, 1440, extra, w=1100))
        h.append('</details>')
        h.append('<details class="m390" %s><summary>%s · 390 px</summary>%s</details>' % ('open' if lang == 'vi' else '', lt, figs(pg, lang, 390, 'full', crop=(0, 0, 390, 1250))))
h.append('<h2>Ảnh hero hiện tại có hợp không?</h2><p class="mut">Ảnh giờ xanh (chưa đổi). Đo: Về chúng tôi sáng TB 0,48; Quỹ thành viên 0,40; VNSHINE 0,30 với 47% điểm ảnh tối.</p>'
         '<table><thead><tr><th>Trang</th><th>A</th><th>B</th><th>Ảnh cần tạo lại (Higgsfield, chưa tạo)</th></tr></thead><tbody>'
         '<tr><td><b>Về chúng tôi</b></td><td>Hợp. Trời xanh cùng tông mảng #0B6274.</td><td>Tạm được, giờ xanh sẫm cạnh nền mist hơi nặng.</td><td>B: cùng phòng họp tầng cao, ban ngày, trời xanh nhạt, sông Sài Gòn, bàn trắng; chủ thể ở nửa phải, nửa trái là kính và tường sáng cho chữ. Khung 4:3.</td></tr>'
         '<tr><td><b>VNSHINE</b></td><td>Chưa hợp: thẻ giá che gần hết, còn lại mảng tối và chữ số cam/hồng.</td><td>Không hợp: phòng tối cạnh nền mist, số cam/hồng.</td><td>Cả A và B: ban ngày, chuyên viên trẻ trước màn hình biểu đồ teal (không số đọc được), cửa kính nhìn ra HCMC. 16:9. B: chủ thể ở 55-95% ngang, nửa trái sáng và ít chi tiết. A: chủ thể nửa trên bên phải (thẻ giá che giữa và dưới).</td></tr>'
         '<tr><td><b>Quỹ thành viên</b></td><td>Hợp, giữ được.</td><td>Hơi tối so với nền mist.</td><td>B: phòng họp hội đồng ban ngày, bàn tròn trắng, tài liệu và tablet, thêm 1-2 người trẻ nhìn nghiêng. Khung 4:5, chủ thể giữa (cắt 10:9 và 16:10).</td></tr>'
         '</tbody></table>')
h.append('<h2>Bảng màu phương án A</h2>' + table(TA))
h.append('<h2>Bảng màu phương án B</h2>' + table(TB))
h.append('<p class="mut">Tương phản tính theo WCAG 2.x từ mã màu. Chữ nằm trên ảnh (tiêu đề, mô tả hero) đã đo thêm trên điểm ảnh thật ở 1440 và 390: ở cả A và B mọi chữ đạt (chữ thường ≥4,5, chữ lớn ≥3); chỉ các số tăng #15897D trong thẻ giá chưa tới 4,5 (cũng ở bản hiện tại). Chữ Hán #C0962D trên trắng chỉ 2,7:1 (brief yêu cầu giữ màu này; chữ lớn cần ≥3).</p>')
h.append('</div><div class="zoom" id="z"><img alt=""></div><script>document.addEventListener("click",function(e){var z=document.getElementById("z");if(e.target.tagName==="IMG"&&e.target.closest("figure")){z.querySelector("img").src=e.target.src;z.classList.add("on")}else if(z.classList.contains("on")){z.classList.remove("on")}})</script></body></html>')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
html = '\n'.join(h)
open(OUT, 'w', encoding='utf-8').write(html)
print('OK', OUT, round(len(html.encode('utf-8')) / 1024 / 1024, 2), 'MB')
