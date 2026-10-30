# PHFM website · bản Teal (VI/EN) · ghi chú cho dev

File bàn giao: `dist/phfm-website.html` (tạo bằng `python3 src/build.py`) (8 MB). Mọi thứ nằm gọn trong một file: React 18.3.1, font Inter (latin + vietnamese, 300–700) và toàn bộ ảnh WebP. File không gọi CDN hay Google Fonts.

Bản 中文 chưa làm. Nút 中文 vẫn còn, nhưng nội dung sẽ được làm ở vòng sau.

## 1. Đường dẫn trang (A01)

- Mỗi trang có URL riêng dạng `#/vi/<trang>` hoặc `#/en/<trang>`, ví dụ `#/vi/phvsf`, `#/en/careers`.
- Back/Forward, F5 và đổi ngôn ngữ đều giữ đúng trang. `document.title` đổi theo trang.
- Danh sách trang: home, about, funds, phvsf, vnshine, member, portfolio, advisory, ir, news, academy, careers, contact, guidePhvsf, guideVnshine, faq, glossary, forms, terms, privacy.
- Muốn dùng URL dạng `/vi/phvsf` thì sửa 2 hàm `__phfmRoute` và `__phfmSetHash` ở đầu `<head>`, rồi cấu hình rewrite về `index.html`.

## 2. Số liệu quỹ (B01, B02) · cần làm khi nối CMS

- Hiện tại mỗi quỹ có **một** chuỗi NAV minh hoạ, được hàm `fundCalc()` sinh ra.
- Mọi khối lấy số từ chuỗi này nên luôn khớp nhau: hero, bảng hiệu quả, biểu đồ, lịch sử NAV, thông tin giao dịch, danh sách quỹ.
- **Ngày số liệu lấy theo ngày cập nhật dữ liệu, không lấy theo ngày người xem mở trang.**
  - Ngày này là biến `window.PHFM_ASOF`, hiện đặt là `'2026-10-14'`.
  - Khi nối dữ liệu thật, gán `PHFM_ASOF` bằng ngày của dòng NAV mới nhất trong CMS.
  - Tuyệt đối không dùng `new Date()`.
- Cách nối dữ liệu thật: thay phần sinh chuỗi trong `fundCalc()` bằng chuỗi lấy từ CMS (mỗi ngày giao dịch một dòng gồm ngày, NAV/CCQ, chỉ số tham chiếu). Các khối còn lại không phải sửa. Code có ghi chú `DEV:` ở đúng chỗ.
- Mốc PHVSF đang dùng: YTD −6,11%, MTD −1,02%, ngày −0,14%. VN-Index tương ứng: −2,55%, −1,68%, −0,82%. Số "từ khi thành lập" là minh hoạ.
- Dưới mỗi khối số có dòng "Số liệu minh hoạ, cập nhật đến ngày 14/10/2026". **Xoá dòng này khi đã có số thật.**

## 3. Nút tải tài liệu (A05)

- Tài liệu chưa có file nên khi bấm nút tải, trang hiện thông báo "Tài liệu đang được cập nhật. Vui lòng quay lại sau."
- Đoạn này nằm trong script cuối `<body>`, bắt các nút có `aria-label` hoặc chữ "Tải về / Tải xuống / Download / CSV/Excel / (PCF)".
- Khi có file thật: gắn `href` tới file và bỏ khớp regex `DL` cho nút đó.
- Vòng 6 (R6-03): nút "Tải về ↓" mới có thuộc tính `data-dl="1"` (script cũng bắt thuộc tính này, để bản 中文 chữ "下載" cũng hiện thông báo). Nằm ở: mục "Phiếu đăng ký mở tài khoản giao dịch chứng chỉ quỹ mở" trong Hồ sơ Nhà đầu tư cá nhân và khối "Biểu mẫu" (4 biểu mẫu Quỹ mở PHVSF) ở Hướng dẫn PHVSF. Khi có file: bỏ `data-dl`, gắn `href` tới file.
- **[placeholder] file PDF** cho 5 nút này (và cho các biểu mẫu ở trang Biểu mẫu): chưa có file. Danh sách cần PHFM cấp: Phiếu đăng ký mở tài khoản giao dịch chứng chỉ quỹ mở; Phiếu đăng ký mua/bán chứng chỉ quỹ mở; Mẫu thông tin bổ sung dành cho nhà đầu tư tổ chức; Biểu mẫu khai báo FATCA và AML. Dữ liệu 4 biểu mẫu lấy từ `PHFM_DATA.forms.groups[0].items`, nên khi nối CMS khối ở Hướng dẫn PHVSF tự đổi theo trang Biểu mẫu.

