# Vòng 6 (nhóm R6-02, R6-03): sửa link neo và khối Biểu mẫu ở các trang Hướng dẫn, Học viện. Mỗi mục là một hàm vá trong PATCHES6B.
from patches import rep, part


def p_r6_03_css(s):
    """CSS riêng của R6-03 (src/parts/r6b.css), nạp sau r5.css."""
    return rep(s, '</helmet>', '<style>' + part('r6b.css') + '</style></helmet>')


def p_r6_03_step03(s):
    """R6-03 #30: Bước 03 Giao dịch thứ cấp, bản EN và 中文, hiện ô tròn teal đậm "✓" và nhãn "Step 03" / "步驟 03",
    khác bước 01, 02 (ô tròn vàng có số, đường vàng chạy dài). Đổi hai dòng đó theo mẫu bước 01, 02. Bản VI đã đúng."""
    old_badge = '<span style="flex:none;width:44px;height:44px;border-radius:999px;background:var(--espresso);color:var(--ivory);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16px">✓</span>'
    new_badge = '<span style="flex:none;width:44px;height:44px;border-radius:999px;background:var(--gold-amber);color:var(--espresso);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16px">03</span>'
    line = '<span style="flex:1;height:2px;background:linear-gradient(90deg,var(--gold) 0%,var(--sand) 100%)"></span>'
    for lab in ('Step 03', '步驟 03'):
        old_lab = '<span style="font-size:12px;line-height:16px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-ink)">%s</span>' % lab
        s = rep(s, old_badge + '\n                ' + old_lab, new_badge + '\n                ' + line)
    return s


def p_r6_03_data(s):
    """Dữ liệu cho khối Biểu mẫu (renderVals): formsPh.items = 4 biểu mẫu của nhóm đầu ("Quỹ mở PHVSF") ở trang Biểu mẫu;
    r6b.all = chữ link sang trang Biểu mẫu (VI, EN; 中文 dùng tên trang Biểu mẫu có sẵn trong từ điển)."""
    return rep(s, "formsV: { groups: (d.forms.groups || []).map(g => ({ g: g.g, items: g.items })) }",
                  "formsV: { groups: (d.forms.groups || []).map(g => ({ g: g.g, items: g.items })) }, formsPh: { items: ((d.forms.groups || [])[0] || {}).items || [] }, r6b: { all: l === 'vi' ? 'Xem tất cả biểu mẫu' : l === 'en' ? 'View all forms' : d.forms.title }")


FORMS_SEC = '''
    <section id="r6-forms" data-screen-label="Biểu mẫu" style="display:flex;flex-wrap:wrap;gap:32px 64px;padding:64px 0 72px;scroll-margin-top:200px">
      <div style="flex:1 1 220px;max-width:300px">
        <h2 style="margin:0;font-size:32px;line-height:40px;font-weight:700;color:var(--espresso)">{{ d.forms.title }}</h2>
      </div>
      <div style="flex:3 1 480px;min-width:0;display:flex;flex-direction:column;gap:24px">
        <p style="margin:0;font-size:16px;line-height:24px;max-width:62ch">{{ d.forms.lead }}</p>
        <div style="display:flex;flex-direction:column;gap:12px">
          <sc-for list="{{ formsPh.items }}" as="fi" hint-placeholder-count="4">
            <div class="r6b-frow" style="display:flex;align-items:center;justify-content:space-between;gap:12px 24px;flex-wrap:wrap;background:var(--white);border:1px solid var(--sand);border-radius:2px;padding:16px 20px">
              <div style="min-width:0;flex:1 1 280px"><div style="font-size:16px;line-height:24px;font-weight:600;color:var(--espresso)">{{ fi.t }}</div><div style="font-size:14px;line-height:22px;color:var(--muted);margin-top:2px">{{ fi.d }}</div></div>
              <a href="#" data-dl="1" class="th-btn th-teal r6b-dl" style="flex:none">{{ d.forms.dl }} ↓</a>
            </div>
          </sc-for>
        </div>
        <div><a href="#" onClick="{{ go.forms }}" style="cursor:pointer;font-size:15px;font-weight:600">{{ r6b.all }} →</a></div>
      </div>
    </section>
'''

