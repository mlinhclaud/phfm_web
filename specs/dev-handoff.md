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
- Teal đậm `#0A3440` dùng cho: hero các trang con, thanh mục con dính dưới header, khối "Quỹ phù hợp", ô chênh lệch giá/NAV, avatar ban điều hành.

## 9. Chỉnh sửa nội dung sau này

- Chữ VI/EN các trang con: sửa ở artifact "Nội dung website PHFM". Bản build đọc phần đã sửa từ `edits.json` và áp lên `PHFM_DATA` lúc tải trang (đoạn script ngay sau dữ liệu). Khi nối CMS, phần này thay bằng dữ liệu CMS.
- Bố cục, màu, khoảng cách: sửa trên canvas "Website PHFM - Teal Vanguard · Trang con". Claude so canvas với bản gốc và đưa thay đổi vào code.

---

## Danh sách thay đổi

Xem `specs/changelog.md`.
