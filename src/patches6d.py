# Vòng 6, sửa nhỏ sau review (issue #47). Tách file riêng để không đụng danh sách PATCHES6C của R6-05 và ảnh hero.
from patches import rep, part

PXCARD = ('<div style="background:rgba(255,255,255,.94);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);'
          'border:1px solid var(--sand);border-radius:16px;padding:28px 28px 24px">')


def p_fix47_pxcard(s):
    """#47: số % đỏ/xanh trong thẻ giá ở hero PHVSF và VNSHINE chỉ đạt 3,8–4,5:1 vì thẻ trắng 94% nằm trên ảnh.
    Rin chọn: chỉ đậm màu ở thẻ giá. Gắn class r6-pxcard cho thẻ (một chỗ trong template trang quỹ, dùng chung
    cho PHVSF và VNSHINE) và đặt lại hai biến màu trong phạm vi thẻ: đỏ #B4472E, xanh #0F7468 (≥ 4,7:1 kể cả khi
    ảnh dưới thẻ tối nhất). Màu tăng/giảm ở các chỗ khác giữ nguyên."""
    s = rep(s, PXCARD, PXCARD.replace('<div style=', '<div class="r6-pxcard" style=', 1))
    return rep(s, '</helmet>', '<style>' + part('r6d.css') + '</style></helmet>')


PATCHES6D = [p_fix47_pxcard]
