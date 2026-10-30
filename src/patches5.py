# Vòng 5: phối màu trang con theo phương án A "chéo như trang chủ" (Rin chọn). Mỗi mục là một hàm vá trong PATCHES5.
from patches import rep, part


def p_r5_markup(s):
    """Thêm class móc cho r5.css (không đổi nội dung):
    .r5-aw = khung ảnh hero rộng của About và Học viện (div tuyệt đối bên phải) ; .r5-aw-ov = lớp gradient trong khung;
    .r5-picw = khung bọc ảnh hero ba trang dịch vụ (Quỹ thành viên, Quản lý danh mục, Tư vấn)."""
    s = rep(s, '<div style="position:absolute;top:0;bottom:0;right:0;width:72vw;overflow:hidden">',
               '<div class="r5-aw" style="position:absolute;top:0;bottom:0;right:0;width:72vw;overflow:hidden">', 2)
    s = rep(s, '<div style="position:absolute;top:0;bottom:0;left:-2px;width:50%;background:linear-gradient(90deg, #0A3440 0%, #0A3440 36%, rgba(10,52,64,0) 100%)"></div>',
               '<div class="r5-aw-ov" style="position:absolute;top:0;bottom:0;left:-2px;width:50%;background:linear-gradient(90deg, #0A3440 0%, #0A3440 36%, rgba(10,52,64,0) 100%)"></div>', 2)
    s = rep(s, '<img class="hero-pic" data-svc="{{ svc.k }}" src="{{ svc.img }}" alt="" style="display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:2px;background:var(--cream)">',
               '<div class="r5-picw"><img class="hero-pic" data-svc="{{ svc.k }}" src="{{ svc.img }}" alt="" style="display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:2px;background:var(--cream)"></div>')
    return s


def p_r5_menu(s):
    """Gạch "mục đang chọn" của menu header (7 mục) gắn class th-act để r5.css ẩn gạch hover trên cùng mục và đặt cùng vị trí/màu."""
    return rep(s, '<div style="position:absolute;left:0;right:0;bottom:-1px;height:2px;background:var(--gold)"></div></sc-if>',
                  '<div class="th-act" style="position:absolute;left:0;right:0;bottom:-1px;height:2px;background:var(--gold)"></div></sc-if>', 7)


def p_r5_nofit(s):
    """Tắt script căn đều (okBlock/fit) trên mọi nội dung trong <main> và bài đọc #rd5: không còn word-spacing/letter-spacing âm.
    Trang chủ và chân trang đã bị loại trừ từ trước."""
    return rep(s, "function okBlock(el){if(el.closest('[data-hm],.ft'))return false;", "function okBlock(el){if(el.closest('[data-hm],.ft,main,#rd5'))return false;")


def p_r5_pages(s):
    """Gắn class theo trang vào <main> (nhãn data-screen-label đổi theo ngôn ngữ nên không dùng làm móc CSS) để r5.css xen kẽ nền section."""
    for label, cls in [('Công bố thông tin', 'pg-ir'), ('Tin tức & Góc nhìn', 'pg-news'), ('Kiến thức Đầu tư', 'pg-academy'),
                       ('Thuật ngữ đầu tư', 'pg-glossary'), ('Câu hỏi thường gặp', 'pg-faq')]:
        s = rep(s, '<main data-screen-label="%s">' % label, '<main class="%s" data-screen-label="%s">' % (cls, label))
    return s


def p_r5css(s):
    return rep(s, '</helmet>', '<style>' + part('r5.css') + '</style></helmet>')


PATCHES5 = [p_r5_markup, p_r5_menu, p_r5_nofit, p_r5_pages, p_r5css]
