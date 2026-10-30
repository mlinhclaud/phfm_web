# Vòng 5: xem trước hai phương án phối màu trang con (chưa merge vào bản chính).
# Chỉ chạy khi có biến môi trường R5=a hoặc R5=b:  R5=a python3 src/build.py  ->  dist/phfm-website-r5a.html
# Không có biến R5 thì PATCHES5 rỗng và bản build mặc định không đổi một byte.
import os
from patches import rep, part

R5 = os.environ.get('R5', '').strip().lower()


def p_r5_markup(s):
    """Thêm class móc cho CSS r5a/r5b (không đổi nội dung):
    .r5-aw = khung ảnh hero rộng của About và Học viện (div tuyệt đối bên phải) ; .r5-aw-ov = lớp gradient trong khung;
    .r5-picw = khung bọc ảnh hero ba trang dịch vụ (Quỹ thành viên, Quản lý danh mục, Tư vấn)."""
    s = rep(s, '<div style="position:absolute;top:0;bottom:0;right:0;width:72vw;overflow:hidden">',
               '<div class="r5-aw" style="position:absolute;top:0;bottom:0;right:0;width:72vw;overflow:hidden">', 2)
    s = rep(s, '<div style="position:absolute;top:0;bottom:0;left:-2px;width:50%;background:linear-gradient(90deg, #0A3440 0%, #0A3440 36%, rgba(10,52,64,0) 100%)"></div>',
               '<div class="r5-aw-ov" style="position:absolute;top:0;bottom:0;left:-2px;width:50%;background:linear-gradient(90deg, #0A3440 0%, #0A3440 36%, rgba(10,52,64,0) 100%)"></div>', 2)
    s = rep(s, '<img class="hero-pic" data-svc="{{ svc.k }}" src="{{ svc.img }}" alt="" style="display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:2px;background:var(--cream)">',
               '<div class="r5-picw"><img class="hero-pic" data-svc="{{ svc.k }}" src="{{ svc.img }}" alt="" style="display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:2px;background:var(--cream)"></div>')
    return s


def p_r5css(s):
    css = part('r5%s.css' % R5)
    return rep(s, '</helmet>', '<style>' + css + '</style></helmet>')


PATCHES5 = [p_r5_markup, p_r5css] if R5 in ('a', 'b') else []