## 4. Tìm kiếm (A06)

- Tìm kiếm chạy ngay trên trình duyệt, không cần server.
- Phạm vi tìm: tên trang, bài viết, FAQ, thuật ngữ, biểu mẫu, công bố thông tin, vị trí tuyển dụng. Gõ không dấu vẫn tìm ra.
- Khi nối CMS, dữ liệu tìm kiếm được lấy từ `window.PHFM_DATA`, nên không cần sửa gì thêm.

## 5. Các việc còn để ngỏ (đã thống nhất không xử lý vòng này)

- **Form** (Liên hệ, Quỹ thành viên, Quản lý danh mục, Tư vấn, đăng ký nhận báo cáo): chưa gửi dữ liệu đi đâu (A07). Dev cần nối backend hoặc email.
- **Mục CMS ở Danh sách quỹ**: khung "Ghi chú demo" đã gỡ khỏi giao diện (A16). Phần quản lý nội dung quỹ do dev dựng.
- **Bản đồ trang Liên hệ** là hình vẽ (A17). Có thể thay bằng Google Maps embed.
- **Số tài khoản nhận tiền** ở Hướng dẫn PHVSF cần pháp chế/vận hành xác nhận (B03).
- **Hồ sơ** còn ghi "CMND" (B05). **Bài MSCI** cần ghi nguồn số liệu (B06).

## 6. Logo và icon

- Toàn bộ logo đối tác (kể cả BIDV, EY, VNDIRECT, Finhay, Mirae Asset, HSC, Vietcap) đã nhúng trong file, lấy từ folder Partner của PHFM. Không còn link ngoài.
- Footer có 5 icon: LinkedIn, Facebook, YouTube, Instagram, Zalo, cùng màu teal #0B6274.

## 6b. Tài liệu quỹ (PHVSF, VNSHINE)

- Có bộ lọc Loại tài liệu và Năm, ô chọn từng dòng, "Chọn tất cả", nút "Tải tài liệu đã chọn (n)" và nút tải riêng từng file.
- Chưa có file thật nên các nút tải hiện thông báo "đang cập nhật". Khi nối CMS: mỗi tài liệu cần `url`; nút tải nhiều file nên gọi một API nén ZIP ở server (trình duyệt không tải được nhiều file một lần một cách ổn định).
- Logic nằm ở `fdDl`, `fdToggleAll` trong class `Component`.

## 6c. Nút Công cụ nổi

- Nút "Công cụ" ở góc phải dưới mở 3 công cụ: Ước tính đầu tư định kỳ, Trắc nghiệm khẩu vị rủi ro, Bắt đầu từ con số 0. Kết quả chỉ mang tính minh hoạ, đã ghi rõ trong công cụ.
- Code nằm trong script cuối `<body>` (id `pt-fab`).

## 6d. Chờ pháp chế và việc còn thiếu (vòng 6)

Chữ mới áp ngay ở VI, EN viết tương đương, 中文 không tự dịch (cô Helena duyệt). Mọi chữ dưới đây chờ pháp chế trước go-live.

