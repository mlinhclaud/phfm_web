# Vòng 6 (nhóm R6-02, R6-03): sửa link neo và khối Biểu mẫu ở các trang Hướng dẫn. Mỗi mục là một hàm vá trong PATCHES6B.
from patches import rep, part


def p_r6_02_anchor(s):
    """R6-02 (#34, #84): hai thẻ phương thức ở Hướng dẫn VNSHINE bản EN và 中文 còn href="#so-cap"/"#thu-cap",
    bấm vào làm hash đổi sang "#so-cap" nên mất route (#/en/guideVnshine) và về trang chủ.
    Bản VI không có href, chỉ có onClick cuộn mượt (gv.goPrimary / gv.goSecondary).
    Đổi sang href="#" như các link còn lại: site.js đã chặn href="#" (preventDefault), onClick vẫn chạy,
    giữ được focus bàn phím. Thêm cursor:pointer như bản VI."""
    for sec, fn in (('so-cap', 'goPrimary'), ('thu-cap', 'goSecondary')):
        s = rep(s, '<a href="#%s" onClick="{{ gv.%s }}" style="text-decoration:none;' % (sec, fn),
                   '<a href="#" onClick="{{ gv.%s }}" style="cursor:pointer;text-decoration:none;' % fn, 2)
    return s


PATCHES6B = [p_r6_02_anchor]
