# Vòng 6 (nhóm R6-04, R6-05): trang quỹ PHVSF, VNSHINE, Danh sách quỹ, Công bố thông tin; Về chúng tôi.
# Mỗi mục là một hàm vá trong PATCHES6C. CSS viết ở parts/r6c.css (nạp sau r6.css).
# Chữ mới: VI theo bình luận của Linh, EN tương đương, 中文 không tự dịch (khoá zh là chữ EN, chữ EN đổi thì zh hiện EN
# cho tới khi cô Helena duyệt). Mọi chữ mới ghi "chờ pháp chế" trong specs/dev-handoff.md mục 6d.
from patches import rep, part


def p_r6c_css(s):
    return rep(s, '</helmet>', '<style>' + part('r6c.css') + '</style></helmet>')


# ---------------------------------------------------------------- R6-04 · Q5 thuật ngữ Shareholder Yield
def p_r6_04_yield(s):
    """Q5 (issue #9): bản VI dùng "Tỷ suất Lợi nhuận Cổ đông" thay cho "Lợi suất Cổ đông" ở mọi chỗ (brand-rules).
    11 chỗ: 10 trong dữ liệu/template (phụ đề Học viện, hero và thẻ VNSHINE, tổng quan, tiêu đề chiến lược, FAQ, thuật ngữ)
    và 1 ở tiêu đề tab (site.js). Bản EN giữ "Shareholder Yield" (không đổi). Tiêu đề tin 10.09.2026 viết "lợi suất cho cổ đông"
    (cùng khái niệm) đổi theo cho đồng nhất."""
    s = rep(s, 'Lợi suất Cổ đông', 'Tỷ suất Lợi nhuận Cổ đông', 11)
    s = rep(s, 'chiến lược lợi suất cho cổ đông', 'chiến lược tỷ suất lợi nhuận cổ đông')
    return s


# ---------------------------------------------------------------- R6-04 · #111, #100 nhãn hero PHVSF
def p_r6_04_eyebrow(s):
    """#111 (VI) và #100 (EN): nhãn nhỏ trên tiêu đề hero PHVSF còn "QUỸ MỞ · GIAO DỊCH HẰNG NGÀY" / "OPEN-ENDED FUND · DAILY DEALING".
    Đổi thành "QUỸ MỞ" / "OPEN-ENDED FUND". Khoá zh cũ ("OPEN-ENDED EQUITY FUND · DAILY DEALING") đã không còn khớp EN từ trước,
    nên 中文 không thay đổi so với hiện tại; chờ cô Helena."""
    return rep(s, "heroEyebrow:b('QUỸ MỞ · GIAO DỊCH HẰNG NGÀY','OPEN-ENDED FUND · DAILY DEALING'),",
                  "heroEyebrow:b('QUỸ MỞ','OPEN-ENDED FUND'),")


# ---------------------------------------------------------------- R6-04 · #50, Q7 ghi chú nhỏ in nghiêng
def p_r6_04_notes(s):
    """#50, #72 (Q7): ghi chú dưới bảng và biểu đồ thống nhất chữ nhỏ 12px, in nghiêng, màu --muted.
    Giữ nội dung "Số liệu minh hoạ, cập nhật đến ngày…" (brand-rules). Trước đó: "Số liệu minh hoạ" không nghiêng (3 chỗ ở trang quỹ,
    13px không nghiêng ở Danh sách quỹ), ghi chú hiệu quả 12,5px, "*Theo dữ liệu tại ngày" 13px."""
    s = rep(s, '<div style="font-size:12px;color:var(--muted);margin-top:10px">{{ d.ui.source }} · {{ d.ui.d2 }}</div>',
               '<div style="font-size:12px;font-style:italic;color:var(--muted);margin-top:10px">{{ d.ui.source }} · {{ d.ui.d2 }}</div>')
    s = rep(s, '<div style="font-size:12px;color:var(--muted);margin-top:16px">{{ d.ui.source }} · {{ d.ui.d2 }}</div>',
               '<div style="font-size:12px;font-style:italic;color:var(--muted);margin-top:16px">{{ d.ui.source }} · {{ d.ui.d2 }}</div>')
    s = rep(s, '<div style="font-size:12px;color:var(--muted);margin-top:16px">{{ d.ui.source }}</div>',
               '<div style="font-size:12px;font-style:italic;color:var(--muted);margin-top:16px">{{ d.ui.source }}</div>')
    s = rep(s, 'background:transparent;font-size:12.5px;line-height:20px;font-style:italic;color:var(--muted)">{{ f.perfNoteShow }}</div>',
               'background:transparent;font-size:12px;line-height:20px;font-style:italic;color:var(--muted)">{{ f.perfNoteShow }}</div>')
    s = rep(s, '<div style="font-size:13px;font-style:italic;color:var(--muted);margin-top:12px">{{ d.fundUi.latNote }} {{ f.latest.d }}</div>',
               '<div style="font-size:12px;font-style:italic;color:var(--muted);margin-top:12px">{{ d.fundUi.latNote }} {{ f.latest.d }}</div>')
    s = rep(s, '<p style="font-size:13px;color:var(--muted);margin:16px 0 0">{{ d.ui.fl_src }}</p>',
               '<p style="font-size:12px;font-style:italic;color:var(--muted);margin:16px 0 0">{{ d.ui.fl_src }}</p>')
    return s


