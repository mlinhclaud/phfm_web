# Các bản vá áp lên tài liệu C + B gốc. Mỗi bản vá kiểm tra số lần khớp để tránh vá nhầm.
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))

def rep(s, old, new, count=1):
    n = s.count(old)
    if n != count:
        raise SystemExit('PATCH MISMATCH (%d != %d): %r' % (n, count, old[:120]))
    return s.replace(old, new)

def part(name):
    return open(os.path.join(HERE, 'parts', name), encoding='utf-8').read()

def apply_all(s):
    for fn in PATCHES:
        s = fn(s)
    return s

# ---------------------------------------------------------------- A01: đường dẫn riêng cho từng trang
def p_routing(s):
    # đọc trang + ngôn ngữ từ URL (#/vi/vnshine) ngay khi tải
    s = rep(s, '<meta name="robots" content="noindex">', part('head_route.html'))
    s = rep(s, "state = { page: 'home', lang: null,",
            "state = { page: window.__phfmRoute().page, lang: window.__phfmRoute().lang,")
    # đồng bộ khi bấm Back/Forward hoặc dán link
    s = rep(s, "    window.__phfmGo = p => this.go(p)();",
            "    window.__phfmGo = p => this.go(p)();\n"
            "    this.onHash = () => { const r = window.__phfmRoute(); const S = this.state; if (r.page !== S.page || r.lang !== (S.lang || 'vi')) { this.setState({ page: r.page, lang: r.lang, menu: false, navOpen: false }); window.scrollTo(0, 0); } };\n"
            "    window.addEventListener('hashchange', this.onHash);")
    # đổi trang -> ghi vào URL
    s = rep(s, "go(p) { return () => { this.setState({ page: p,",
            "go(p) { return () => { window.__phfmSetHash(this.state.lang || 'vi', p); this.setState({ page: p,")
    # đổi ngôn ngữ -> ghi vào URL, bỏ postMessage ra khung demo
    s = rep(s, "setVi: () => (this.setState({ lang: 'vi' }), parent.postMessage({ phfmLang: 'vi' }, '*')), setEn: () => (this.setState({ lang: 'en' }), parent.postMessage({ phfmLang: 'en' }, '*')), setZh: () => (this.setState({ lang: 'zh' }), parent.postMessage({ phfmLang: 'zh' }, '*')),",
            "setVi: () => (window.__phfmSetHash('vi', this.state.page), this.setState({ lang: 'vi' })), setEn: () => (window.__phfmSetHash('en', this.state.page), this.setState({ lang: 'en' })), setZh: () => (window.__phfmSetHash('zh', this.state.page), this.setState({ lang: 'zh' })),")
    # tiêu đề tab trình duyệt theo trang
    s = rep(s, "    const p = this.state.page, S = this.state;\n",
            "    const p = this.state.page, S = this.state;\n    window.__phfmTitle && window.__phfmTitle(p, l);\n")
    return s

# ---------------------------------------------------------------- A08 + A11: template không nằm trong DOM sống
def p_template(s):
    """Template dc được để trong <script type="text/x-dc-template"> thay vì <x-dc> sống:
    trình duyệt không tải các ảnh {{ p.img }} giả, console không báo lỗi SVG/ô ngày,
    và runtime không tải lại toàn bộ trang (fetch location.href) để lấy template."""
    a = s.index('<x-dc>', s.index('<body>'))
    b = s.index('</x-dc>', a)
    tpl = s[a + 6:b]
    assert '</script' not in tpl
    s = s[:a] + '<x-dc></x-dc><script type="text/x-dc-template" id="dc-tpl">' + tpl + '</script>' + s[b + 7:]
    s = rep(s, '      template: dc.innerHTML,',
            '      template: doc.getElementById("dc-tpl") ? doc.getElementById("dc-tpl").textContent : dc.innerHTML,')
    s = rep(s, '    if (!window.__resources) {\n      fetch(location.href)',
            '    if (!window.__resources && !doc.getElementById("dc-tpl")) {\n      fetch(location.href)')
    return s

# ---------------------------------------------------------------- A11: mỗi ảnh nhúng 1 lần
REMAP_TPL = {}   # (vị trí) -> khoá ảnh mới, điền ở p_images_remap

