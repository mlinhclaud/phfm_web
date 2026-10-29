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


# ---------------------------------------------------------------- R4-09: bộ ảnh stock mới (plans/stock-r5.md)
def p_r4_09(s):
    """Thay ảnh theo TỪNG VỊ TRÍ (H1-H10, N1-N10), không đổi hàng loạt theo khoá cũ.
    Chạy sau p_imgmap/p_r3img/p_images nên chuỗi khớp là dạng cuối: window.__I.<khoá> hoặc {{ img.<khoá> }}.
    Giữ nguyên: thẻ Học viện (pk_I03, vn_city) và nền CTA hai trang Hướng dẫn (ctaImg), vì không khớp chuỗi nào dưới đây."""
    # H1 Về chúng tôi: hero chuyển sang kiểu .dh (nền teal đậm #0A3440, chữ trắng), ảnh bên phải, bỏ gradient trắng
    s = rep(s, '<section id="ab-overview" class="hero-sub" style="', '<section id="ab-overview" class="dh hero-sub" style="')
    # lớp mờ teal rộng hơn hero Học viện (ảnh About sáng hơn): chữ trắng đè lên ảnh vẫn >= 4.5:1
    s = rep(s, '<img src="{{ img.ab_hero }}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:72% 35%;display:block">\n          <div style="position:absolute;top:0;bottom:0;left:-2px;width:34%;background:linear-gradient(90deg, var(--ivory) 0%, var(--ivory) 12%, rgba(255,255,255,0) 100%)"></div>',
               '<img src="{{ img.r5_about_hero }}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:70% 50%;display:block">\n          <div style="position:absolute;top:0;bottom:0;left:-2px;width:50%;background:linear-gradient(90deg, #0A3440 0%, #0A3440 36%, rgba(10,52,64,0) 100%)"></div>')
    s = rep(s, '<img src="{{ img.ab_hero }}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:65% 40%;display:block">',
               '<img src="{{ img.r5_about_hero }}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:75% 50%;display:block">')
    # H2, H3 hero trang quỹ (dữ liệu funds)
    s = rep(s, 'heroImg:window.__I.pk_I03,', 'heroImg:window.__I.r5_phvsf_hero,')
    s = rep(s, 'heroImg:window.__I.r3_vns_hero,price', 'heroImg:window.__I.r5_vns_hero,price')
    # H4, H5, H6 ảnh hero trang dịch vụ (dữ liệu services)
    s = rep(s, 'member:{img:window.__I.advisor,', 'member:{img:window.__I.r5_member_hero,')
    s = rep(s, 'portfolio:{img:window.__I.pk_I05,', 'portfolio:{img:window.__I.r5_pf_hero,')
    s = rep(s, 'advisory:{img:window.__I.r3_adv_hero,', 'advisory:{img:window.__I.r5_adv_hero,')
    # H7 Học viện (hai bản: layout rộng và hẹp). Thẻ Học viện dùng pk_I03/vn_city ở dữ liệu guide, không đụng tới
    # ảnh Học viện sáng hơn ảnh cũ: lớp mờ teal rộng như hero About để chữ trắng >= 4.5:1
    s = rep(s, '<img src="{{ img.pk_I07 }}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 40%;display:block">\n          <div style="position:absolute;top:0;bottom:0;left:-2px;width:34%;background:linear-gradient(90deg, var(--ivory) 0%, var(--ivory) 12%, rgba(255,255,255,0) 100%)"></div>',
               '<img src="{{ img.r5_acad_hero }}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 50%;display:block">\n          <div style="position:absolute;top:0;bottom:0;left:-2px;width:50%;background:linear-gradient(90deg, #0A3440 0%, #0A3440 36%, rgba(10,52,64,0) 100%)"></div>')
    s = rep(s, '<img src="{{ img.pk_I07 }}" alt="" style="display:block;width:100%;aspect-ratio:16/9;object-fit:cover;object-position:36% 40%;margin-top:40px;border-radius:2px">',
               '<img src="{{ img.r5_acad_hero }}" alt="" style="display:block;width:100%;aspect-ratio:16/9;object-fit:cover;object-position:50% 40%;margin-top:40px;border-radius:2px">')
    # H8 Tuyển dụng: khoá `team` còn ở bài N7, nên chỉ đổi thẻ <img> hero (aspect 4/3)
    s = rep(s, '<img src="{{ img.team }}" alt="" style="display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:2px">',
               '<img src="{{ img.r5_cr_hero }}" alt="" style="display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:2px">')
    # H9, H10 dải ảnh Hướng dẫn (VI/EN/中文): ảnh + alt + khung cắt. class gh-p / gh-v để r4.css đặt khung cắt mobile
    gp = 'style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:70% 55%;pointer-events:none">'
    for alt_old, alt_new in [('Chồng đá cân bằng với đồng xu trên đỉnh', 'Nhà đầu tư xem ứng dụng đầu tư trên điện thoại'),
                             ('Balanced stones with a coin on top', 'An investor checking an investing app on a phone'),
                             ('頂端放著硬幣的平衡石堆', '投資人在手機上查看投資應用程式')]:
        s = rep(s, '<img src="{{ img.pk_I03 }}" alt="%s" %s' % (alt_old, gp),
                   '<img class="gh-pic gh-p" src="{{ img.r5_gp_hero }}" alt="%s" style="position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;object-position:85%% 50%%;pointer-events:none">' % alt_new)
    gv = 'style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:right 40%;pointer-events:none">'
    for alt_old, alt_new in [('Tòa tháp kính vàng, hình ảnh chủ đạo của VNSHINE', 'Màn hình theo dõi giá và NAV của quỹ ETF'),
                             ('Gold glass tower, the VNSHINE key visual', 'Screens tracking ETF price and NAV'),
                             ('金色玻璃大樓，VNSHINE 主視覺', '追蹤 ETF 價格與 NAV 的螢幕')]:
        s = rep(s, '<img src="{{ img.vn_city }}" alt="%s" %s' % (alt_old, gv),
                   '<img class="gh-pic gh-v" src="{{ img.r5_gv_hero }}" alt="%s" style="position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;object-position:75%% 50%%;pointer-events:none">' % alt_new)
    # N1-N10 ảnh bài Góc nhìn (từng bài, khớp theo cặp khoá cũ + chữ đầu của dòng)
    for old, new in [('r3_nw_msci', 'r5_nw_msci'), ('r3_nw_rot', 'r5_nw_rot'), ('pk_I12', 'r5_nw_macro'), ('pk_I14', 'r5_nw_rebal'),
                     ('nw_city', 'r5_nw_aug'), ('pk_I15', 'r5_nw_fund'), ('team', 'r5_nw_bank'), ('pk_I13', 'r5_nw_dca'),
                     ('pk_I17', 'r5_nw_h2'), ('pk_I18', 'r5_nw_div')]:
        s = rep(s, '\n   {img:window.__I.%s,cat:' % old, '\n   {img:window.__I.%s,cat:' % new)
    return s


