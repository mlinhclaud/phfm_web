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


# ---------------------------------------------------------------- R4-01: thu chiều cao hero các trang con
MH = 'min-height:min(900px, calc(100vh - var(--hdr-h, 121px)));'

def p_r4_01(s):
    """Bỏ min-height:min(900px, ...) ở hero trang con. Gắn class dùng chung:
    .hero-sub = section hero, .hero-in = khung nội dung bên trong, .hero-pic = ảnh minh hoạ trong hero.
    Chiều cao và padding viết một chỗ ở r4.css (khối R4-01), hero mới (R4-09...) chỉ cần thêm class."""
    # section hero
    s = rep(s, '<section id="ab-overview" style="' + MH, '<section id="ab-overview" class="hero-sub" style="')
    s = rep(s, '<section class="fh" style="' + MH, '<section class="fh hero-sub" style="')
    s = rep(s, '<section class="dh" style="' + MH, '<section class="dh hero-sub" style="', 3)
    # khung nội dung bên trong
    s = rep(s, '<div style="position:relative;max-width:1280px;margin:0 auto;padding:56px 48px 72px;display:grid;grid-template-columns:{{ f.heroCols2 }}',
               '<div class="hero-in" style="position:relative;max-width:1280px;margin:0 auto;padding:56px 48px 72px;display:grid;grid-template-columns:{{ f.heroCols2 }}')
    s = rep(s, '<div style="position:relative;max-width:1280px;margin:0 auto;padding:40px 48px 96px">',
               '<div class="hero-in" style="position:relative;max-width:1280px;margin:0 auto;padding:40px 48px 96px">')
    s = rep(s, '<div style="position:relative;width:100%;max-width:1280px;margin:0 auto;padding:40px 48px 64px;box-sizing:border-box">',
               '<div class="hero-in" style="position:relative;width:100%;max-width:1280px;margin:0 auto;padding:40px 48px 64px;box-sizing:border-box">', 2)
    s = rep(s, '<sc-if value="{{ heroNarrow }}">\n        <div style="max-width:1280px;margin:0 auto;padding:40px 48px 56px">',
               '<sc-if value="{{ heroNarrow }}">\n        <div class="hero-in hero-nar" style="max-width:1280px;margin:0 auto;padding:40px 48px 56px">')
    s = rep(s, 'background:var(--ivory)">\n        <div style="max-width:1280px;margin:0 auto;padding:40px 48px 96px">',
               'background:var(--ivory)">\n        <div class="hero-in" style="max-width:1280px;margin:0 auto;padding:40px 48px 96px">')
    # ảnh trang dịch vụ (member, portfolio, advisory): tỉ lệ 4/5 làm hero cao 800px, đổi sang ngang hơn
    s = rep(s, '<img src="{{ svc.img }}" alt="" style="display:block;width:100%;aspect-ratio:4/5;',
               '<img class="hero-pic" data-svc="{{ svc.k }}" src="{{ svc.img }}" alt="" style="display:block;width:100%;aspect-ratio:4/5;')
    # khoá trang dịch vụ (member, portfolio, advisory) để chỉnh khung cắt riêng từng ảnh
    s = rep(s, 'return { ...s, others: products.slice(2)', 'return { ...s, k: p, others: products.slice(2)')
    # Học viện, layout hẹp: khung nội dung chưa có class
    s = rep(s, '<div style="width:100%;max-width:1280px;margin:0 auto;padding:40px 48px 56px;box-sizing:border-box">',
               '<div class="hero-in hero-nar" style="width:100%;max-width:1280px;margin:0 auto;padding:40px 48px 56px;box-sizing:border-box">')
    # about, mobile: khối ảnh dưới chữ cao 420px, gắn class để thu ở r4.css
    s = rep(s, '<div style="position:relative;height:420px;overflow:hidden">',
               '<div class="hero-pic-box" style="position:relative;height:420px;overflow:hidden">')
    return s


PATCHES4 = [p_r4_01, p_r4_05, p_r4css]