def p_images(s):
    s = rep(s, '<script>\n/* Định tuyến', '<!--@@IMGREG@@-->\n<script>\n/* Định tuyến')
    # template: <img src="@@IMG:k@@"> -> src="{{ img.k }}"
    s = re.sub(r'src="@@IMG:(\w+)@@"', lambda m: 'src="{{ img.%s }}"' % m.group(1), s)
    # chuỗi JS ...url(@@IMG:k@@)... -> nối chuỗi
    s = re.sub(r"url\(@@IMG:(\w+)@@\)'", lambda m: "url(' + window.__I.%s + ')'" % m.group(1), s)
    # chuỗi JS '@@IMG:k@@' -> window.__I.k
    s = re.sub(r"'@@IMG:(\w+)@@'", lambda m: 'window.__I.%s' % m.group(1), s)
    s = rep(s, '      d, is, go, act, guide,', '      img: window.__I, d, is, go, act, guide,')
    return s

# ---------------------------------------------------------------- Trang chủ Teal Vanguard + footer chung
def p_home(s):
    a = s.index('  <sc-if value="{{ is.home }}" hint-placeholder-val="{{ true }}">')
    b = s.index('  <sc-if value="{{ is.fund }}">', a)
    s = s[:a] + part('home.html') + '\n' + s[b:]
    a = s.index('    const TH0 = {')
    b = s.index('    const spans = [', a)
    s = s[:a] + part('th.js') + '\n' + s[b:]
    a = s.index('<footer style="background:#E3EEF0;border-top:4px solid #E9C46A">')
    b = s.index('</footer>', a) + len('</footer>')
    s = s[:a] + part('footer.html') + s[b:]
    s = rep(s, '      img: window.__I, d, is, go, act, guide,',
            "      img: window.__I, hrefs, ftL: l === 'vi' ? { li: 'PHFM trên LinkedIn', fb: 'PHFM trên Facebook', yt: 'PHFM trên YouTube', ios: 'Tải về trên App Store', and: 'Tải về trên Google Play' } : { li: 'PHFM on LinkedIn', fb: 'PHFM on Facebook', yt: 'PHFM on YouTube', ios: 'Download on the App Store', and: 'Get it on Google Play' }, d, is, go, act, guide,")
    # CSS trang chủ + footer + theme: đặt cuối helmet để đè các lớp CSS cũ
    s = rep(s, '</helmet>', '<style>' + part('home.css') + '</style>\n<style>' + part('theme.css') + '</style>\n</helmet>')
    return s

def p_header(s):
    s = rep(s, '''<div onClick="{{ go.home }}" style="cursor:pointer;display:flex;align-items:center">
        <x-import component-from-global-scope="PHFMDesignSystem_f2e5ca.Logo" asset-base="assets" height="{{ 58 }}" hint-size="96px,58px"></x-import>
      </div>''', '''<a href="{{ hrefs.home }}" onClick="{{ go.home }}" class="th-logo" aria-label="{{ ftL.home }}"><img src="{{ img.hm_logo }}" alt="Phu Hung Fund Management"></a>''')
    s = rep(s, 'Hotline {{ d.ui.hotline }}</a>', 'Hotline (028) 5413 7991</a>')
    s = rep(s, 'href="tel:02854137991" class="tb-a"', 'href="tel:+842854137991" class="tb-a"')
    # icon tìm kiếm + menu theo canvas mobile
    s = rep(s, '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#0A3440" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.6-3.6"/></svg>',
            '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#16262B" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>')
    s = rep(s, '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#0A3440" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
            '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#16262B" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg>')
    s = rep(s, '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#0A3440" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
            '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#16262B" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>')
    s = rep(s, "ios: 'Tải về trên App Store', and: 'Tải về trên Google Play' }", "ios: 'Tải về trên App Store', and: 'Tải về trên Google Play', home: 'PHFM trang chủ' }")
    s = rep(s, "ios: 'Download on the App Store', and: 'Get it on Google Play' }", "ios: 'Download on the App Store', and: 'Get it on Google Play', home: 'PHFM home' }")
    return s