# ---------------------------------------------------------------- R4-04: ô giá ở hero VNSHINE và PHVSF
def p_r4_04(s):
    """Hàng chỉ số (Giá đóng cửa · NAV/CCQ · Ngày) thành lưới cột đều .px-row (CSS ở r4.css, khối R4-04).
    Bảng hiệu quả: cột nào mọi hàng đều '—' thì ẩn (tính trong renderVals, theo dữ liệu, không theo tên quỹ),
    thêm một dòng ghi chú khi có cột bị ẩn. Ngày niêm yết lấy từ PHFM_ANCHORS[quỹ].start (ngày dòng số liệu đầu tiên)."""
    LB = 'font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)'
    old = """<div style="display:flex;gap:40px;flex-wrap:wrap">
              <sc-if value="{{ f.isEtf }}"><div><div style="%s">{{ d.fundUi.closePrice }}</div><div style="display:flex;align-items:baseline;gap:6px;margin-top:6px"><span style="font-size:32px;line-height:40px;font-weight:700;color:var(--ink);letter-spacing:-.01em;font-variant-numeric:tabular-nums">{{ f.cuPrice }}</span><span style="font-size:14px;color:var(--muted)">{{ f.navUnit }}</span></div></div></sc-if>
              <div><div style="%s">{{ f.navLabel }}</div><div style="display:flex;align-items:baseline;gap:6px;margin-top:6px"><span style="font-size:32px;line-height:40px;font-weight:700;color:var(--ink);letter-spacing:-.01em;font-variant-numeric:tabular-nums">{{ f.cuNav }}</span><span style="font-size:14px;color:var(--muted)">{{ f.navUnit }}</span></div></div>
              <div><div style="%s">{{ d.fundUi.date }}</div><div style="font-size:24px;line-height:40px;font-weight:700;color:var(--ink);margin-top:6px">{{ f.asOf }}</div></div>
            </div>""" % (LB, LB, LB)
    new = """<div data-keepgrid class="px-row" style="--pxc:{{ f.pxCols }};--pxm:{{ f.pxColsM }}">
              <sc-if value="{{ f.isEtf }}"><div class="px-c"><div class="px-l">{{ d.fundUi.closePrice }}</div><div class="px-v">{{ f.cuPrice }}</div><div class="px-u">{{ f.navUnit }}</div></div></sc-if>
              <div class="px-c"><div class="px-l">{{ f.navLabel }}</div><div class="px-v">{{ f.cuNav }}</div><div class="px-u">{{ f.navUnit }}</div></div>
              <div class="px-c"><div class="px-l">{{ d.fundUi.date }}</div><div class="px-v">{{ f.asOf }}</div></div>
            </div>"""
    s = rep(s, old, new)
    # số cột bảng hiệu quả theo dữ liệu (tiêu đề và từng hàng)
    s = rep(s, 'grid-template-columns:minmax(0,1.3fr) repeat(3,minmax(0,1fr))', 'grid-template-columns:minmax(0,1.3fr) repeat({{ f.heroNCol }},minmax(0,1fr))', 2)
    # ghi chú cột bị ẩn, ngay dưới bảng
    s = rep(s, '<div style="font-size:12px;line-height:18px;font-style:italic;color:var(--muted);margin-top:14px">{{ f.heroNote }}</div>',
               '<sc-if value="{{ f.hasHidCol }}"><div class="px-note">{{ f.hidColNote }}</div></sc-if>\n            <div style="font-size:12px;line-height:18px;font-style:italic;color:var(--muted);margin-top:14px">{{ f.heroNote }}</div>')
    # logic: ẩn cột toàn '—'. Chạy sau khi cuRows đã tính từ chuỗi chung (p_fundcalc ở patches.py)
    s = rep(s, "        f.heroCols2 = wide ?",
               """        { const nc = F.heroCols.length, keep = [], hid = [];
          for (let i = 0; i < nc; i++) (f.cuRows.some(r => r.v[i] && r.v[i].t !== '—') ? keep : hid).push(i);
          if (!keep.length) { keep.push(...hid); hid.length = 0; }
          f.heroColsL = f.heroColsL.filter((_, i) => keep.indexOf(i) >= 0);
          f.cuRows = f.cuRows.map(r => ({ ...r, v: r.v.filter((_, i) => keep.indexOf(i) >= 0) }));
          f.heroNCol = String(keep.length); f.pxCols = F.isEtf ? 'repeat(3,auto)' : 'repeat(2,minmax(0,1fr))'; f.pxColsM = F.isEtf ? 'repeat(2,minmax(0,1fr))' : 'minmax(0,1fr)';
          const st = ((window.PHFM_ANCHORS || {})[p] || {}).start; f.hasHidCol = hid.length > 0 && !!st;
          if (f.hasHidCol) { const dmy = st.slice(8, 10) + '/' + st.slice(5, 7) + '/' + st.slice(0, 4), lbl = hid.map(i => F.heroCols[i]).join(', ');
            f.hidColNote = F.isEtf ? L3('Quỹ niêm yết ngày ' + dmy + ', chưa đủ dữ liệu ' + lbl + '.', 'The fund listed on ' + dmy + ', so there is not enough data for ' + lbl + ' yet.')
              : L3('Quỹ thành lập ngày ' + dmy + ', chưa đủ dữ liệu ' + lbl + '.', 'The fund was set up on ' + dmy + ', so there is not enough data for ' + lbl + ' yet.'); } }
        f.heroCols2 = wide ?""")
    return s


PATCHES4 = [p_r4_01, p_r4_05, p_r4_09, p_r4_04, p_r4css]
