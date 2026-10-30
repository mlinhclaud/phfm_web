# Vòng 6: R6-01 trả bố cục trang con về bản gốc (build 3131e7e), giữ màu A của vòng 5.
# Cách làm: gỡ trực tiếp các thay đổi hình học trong patches4.py, r4.css, r5.css (xem specs/changelog.md, mục Vòng 6);
# phần còn lại (khung ảnh, dải teal xếp dọc) viết ở r6.css, nạp sau r5.css. Mỗi mục sau thêm một hàm vá vào PATCHES6.
from patches import rep, part


def p_r6css(s):
    return rep(s, '</helmet>', '<style>' + part('r6.css') + '</style></helmet>')


PATCHES6 = [p_r6css]