def p_scripts_exempt(s):
    """Các script chỉnh layout mobile/hiệu ứng cũ không đụng vào trang chủ mới và footer mới."""
    s = rep(s, "if(e.closest('[data-keepgrid]'))return;var cs=getComputedStyle(e);if(cs.display==='flex'&&m",
               "if(e.closest('[data-keepgrid],[data-hm],.ft'))return;var cs=getComputedStyle(e);if(cs.display==='flex'&&m")
    s = rep(s, "document.querySelectorAll('main section, main section>div, footer>div').forEach(function(e){var cs=getComputedStyle(e);",
               "document.querySelectorAll('main section, main section>div, footer>div').forEach(function(e){if(e.closest('[data-hm],.ft'))return;var cs=getComputedStyle(e);")
    s = rep(s, "if(e.closest('[data-keepgrid],svg,button,a,input,select,textarea,label,.th-hero'))continue;",
               "if(e.closest('[data-keepgrid],svg,button,a,input,select,textarea,label,.th-hero,[data-hm],.ft'))continue;")
    s = rep(s, "document.querySelectorAll('main section').forEach(function(sec,si){if(si===0)return;",
               "document.querySelectorAll('main:not([data-hm]) section').forEach(function(sec,si){if(si===0)return;")
    return s

FD = os.path.join(HERE, '..', 'vendor', 'fonts')
UR = {'latin': 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD',
      'vietnamese': 'U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB'}

def p_fonts(s):
    """A12: chỉ dùng Inter, nhúng sẵn (latin + tiếng Việt, 300–700). Bỏ Playfair/Meow Script/Noto tải từ Google
    và bỏ @font-face Microsoft JhengHei trỏ tới file ../fonts/*.ttf không tồn tại."""
    import base64
    a = s.index('@import url("https://fonts.googleapis.com/css2?family=Playfair+Display')
    b = s.index('\n', a)
    s = s[:a] + s[b + 1:]
    s = re.sub(r'@font-face \{ font-family: "Microsoft JhengHei";[^}]*\}\n', '', s)
    ff = []
    for w in (300, 400, 500, 600, 700):
        for sub in ('latin', 'vietnamese'):
            data = base64.b64encode(open(os.path.join(FD, 'inter-%s-%d-normal.woff2' % (sub, w)), 'rb').read()).decode()
            ff.append("@font-face{font-family:'Inter';font-style:normal;font-display:swap;font-weight:%d;src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s}" % (w, data, UR[sub]))
    s = rep(s, '<!--@@IMGREG@@-->', '<style>' + ''.join(ff) + '</style>\n<!--@@IMGREG@@-->')
    # căn đều 2 lề tự động: không áp vào trang chủ mới
    s = rep(s, "function okBlock(el){var cs=getComputedStyle(el);", "function okBlock(el){if(el.closest('[data-hm],.ft'))return false;var cs=getComputedStyle(el);")
    return s

