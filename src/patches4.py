# Vòng 4: hero gọn, ảnh hero Về chúng tôi, Lịch sử hình thành, ô giá quỹ, chữ Hán Tân Tốc Thực Giản.
# Mỗi mục thêm một hàm vá vào PATCHES4 (dùng rep() để khớp chính xác).
import re
from patches import rep, part


# ---------------------------------------------------------------- css vòng 4 (nạp sau r3.css)
def p_r4css(s):
    css = part('r4.css')
    # file chỉ có comment thì không chèn gì, để build không đổi so với trước khi có khung
    if not re.sub(r'/\*.*?\*/', '', css, flags=re.S).strip():
        return s
    return rep(s, '</helmet>', '<style>' + css + '</style></helmet>')


PATCHES4 = [p_r4css]