- **"Tỷ suất Lợi nhuận Cổ đông"** (VI) thay "Lợi suất Cổ đông" toàn site (Q5, issue #9). EN giữ "Shareholder Yield".
- **"Quỹ ETF đầu tiên tại Việt Nam được xây dựng theo Chiến lược Tỷ suất Lợi nhuận Cổ đông - Shareholder Yield"** (hero và thẻ VNSHINE, VI/EN): giữ theo ý Rin (Q6). "Đầu tiên" là tuyên bố cần pháp chế xác nhận; nếu không xác nhận được thì đổi sang "một trong những quỹ ETF tiên phong" (brand-rules: không viết như độc quyền).
- Nhãn hero PHVSF "QUỸ MỞ" / "OPEN-ENDED FUND" (R6-04).
- Dòng "Tài liệu đang được cập nhật." / "This document is being updated." trong Tài liệu quỹ khi loại tài liệu chưa có file (R6-04).
- Dòng "Số liệu minh hoạ, cập nhật đến ngày…" giữ đến khi có số thật từ CMS (Q7), chữ nhỏ in nghiêng.
- **Tài liệu quỹ (PHVSF, VNSHINE)**: 9 loại theo bình luận #134. Chưa có file: Factsheets, Thông tin quỹ, Giấy phép (cả hai quỹ), Khác (PHVSF), Báo cáo tài chính (VNSHINE). Dev nối `url` từng tài liệu khi có file. Biểu mẫu nằm ở trang Biểu mẫu, không còn trong Tài liệu quỹ.
- **Công bố thông tin**: 8 loại theo bình luận #116 (Thông báo quỹ, Điều lệ quỹ, Bản cáo bạch, Báo cáo tài chính, Báo cáo hoạt động tháng, Báo cáo NAV ngày/tuần, Biểu mẫu, Factsheet). Hai loại Biểu mẫu và Factsheet chưa có tài liệu mẫu.
- **Chờ cô Helena (中文)**: nhãn hero PHVSF "OPEN-ENDED FUND" (đang hiện EN), dòng "Tài liệu đang được cập nhật" (hiện EN), 9 tên loại tài liệu và "Tỷ suất Lợi nhuận Cổ đông" (zh dùng "股東收益率", không đổi).
- **Về chúng tôi, bốn số liệu đầu (R6-05, #64)**: ba số đầu lấy đúng chuỗi trang chủ (VI "+18 năm hoạt động", "+2.000 tỷ VND AUM", "4 sản phẩm quỹ"; EN "18+ years of operation", "2,000+ bn VND AUM", "4 fund products"), số vốn điều lệ EN viết "88.45 bn VND". Bản 中文: ba nhãn này đang hiện chữ EN, chờ cô Helena. Tên EN bốn giá trị Tân · Tốc · Thực · Giản: chờ Rin gửi (Q4).
- Nội dung từ phfm.vn cho PHVSF (`product-service/performance` và `overview` bản EN): Rin chưa gửi (Q9, Q10). Giữ như hiện tại.

## 7. Ảnh (A11)

- Ảnh mới được nén WebP chất lượng 84. Ảnh hero và ảnh dải ngang rộng 1920px. Ảnh thẻ và ảnh bài viết rộng 960px, khoảng 2 lần khung hiển thị lớn nhất, nên vẫn nét trên màn hình retina.
- Mỗi ảnh chỉ nhúng một lần, lưu trong `window.__I`.
- Khi deploy, có thể tách các ảnh này ra file riêng để tận dụng cache. Chất lượng không đổi.

## 8. Ghi chú kỹ thuật

- Trang render bằng runtime "dc" (template + class `Component`).
  - Template nằm trong `<script type="text/x-dc-template" id="dc-tpl">`.
  - Dữ liệu nằm ở `window.PHFM_DATA` (song ngữ dạng `{vi, en}`).
- Một số script cũ chỉnh DOM sau khi render: chỉnh mobile, căn chữ, hiệu ứng hiện dần.
  - Trang chủ (`[data-hm]`) và footer (`.ft`) được loại khỏi các script này để giữ đúng bản thiết kế Teal Vanguard.
- Màu theo đúng bảng Teal Vanguard của trang chủ: teal `#0B6274`, teal đậm `#0A3440`, vàng nút `#E9C46A`, vàng logo `#C0962D`, màu tăng `#15897D`, mist `#E3EEF0`.
- Màu theo khối của trang con (sau vòng 5, phương án A "chéo như trang chủ"; CSS ở `src/parts/r5.css`, nạp sau `r4.css`):

| Khối | Nền | Chữ / nhấn |
|---|---|---|
| Hero `.dh` / `.fh` | Teal đậm `#0A3440` bên trái, mảng chéo teal `#0B6274` bên phải (skewX -16deg, mốc 55%, như `.hm-skew`), vòng vàng `#E9C46A` ở góc | Chữ trắng, nhãn vàng. Ảnh trong khung bo 20px trên mảng chéo (trang quỹ: ảnh cắt theo cạnh chéo, mờ 60%). Hero hai cột (Quỹ thành viên, Quản lý danh mục, Tư vấn, Tuyển dụng, từ 761px) giữ mảng chéo và vòng vàng; dưới 761px thành dải teal chính dưới chữ. Trang quỹ xếp dọc dưới 1100px (JS `wide` = từ 1100px): thẻ giá bọc trong `.r5-fhc` có dải teal và bản sao ảnh, bắt đầu dưới hàng nút. `.hero-sub` là `position:relative; overflow:hidden` cho mọi hero |
| Thanh mục con `.nm-sbar` | Mist `#E3EEF0`, viền dưới `#D8E7EA` | Chữ teal `#0B6274`, hover/focus chữ `#0A3440` và gạch vàng 3px |
| Lịch sử hình thành `.ab-j` | Mist `#E3EEF0` | Trục và mốc vàng `#E9C46A`; năm giai đoạn teal 28-32px, tên giai đoạn `#0A3440` 18px, năm mốc teal và sự kiện `#16262B` 15px |
| Quỹ phù hợp `.fit` | Mist `#E3EEF0`, ô tích trắng | Chữ `#16262B`, tiêu đề `#0A3440` |
| Ô chênh lệch giá/NAV `.pd-cell` | Teal `#0B6274`, vạch vàng 3px phía trên | Số trắng, nhãn `#D8E7EA` |
| Section thân trang | Xen kẽ trắng `#FFFFFF` và mist `#E3EEF0`, không hai section liền nhau cùng nền (hero teal đậm, thanh mục con mist, section đầu trắng). Chân trang mist có viền vàng 4px, không tính vào quy tắc | Thẻ trong section giữ nền trắng có viền `#D8E7EA`. Section chỉ rộng 1280px được phủ nền kín ngang bằng `box-shadow: 0 0 0 100vmax` và `clip-path: inset(0 -100vmax)` (viết theo id hoặc class trang trong `r5.css`) |
| Hero trang Hướng dẫn `.nm-ghero` | Mist `#E3EEF0` (trước đây VNSHINE dùng `#EEF3F4`, ngoài bảng màu) | |

- Thứ tự nền từng trang: xem bảng trong PR vòng 5 (R5-01) và `qa/r5sections.js` (chạy lại sau mỗi lần thêm section: phải không còn cờ `=SAME`).
- Chữ trang con (vòng 5): đoạn căn trái, `text-wrap:pretty`; tiêu đề `text-wrap:balance`. Script căn đều `okBlock`/`fit` đã tắt trong `<main>` và bài đọc `#rd5` (không còn word-spacing/letter-spacing âm). Trang chủ không đổi. `node qa/r5spacing.js` quét lại.
- Menu header: gạch "mục đang chọn" có class `th-act`; ở mục đó gạch hover `::after` bị ẩn, mỗi mục chỉ một gạch vàng. `node qa/r5menu.js` kiểm các trạng thái ở 1440 và 1024.
- Teal đậm `#0A3440` dùng cho: hero các trang con, avatar ban điều hành, khối kêu gọi cuối trang (gradient trên ảnh), dải trên cùng và nút Công cụ.

## 9. Chỉnh sửa nội dung sau này

- Chữ VI/EN các trang con: sửa ở artifact "Nội dung website PHFM". Bản build đọc phần đã sửa từ `edits.json` và áp lên `PHFM_DATA` lúc tải trang (đoạn script ngay sau dữ liệu). Khi nối CMS, phần này thay bằng dữ liệu CMS.
- Bố cục, màu, khoảng cách: sửa trên canvas "Website PHFM - Teal Vanguard · Trang con". Claude so canvas với bản gốc và đưa thay đổi vào code.

---

## Danh sách thay đổi

Xem `specs/changelog.md`.