def p_retheme(s):
    """C01: đưa màu các trang con về bộ teal của homepage."""
    s = rep(s, '--gold-amber: #C0962D;     /* bright accent, CTA fill */', '--gold-amber: #E9C46A;     /* bright accent, CTA fill */')
    s = rep(s, '--gold-soft: #FCF0CC;      /* badge, highlight, soft accent ground */', '--gold-soft: #DCEBEE;      /* badge, highlight, soft accent ground (teal) */')
    s = rep(s, '  --sand: #D3DEE1;', '  --sand: #D8E7EA;')
    s = rep(s, '  --muted: #5B6B70;', '  --muted: #4D6066;')
    s = rep(s, '  --up-on-light: #0E7C66;', '  --up-on-light: #15897D;')
    s = rep(s, '  --teal-deep: #0E7C66;', '  --teal-deep: #15897D;')
    s = rep(s, '  --indigo-deep: #2B4C7E;', '  --indigo-deep: #86B4BE;')
    # đường biểu đồ: quỹ = vàng logo, so sánh = teal-grey, đường thứ 3 = teal thương hiệu
    s = rep(s, "const colors = ['#C0962D', '#2B4C7E', '#12A98C'];", "const colors = ['#C0962D', '#86B4BE', '#0B6274'];")
    # 3 trụ cột Shareholder Yield: nâu → vàng → vàng chanh  ⇒  teal đậm → teal → vàng
    s = rep(s, "bg: ['#7D5F1A', '#C0962D', '#E8B923'][i], fg: ['#FFFFFF', '#FFFFFF', '#0A3440'][i]",
               "bg: ['#0A3440', '#0B6274', '#E9C46A'][i], fg: ['#FFFFFF', '#FFFFFF', '#16181A'][i]")
    # lớp phủ màu kem trên ảnh hero  ⇒  trắng
    s = s.replace('rgba(255,248,234,', 'rgba(255,255,255,')
    # bản đồ minh hoạ nền be  ⇒  tông teal nhạt
    s = rep(s, 'background:#EFE6D2;overflow:hidden', 'background:#E3EEF0;overflow:hidden')
    s = rep(s, 'height:24%;background:#E3E7E2', 'height:24%;background:#D8E7EA')
    # nút vàng phụ (khối CTA trang hướng dẫn)
    s = s.replace('background:#E0AE3A;', 'background:#E9C46A;').replace('border:1px solid #E0AE3A}', 'border:1px solid #E9C46A}')
    # viền logo đại lý dùng màu be dự phòng
    s = rep(s, 'border:1px solid var(--sand,#E8DFC8)', 'border:1px solid var(--sand,#D8E7EA)')
    # thanh tiêu đề gradient vàng-nâu (hl-u, hl-tb...)  ⇒  vàng logo một màu
    s = s.replace('linear-gradient(90deg,color-mix(in srgb,var(--hlc,#C0962D) 62%,#000),var(--hlc,#C0962D) 55%,color-mix(in srgb,var(--hlc,#C0962D) 45%,#fff))', 'var(--hlc,#C0962D)')
    s = s.replace('linear-gradient(90deg,color-mix(in srgb,var(--hlc2,#C0962D) 62%,#000),var(--hlc2,#C0962D) 55%,color-mix(in srgb,var(--hlc2,#C0962D) 45%,#fff))', 'var(--hlc2,#C0962D)')
    s = s.replace('linear-gradient(90deg,color-mix(in srgb,currentColor 62%,#000),currentColor 55%,color-mix(in srgb,currentColor 45%,#fff))', 'currentColor')
    # ghim bản đồ liên hệ: nâu  ⇒  teal
    s = rep(s, 'background:rgba(122,92,0,.18);display:flex;align-items:center;justify-content:center"><span style="width:16px;height:16px;border-radius:50%;background:var(--gold-ink)">',
               'background:rgba(11,98,116,.18);display:flex;align-items:center;justify-content:center"><span style="width:16px;height:16px;border-radius:50%;background:#0B6274">')
    return s

import json as _json
def _picks():
    pf = os.path.join(HERE, 'picks.json')
    return _json.load(open(pf)) if os.path.exists(pf) else {}

