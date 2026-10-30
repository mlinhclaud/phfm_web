# Vòng 4: hero gọn, ảnh hero Về chúng tôi, Lịch sử hình thành, ô giá quỹ, chữ Hán Tân Tốc Thực Giản.
# Mỗi mục thêm một hàm vá vào PATCHES4 (dùng rep() để khớp chính xác).
import re, os, base64
from patches import rep, part, FD


# ---------------------------------------------------------------- css vòng 4 (nạp sau r3.css)
def p_r4css(s):
    css = part('r4.css')
    if '@@HAN600@@' in css:  # R4-05: font Noto Serif TC subset (新 速 實 簡), nhúng base64 như Inter
        data = base64.b64encode(open(os.path.join(FD, 'noto-serif-tc-600-subset.woff2'), 'rb').read()).decode()
        css = css.replace('@@HAN600@@', 'data:font/woff2;base64,' + data)
    # file chỉ có comment thì không chèn gì, để build không đổi so với trước khi có khung
    if not re.sub(r'/\*.*?\*/', '', css, flags=re.S).strip():
        return s
    return rep(s, '</helmet>', '<style>' + css + '</style></helmet>')


# ---------------------------------------------------------------- R4-05: chữ Hán ở Giá trị cốt lõi
def p_r4_05(s):
    """Hiện d.about.values[].c (新 速 實 簡) trên tên giá trị. CSS .ab-han ở r4.css."""
    return rep(s, """<div style="padding:36px 28px;border-right:1px solid var(--sand);border-bottom:1px solid var(--sand);background:var(--white)">
              <div style="font-size:20px;font-weight:700;color:var(--espresso)">{{ v.n }}</div>""",
               """<div style="padding:36px 28px;border-right:1px solid var(--sand);border-bottom:1px solid var(--sand);background:var(--white)">
              <div class="ab-han" lang="zh-Hant" aria-hidden="true">{{ v.c }}</div>
              <div style="font-size:20px;font-weight:700;color:var(--espresso)">{{ v.n }}</div>""")


PATCHES4 = [p_r4_05, p_r4css]