# ---------------------------------------------------------------- R6-04 · #3 "Chọn tất cả" bấm được cả dòng
def p_r6_04_selall(s):
    """#3: ở Tài liệu quỹ chỉ ô tick bấm được, chữ "Chọn tất cả" thì không. Đưa onClick lên cả dòng .fd-head (chữ + ô);
    ô tick bên trong không còn onClick riêng (tránh bấm một lần mà chọn rồi bỏ chọn)."""
    return rep(s, '<div class="fd-head" data-keepgrid><span onClick="{{ f.fdToggleAll }}" role="checkbox" class="fd-cb">',
                  '<div class="fd-head" data-keepgrid onClick="{{ f.fdToggleAll }}" role="checkbox"><span class="fd-cb">')


# ---------------------------------------------------------------- R6-04 · Q8 loại tài liệu của trang quỹ
def p_r6_04_docs(s):
    """Q8 (#94, #98, #115, #116, #130, #134):
    - Tài liệu quỹ PHVSF và VNSHINE: bộ lọc hiện đủ 9 loại (Báo cáo ngày, tuần / Báo cáo tài chính / Báo cáo hoạt động tháng /
      Factsheets / Bản cáo bạch / Điều lệ quỹ / Thông tin quỹ / Giấy phép / Khác), kể cả loại chưa có file. Chọn loại chưa có file
      thì hiện một dòng "Tài liệu đang được cập nhật" với nút tải báo thông báo (site.js).
    - Biểu mẫu chuyển hẳn sang trang Biểu mẫu: bỏ "Mẫu đăng ký mua/bán chứng chỉ quỹ" (PHVSF) và "Bộ tài liệu dành cho thành viên lập quỹ"
      (VNSHINE) khỏi Tài liệu quỹ. Trang Biểu mẫu đã có cả hai biểu mẫu tương ứng.
    - Công bố thông tin đã dùng sẵn 8 loại của #116 theo đúng thứ tự (ir.types), không đổi."""
    s = rep(s, ".filter(o => o.v === '0' || F.docs.some(x => x.c === +o.v)), docVal", ", docVal")
    s = rep(s, "      const fdN = docs.filter(x => x.sel).length, fdAll = ",
            "      if (S.docCat > 0 && !F.docs.some(x => x.c === S.docCat)) docs.splice(0, docs.length, { c: S.docCat, t: F.docCats[S.docCat], d: l === 'vi' ? 'Tài liệu đang được cập nhật.' : 'This document is being updated.', cat: F.docCats[S.docCat], date: '—', isNew: false, ph: true, sel: false, unsel: false, toggle: () => {} });\n"
            "      const fdN = docs.filter(x => x.sel).length, fdAll = ")
    s = rep(s, "docCount: docs.length,", "docCount: docs.filter(x => !x.ph).length,")
    # biểu mẫu ra khỏi Tài liệu quỹ
    s = rep(s, "date:'14.08.2026',size:'3,2 MB'},\n   {c:9,t:b('Mẫu đăng ký mua/bán chứng chỉ quỹ','Subscription/redemption form'),d:b('Dùng khi giao dịch qua đại lý phân phối.','For transactions through a distributor.'),date:'01.07.2026',size:'240 KB'}\n",
               "date:'14.08.2026',size:'3,2 MB'}\n")
    s = rep(s, "date:'20.05.2026',size:'780 KB'},\n   {c:9,t:b('Bộ tài liệu dành cho thành viên lập quỹ','Authorised participant pack'),d:b('Hợp đồng mẫu, quy trình hoán đổi, biểu mẫu đặt lệnh.','Template agreement, creation/redemption procedure, order forms.'),date:'20.05.2026',size:'1,8 MB'}\n",
               "date:'20.05.2026',size:'780 KB'}\n")
    return s