def p_imgmap(s):
    """C02: thay ảnh tông be/nâu theo bảng ảnh Rin đã duyệt (vòng 1 + vòng 2)."""
    P = _picks()
    k = lambda slot, orig: ('pk_' + slot) if ('pk_' + slot) in P else orig
    # I01: hero trang Về chúng tôi (2 bản desktop/mobile trong template)
    s = s.replace('<img src="@@IMG:advisor@@"', '<img src="@@IMG:ab_hero@@"')
    # I02: dải Sứ mệnh / Tầm nhìn
    s = rep(s, '<img src="@@IMG:coinplant@@"', '<img src="@@IMG:%s@@"' % k('I02', 'coinplant'))
    # I03 + I04: ảnh đá cuội / tháp vàng dùng ở trang quỹ, hướng dẫn, học viện, CTA
    s = s.replace('@@IMG:dc_stones@@', '@@IMG:%s@@' % k('I03', 'dc_stones'))
    s = s.replace('@@IMG:dc_vntower@@', '@@IMG:vn_city@@')
    # I05, I06: hero Quản lý danh mục, Tư vấn đầu tư (trong dữ liệu dịch vụ)
    s = rep(s, "portfolio:{img:'@@IMG:docs@@'", "portfolio:{img:'@@IMG:%s@@'" % k('I05', 'docs'))
    s = rep(s, "advisory:{img:'@@IMG:office@@'", "advisory:{img:'@@IMG:%s@@'" % k('I06', 'office'))
    # I07: hero Học viện (2 bản)
    s = s.replace('<img src="@@IMG:planner@@"', '<img src="@@IMG:%s@@"' % k('I07', 'planner'))
    # I08–I11: 4 thẻ Tuyển dụng
    s = rep(s, "img: ['@@IMG:desk@@', '@@IMG:handshake@@', '@@IMG:office@@', '@@IMG:plant@@'][i % 4]",
            "img: ['@@IMG:%s@@', '@@IMG:cr_team@@', '@@IMG:cr_grow@@', '@@IMG:%s@@'][i %% 4]" % (k('I08', 'desk'), k('I11', 'plant')))
    # I12–I18: ảnh bài viết Góc nhìn (theo thứ tự trong danh sách)
    def seq(s, old, keys):                 # thay lần lượt các lần xuất hiện bằng các khoá tương ứng
        pos = [m.start() for m in re.finditer(re.escape(old), s)]
        assert len(pos) == len(keys), (old, len(pos))
        for i, kk in reversed(list(zip(pos, keys))):
            s = s[:i] + old.replace(old[old.index('@@IMG:') + 6:old.rindex('@@')], kk) + s[i + len(old):]
        return s
    s = seq(s, "\n   {img:'@@IMG:planner@@'", [k('I12', 'planner'), k('I13', 'planner')])
    s = seq(s, "\n   {img:'@@IMG:docs@@'", [k('I14', 'docs'), k('I15', 'docs')])
    s = rep(s, "{img:'@@IMG:tower@@'", "{img:'@@IMG:nw_city@@'")
    s = rep(s, "{img:'@@IMG:g_book@@'", "{img:'@@IMG:%s@@'" % k('I17', 'g_book'))
    s = rep(s, "{img:'@@IMG:coinplant@@'", "{img:'@@IMG:%s@@'" % k('I18', 'coinplant'))
    return s