DL_BTN = '<div class="r6b-dlrow"><a href="#" data-dl="1" class="th-btn th-teal r6b-dl">{{ d.forms.dl }} ↓</a></div>'


def p_r6_03_guide_phvsf(s):
    """R6-03 #16 và #81, Hướng dẫn PHVSF (VI/EN/中文):
    - #81: khối Biểu mẫu sau bước 04, trước Đại lý phân phối: lead và 4 biểu mẫu Quỹ mở PHVSF lấy từ d.forms (cùng dữ liệu trang Biểu mẫu),
      nút Tải về, link "Xem tất cả biểu mẫu" sang trang Biểu mẫu (go.forms).
    - #16: nút "Tải về ↓" cho "Phiếu đăng ký mở tài khoản giao dịch chứng chỉ quỹ mở" trong danh sách Hồ sơ Nhà đầu tư cá nhân.
    Nút tải chưa có file: site.js (A05, thêm nhận data-dl) hiện thông báo "Tài liệu đang được cập nhật"."""
    # ---- #81 khối Biểu mẫu: chèn cuối <main>, ngay sau đoạn cuối của bước 04
    for tail in ('Thời gian giao dịch, thời hạn nhận lệnh và các điều kiện liên quan được thực hiện theo Điều lệ Quỹ, Bản cáo bạch và các quy định hiện hành của PHFM.',
                 'Dealing times, order deadlines and related conditions follow the Fund Charter, the Prospectus and PHFM’s current regulations.',
                 '交易時間、委託收件期限及相關條件依基金章程、公開說明書及 PHFM 現行規定辦理。'):
        old = tail + '</p>\n      </div>\n    </section>\n  </main>'
        s = rep(s, old, tail + '</p>\n      </div>\n    </section>' + FORMS_SEC + '  </main>')
    # ---- #16 nút Tải về ở mục đầu danh sách Hồ sơ cá nhân
    ol = '<ol style="margin:0;padding:0 0 0 24px;display:flex;flex-direction:column;gap:12px;font-size:15px;line-height:23px;text-wrap:pretty">'
    for h, li in (('Hồ sơ Nhà đầu tư cá nhân', 'Phiếu đăng ký mở tài khoản giao dịch chứng chỉ quỹ mở.'),
                  ('Documents for individual investors', 'Open-ended fund unit trading account opening form.'),
                  ('個人投資人應備文件', '開放式基金單位交易帳戶開戶申請書。')):
        old = h + '</h3>\n                ' + ol + '\n                  <li style="padding-left:8px">' + li + '</li>'
        new = h + '</h3>\n                ' + ol + '\n                  <li style="padding-left:8px">' + li + DL_BTN + '</li>'
        s = rep(s, old, new)
    return s


def p_r6_03_academy(s):
    """R6-03 #79, Học viện: thẻ "Biểu mẫu" dưới Thuật ngữ đầu tư (cột trái), nút sang trang Biểu mẫu (go.forms).
    Chữ dùng lại d.forms (title, lead) nên VI/EN khớp trang Biểu mẫu, 中文 lấy theo từ điển có sẵn."""
    old = '{{ d.academy.glossAll }} →</x-import></div></div>'
    card = ('\n          <div class="r6b-acard" style="margin-top:48px;background:var(--white);border:1px solid var(--sand);border-radius:2px;padding:28px 32px">'
            '<h3 style="margin:0;font-size:20px;line-height:28px;font-weight:700;color:var(--espresso)">{{ d.forms.title }}</h3>'
            '<p style="margin:8px 0 0;font-size:15px;line-height:23px;color:var(--muted)">{{ d.forms.lead }}</p>'
            '<div style="display:flex;margin-top:20px"><div onClick="{{ go.forms }}" style="display:flex;cursor:pointer"><x-import component-from-global-scope="PHFMDesignSystem_f2e5ca.Button" variant="secondary" hint-size="220px,44px">{{ r6b.all }} →</x-import></div></div></div>')
    return rep(s, old, old + card)


PATCHES6B = [p_r6_03_css, p_r6_03_step03, p_r6_03_data, p_r6_03_guide_phvsf, p_r6_03_academy]