# ---------------------------------------------------------------- R6-05 · #64 bốn số liệu đầu trang Về chúng tôi
STATS_OLD = "stats:[{v:'+18',u:b('năm','years'),l:b('Năm hoạt động','Years in operation')},{v:'+2.000',u:b('tỷ VNĐ','bn VND'),l:b('Tổng tài sản quản lý','Total assets under management')},{v:'4',u:b('',''),l:b('Sản phẩm quỹ','Fund products')},{v:'88,45',u:b('tỷ VNĐ','bn VND'),l:b('Vốn điều lệ','Charter capital')}],"
STATS_NEW = "stats:[{v:b('+18','18+'),u:b('',''),l:b('năm hoạt động','years of operation')},{v:b('+2.000','2,000+'),u:b('',''),l:b('tỷ VND AUM','bn VND AUM')},{v:'4',u:b('',''),l:b('sản phẩm quỹ','fund products')},{v:b('88,45','88.45'),u:b('tỷ VNĐ','bn VND'),l:b('Vốn điều lệ','Charter capital')}],"

def p_r6_05_stats(s):
    """#64: ba số đầu của Về chúng tôi lấy đúng chuỗi trang chủ (src/parts/th.js, stats):
    VI "+18 năm hoạt động", "+2.000 tỷ VND AUM", "4 sản phẩm quỹ"; EN "18+ years of operation", "2,000+ bn VND AUM", "4 fund products".
    Số thứ tư (vốn điều lệ) giữ, bản EN viết số kiểu Anh "88.45 bn VND". Không đổi số.
    中文: nhãn EN đổi nên bản 中文 hiện chữ EN cho 3 nhãn này tới khi cô Helena duyệt (không thêm khoá PHFM_ZH vì
    trang chủ dùng chung khoá, thêm vào sẽ làm đổi trang chủ 中文)."""
    s = rep(s, STATS_OLD, STATS_NEW)
    return s


# ---------------------------------------------------------------- Ảnh hero mới (bàn giao 30/10, mục 5)
HERO_R6 = {'about_hero': 2, 'acad_hero': 2, 'cr_hero': 1}
HERO_R6_JS = ['phvsf_hero', 'vns_hero', 'member_hero', 'pf_hero', 'adv_hero']

def p_r6_hero(s):
    """8 ảnh hero trang con thay bộ r5_* (ảnh sáng ban ngày, hợp nền hero bản gốc màu A). Ảnh gốc assets/source/generated/r6_*.webp,
    nguồn ghi ở specs/image-sources.json. Đổi khoá theo đúng số chỗ dùng; khung cắt chỉnh ở r6c.css (.r6h-*)."""
    for k, n in HERO_R6.items():
        s = rep(s, '{{ img.r5_%s }}' % k, '{{ img.r6_%s }}' % k, n)
    for k in HERO_R6_JS:
        s = rep(s, 'window.__I.r5_%s' % k, 'window.__I.r6_%s' % k)
    return s


PATCHES6C = [p_r6c_css, p_r6_04_yield, p_r6_04_eyebrow, p_r6_04_notes, p_r6_04_selall, p_r6_04_docs, p_r6_05_stats, p_r6_hero]