def p_funddata(s):
    s = rep(s, '<!--@@IMGREG@@-->', part('fund_anchors.html') + '\n<!--@@IMGREG@@-->')
    s = rep(s, "  fmt(v, dec) { return v.toFixed(dec).replace('.', ',').replace(/\\B(?=(\\d{3})+(?!\\d))/g, '.'); }\n",
            "  fmt(v, dec) { return v.toFixed(dec).replace('.', ',').replace(/\\B(?=(\\d{3})+(?!\\d))/g, '.'); }\n" + part('fundcalc.js'))
    # dòng "Cập nhật lúc 15:00 ngày <hôm nay>"  ⇒  ngày số liệu cố định + nhãn minh hoạ
    a = s.index("{ const nw = new Date(); let bd = new Date(nw.getFullYear(), nw.getMonth(), nw.getDate());")
    b = s.index("'Updated 15:00, ' + ds; }", a) + len("'Updated 15:00, ' + ds; }")
    s = s[:a] + "{ const A0 = window.PHFM_ASOF, ds = A0.slice(8, 10) + '/' + A0.slice(5, 7) + '/' + A0.slice(0, 4); d.ui.source = l === 'vi' ? 'Số liệu minh hoạ, cập nhật đến ngày ' + ds : l === 'zh' ? '示意數據，更新至 ' + A0.replace(/-/g, '/') : 'Illustrative data as of ' + ds; d.ui.asOfDate = ds; }" + s[b:]
    # bảng lịch sử NAV: lấy từ chuỗi chung, không lấy theo ngày mở trang
    a = s.index("      const allDays = []; {")
    b = s.index("      const navTab = (S.navTab === 1 || F.isEtf)", a)
    s = s[:a] + """      const FC = this.fundCalc(p);
      const navAll = []; for (let i = FC.N - 1; i >= Math.max(1, FC.N - 160); i--) { const iso = FC.ds[i], vv = FC.nav[i], ch = (FC.nav[i] / FC.nav[i - 1] - 1) * 100, pdv = FC.pdOf(i); navAll.push({ raw: vv, iso, date: iso.slice(8, 10) + '.' + iso.slice(5, 7) + '.' + iso.slice(0, 4), nav: this.fmt(vv, 2), chg: this.pct(ch, 2, true), up: ch >= 0, down: ch < 0, close: this.fmt(vv * (1 + pdv / 100), 0), pd: this.pct(pdv, 2), pdUp: pdv >= 0, pdDown: pdv < 0 }); }
""" + s[b:]
    # NAV cao/thấp nhất trong năm: tính trên cả chuỗi của năm hiện tại
    s = rep(s, "navYr = navAll.filter(r => r.iso.slice(0, 4) === navAll[0].iso.slice(0, 4)),",
               "navYr = FC.ds.map((iso, i) => ({ iso, raw: FC.nav[i] })).filter(r => r.iso.slice(0, 4) === navAll[0].iso.slice(0, 4)),")
    # tab NAV đang chọn: teal + chữ trắng (vàng + chữ trắng không đủ tương phản)
    s = s.replace("bc: navTab === 0 ? 'var(--gold)' : 'transparent', bg: navTab === 0 ? 'var(--gold)' : 'transparent'", "bc: navTab === 0 ? 'var(--brand)' : 'transparent', bg: navTab === 0 ? 'var(--brand)' : 'transparent'")
    s = s.replace("bc: navTab === 1 ? 'var(--gold)' : 'transparent', bg: navTab === 1 ? 'var(--gold)' : 'transparent'", "bc: navTab === 1 ? 'var(--brand)' : 'transparent', bg: navTab === 1 ? 'var(--brand)' : 'transparent'")
    # biểu đồ: dùng đúng chuỗi chung, kết thúc ở ngày số liệu
    a = s.index("if (!this._phc) this._phc = {}; this._ph = this._phc[p]; if (!this._ph) {")
    b = s.index("this._phc[p] = this._ph; }", a) + len("this._phc[p] = this._ph; }")
    s = s[:a] + "this._ph = { ds: FC.ds, s: [FC.V[0], FC.V[1]] };" + s[b:]
    # YTD trên biểu đồ tính từ phiên cuối năm trước (giống số công bố)
    s = rep(s, "['YTD', pMax.slice(0, 4) + '-01-01']", "['YTD', FC.ds[FC.iY]]")
    # ô hiệu quả ở hero: tính từ chuỗi chung, có dấu và màu theo tăng/giảm
    s = rep(s, "f.cuRows = F.heroRows.map(r => ({ n: r.n, v: r.v.map(x => ({ t: '▲ +' + this.fmt(x * cu, 2) + '%' })) }));",
            "f.cuRows = F.heroRows.map((r, j) => ({ n: r.n, v: ['m1', 'm3', 'si'].map(k => { const x = FC.ret(k, j); return { t: x == null ? '—' : this.pct(x * cu, 2, true), c: x == null ? 'var(--muted)' : x >= 0 ? 'var(--up-on-light)' : 'var(--down-on-light)' }; }) }));")
    s = rep(s, '<sc-for list="{{ hr.v }}" as="hv" hint-placeholder-count="3"><div style="padding:12px 8px;text-align:right;color:var(--up-on-light);font-variant-numeric:tabular-nums;white-space:nowrap">{{ hv.t }}</div></sc-for>',
               '<sc-for list="{{ hr.v }}" as="hv" hint-placeholder-count="3"><div style="padding:12px 8px;text-align:right;color:{{ hv.c }};font-variant-numeric:tabular-nums;white-space:nowrap">{{ hv.t }}</div></sc-for>')
    # NAV hero, giá đóng cửa, chênh lệch giá/NAV, bảng kỳ hiệu quả: cùng nguồn
    s = rep(s, "f.cuPrice = F.price ? this.fmt(parseFloat(F.price.replace(/\\./g, '')) * (S.cu === undefined ? 0 : S.cu), 0) : '';",
               "const close0 = FC.nav[FC.N - 1] * (1 + FC.pdOf(FC.N - 1) / 100); f.cuPrice = F.isEtf ? this.fmt(close0 * cu, 0) : '';\n        if (f.trading) { const pd0 = FC.pdOf(FC.N - 1); f.trading = { ...f.trading, price: this.fmt(close0, 0), inav: this.fmt(FC.nav[FC.N - 1], 2), pd: this.pct(pd0, 2, true), pdColor: pd0 >= 0 ? 'var(--up-on-light)' : 'var(--down-on-light)' }; }\n        { const km = { '1 tháng': 'm1', '1M': 'm1', '3 tháng': 'm3', '3M': 'm3', '6 tháng': 'm6', '6M': 'm6', 'YTD': 'ytd', '1 năm': 'y1', '1Y': 'y1', '3 năm': 'y3', '3Y': 'y3' }; f.perf = D.funds[p].perf.map((r0, ri) => { const lab = d.funds[p].perf[ri].p, key = km[typeof r0.p === 'string' ? r0.p : r0.p.vi] || 'si'; return { p: lab, c: [0, 1].map(j => ({ v: this.pct(FC.ret(key, j), 1, true) })) }; }); }")
    s = rep(s, '<div style="font-size:30px;font-weight:700;color:var(--down-on-light);margin-top:8px">▼ {{ f.trading.pd }}</div>',
               '<div style="font-size:30px;font-weight:700;color:{{ f.trading.pdColor }};margin-top:8px">{{ f.trading.pd }}</div>')
    # thẻ NAV phiên bản cũ (f.oldL) cũng lấy số chung
    s = rep(s, "      f.newL = true; f.oldL = false;", "      f.newL = true; f.oldL = false; { const ch0 = (FC.nav[FC.N - 1] / FC.nav[FC.N - 2] - 1) * 100; f.change = this.pct(ch0, 2, true); f.up = ch0 >= 0; f.down = ch0 < 0; }")
    # Danh sách quỹ: lấy cùng nguồn số
    s = rep(s, "    const p = this.state.page, S = this.state;\n",
            "    const p = this.state.page, S = this.state;\n    if (p === 'funds') { const A = this.fundCalc('phvsf'), B = this.fundCalc('vnshine'), vi = l === 'vi'; d.ui.fl_p_ytd = this.pct(A.ret('ytd', 0), 2); d.ui.fl_p_bm = 'VN-Index: ' + this.pct(A.ret('ytd', 1), 2); d.ui.fl_v_ytd = this.pct(B.ret('si', 0), 2); d.ui.fl_v_bm = (vi ? 'Từ khi niêm yết 10/09/2026 · Chỉ số VNSHINE: ' : 'Since listing on 10/09/2026 · VNSHINE Index: ') + this.pct(B.ret('si', 1), 2); d.ui.fl_src = d.ui.fl_src + ' ' + d.ui.source + '.'; }\n")
    s = rep(s, '{{ d.ui.fl_v_ytd }}</div><div style="font-size:13px;color:var(--muted);margin-top:4px"></div>',
               '{{ d.ui.fl_v_ytd }}</div><div style="font-size:13px;color:var(--muted);margin-top:4px">{{ d.ui.fl_v_bm }}</div>')
    return s

def p_dates(s):
    """A09: ô chọn ngày hiển thị dd/mm/yyyy (VI, EN) thay vì định dạng Mỹ theo trình duyệt."""
    def wrap(s, inp, disp, extra_style):
        new = ('<span class="dtw"' + extra_style + '>' + inp.replace('<input type="date" ', '<input type="date" class="dti" onClick="{{ pickerOpen }}" ')
               + '<span class="dtv">{{ ' + disp + ' }}</span></span>')
        return rep(s, inp, new)
    import re as _re
    for var, disp in (('f.pS', 'f.pSd'), ('f.pE', 'f.pEd'), ('f.navFrom', 'f.navFromD'), ('f.navTo', 'f.navToD')):
        m = _re.search(r'<input type="date" value="\{\{ ' + _re.escape(var) + r' \}\}"[^>]*>', s)
        s = wrap(s, m.group(0), disp, '')
    s = rep(s, "        f.pS = pS; f.pE = pE;", "        f.pS = pS; f.pE = pE; f.pSd = dmy(pS); f.pEd = dmy(pE);")
    s = rep(s, "      const navMore = navN < navFilt.length,",
               "      const dmy2 = x => x ? x.slice(8, 10) + '/' + x.slice(5, 7) + '/' + x.slice(0, 4) : 'dd/mm/yyyy';\n      const navMore = navN < navFilt.length,")
    s = rep(s, "navFrom = S.navFrom || '', navTo = S.navTo || '',", "navFrom = S.navFrom || '', navTo = S.navTo || '', navFromD = dmy2(S.navFrom), navToD = dmy2(S.navTo),")
    s = rep(s, "onNavFrom, onNavTo, navFrom, navTo,", "onNavFrom, onNavTo, navFrom, navTo, navFromD, navToD,")
    s = rep(s, "      img: window.__I, hrefs,", "      pickerOpen: e => { try { e.target.showPicker && e.target.showPicker(); } catch (_) {} },\n      img: window.__I, hrefs,")
    return s

def p_fixes(s):
    # hành vi chung: href="#", nút tải tài liệu, tìm kiếm (A01, A05, A06)
    i = s.rindex('</body>')
    s = s[:i] + part('site.js') + s[i:]
    # A10: căn đều chỉ áp cho đoạn rộng trên desktop; cột hẹp và mobile căn trái
    s = rep(s, "function okBlock(el){if(el.closest('[data-hm],.ft'))return false;var cs=getComputedStyle(el);",
               "function okBlock(el){if(el.closest('[data-hm],.ft'))return false;if(window.innerWidth<=760||el.getBoundingClientRect().width<480){el.style.setProperty('text-align','left','important');return false}var cs=getComputedStyle(el);")
    # A14: chữ tiếng Việt còn sót trong bản EN
    s = rep(s, 'hint-size="260px,44px">Tải danh mục cơ cấu (PCF) ↓</x-import>', 'hint-size="260px,44px">{{ d.fundUi.pcf }} ↓</x-import>')
    s = rep(s, "csv:b('Tải CSV/Excel','Download CSV/Excel'),", "csv:b('Tải CSV/Excel','Download CSV/Excel'),pcf:b('Tải danh mục cơ cấu (PCF)','Download portfolio composition file (PCF)'),")
    s = s.replace("a:'Khối Đầu tư PHFM'", "a:b('Khối Đầu tư PHFM','PHFM Investment Division')")
    # A16: ẩn khung "Ghi chú demo · Mục CMS" ở trang Danh sách quỹ (nội dung dành cho người duyệt demo)
    a = s.index('<div style="margin-top:48px;border:1px dashed var(--gold-ink);padding:24px 28px;max-width:880px;background:var(--cream)">')
    b = s.index('</div>', s.index('{{ d.ui.fl_cms_s }}', a)) + len('</div>')
    s = s[:a] + '<!-- A16: ghi chú demo CMS đã ẩn; nội dung chuyển vào README bàn giao -->' + s[b:]
    # B04: ví dụ tính lãi ở Học viện ghi rõ là minh hoạ
    s = rep(s, "demo:b('Số liệu minh hoạ','Illustrative data'),",
               "demo:b('Số liệu minh hoạ','Illustrative data'),exNote:b('Ví dụ minh hoạ, không phải cam kết lợi nhuận.','Illustrative example only, not a promise of returns.'),")
    s = rep(s, '<div style="font-size:16px;line-height:26px;color:var(--ink);margin-top:10px">{{ academy.cur.ex }}</div></div>',
               '<div style="font-size:16px;line-height:26px;color:var(--ink);margin-top:10px">{{ academy.cur.ex }}</div><div style="font-size:12.5px;line-height:20px;font-style:italic;color:var(--muted);margin-top:10px">{{ d.ui.exNote }}</div></div>')
    return s

import patches2 as _p2
import patches4 as _p4
import patches5 as _p5
PATCHES = [p_routing, p_template, p_imgmap] + _p2.PRE + [p_images, p_home, p_header, p_scripts_exempt, p_fonts, p_retheme, p_funddata, p_dates, p_fixes] + _p2.POST + _p4.PATCHES4 + _p5.PATCHES5
