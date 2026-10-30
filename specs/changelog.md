# Nhật ký thay đổi website PHFM

Cột: Trang | Thay đổi | Lý do. Vòng mới nối thêm ở cuối bảng.

## Vòng 1–3 (21–29/10/2026)


| Trang | Thay đổi | Lý do |
|---|---|---|
| Trang chủ | Thay bằng thiết kế Teal Vanguard (desktop + mobile) | Theo yêu cầu |
| Header mọi trang | Logo ảnh, hotline (028) 5413 7991, menu đậm 600 với gạch chân vàng, icon tìm kiếm/menu mới | Đồng bộ với trang chủ |
| Footer mọi trang | Footer mới theo trang chủ, link mạng xã hội đúng, bỏ gạch thừa; vẫn giữ dòng cảnh báo rủi ro | A04, A13, tuân thủ |
| Toàn site | Bảng màu teal: bỏ nền kem/vàng nhạt, tiêu đề một màu, nút vàng thống nhất #E9C46A, đường VN-Index đổi sang mist, màu tăng #15897D | C01 |
| Toàn site | URL riêng cho từng trang, tiêu đề tab theo trang | A01 |
| Toàn site | Ô tìm kiếm hoạt động | A06 |
| Toàn site | Bỏ font không dùng, chỉ nhúng Inter; sửa link font hỏng | A08, A12 |
| Toàn site | File từ 12,9 MB còn 8 MB, ảnh không giảm độ nét | A11 |
| Toàn site (mobile) | Đoạn văn căn trái, hết hở chữ | A10 |
| PHVSF, VNSHINE, Danh sách quỹ | Một nguồn số cho mọi khối, ngày cố định theo ngày dữ liệu, ghi rõ "số liệu minh hoạ" | B01, B02 |
| PHVSF, VNSHINE | Ô chọn ngày hiển thị dd/mm/yyyy | A09 |
| Biểu mẫu, Tài liệu quỹ, Công bố thông tin | Nút tải hiện thông báo "đang cập nhật" | A05 |
| VNSHINE, Góc nhìn (EN) | Dịch nốt chữ tiếng Việt còn sót | A14 |
| Danh sách quỹ | Gỡ khung "Ghi chú demo · Mục CMS" | A16 |
| Hướng dẫn VNSHINE (mobile) | Khối "Bắt đầu đầu tư" có lại nền | A02 |
| Học viện | Ví dụ tính lãi có ghi chú "ví dụ minh hoạ" | B04 |
| Về chúng tôi, PHVSF, VNSHINE, Quản lý danh mục, Tư vấn, Học viện, Tuyển dụng, Góc nhìn, 2 trang Hướng dẫn | Thay 18 ảnh tông be/nâu bằng ảnh teal đã duyệt (1 ảnh mới tạo cho thẻ Tuyển dụng 01) | C02 |
| **Vòng 3 (29/10)** | | |
| Trang con | Phối thêm teal đậm #0A3440 theo style trang chủ: hero, thanh mục con, khối nhấn | Rin góp ý |
| Header | Menu chỉ còn 1 gạch chân vàng khi rê chuột | Trước đây hiện 2 gạch |
| Toàn site | Thêm lại nút Công cụ nổi (ước tính đầu tư định kỳ, trắc nghiệm khẩu vị rủi ro) | Bị mất ở bản trước |
| PHVSF | Khối "Quỹ phù hợp" làm lại; ô NAV đổi "Quỹ" thành "PHVSF" | Rin góp ý |
| PHVSF, VNSHINE, Về chúng tôi | Bấm cả thẻ ban điều hành/lãnh đạo để xem giới thiệu, bỏ "Tìm hiểu thêm" | Rin góp ý |
| PHVSF, VNSHINE | Tài liệu quỹ: lọc loại, tick chọn, tải nhiều, tải lẻ; ô chọn ngày không còn tràn chữ | Rin góp ý |
| VNSHINE | Hero ảnh mới (Higgsfield); "Chỉ số tham chiếu" thành "VNSHINE Index"; ô chênh lệch giá/NAV đổi màu; logo thành viên lập quỹ mới | Rin góp ý |
| Tư vấn đầu tư | Hero ảnh riêng, không trùng thẻ Tuyển dụng 02 | Mỗi chỗ một ảnh |
| Góc nhìn | Ảnh bìa bài MSCI và bài Luân chuyển ngành thay ảnh nền kem | Rin chọn thay |
| Về chúng tôi, VNSHINE, Hướng dẫn VNSHINE | Logo đối tác từ folder Partner, nhúng vào file | A03 |
| Footer | Thêm icon Instagram, Zalo cùng kiểu 3 icon cũ | A04 |

## Vòng 4

| Trang | Thay đổi | Lý do |
|---|---|---|
| Toàn site | Thêm khung vòng 4: `src/patches4.py`, `src/parts/r4.css` (nạp sau r3.css). Giao diện không đổi, build giống hệt trước | Chuẩn bị cho R4-01 đến R4-05 |
| Về chúng tôi | Giá trị cốt lõi: hiện chữ Hán 新 速 實 簡 trên tên giá trị (Noto Serif TC, 60px desktop / 56px mobile, vàng logo `#C0962D`); font subset 4 chữ nhúng base64 (2 KB) | Dữ liệu `values[].c` đã có nhưng template chưa hiện |
| Về chúng tôi, PHVSF, VNSHINE, Quỹ thành viên, Danh mục đầu tư, Tư vấn, Học viện, Tuyển dụng | Thu chiều cao hero: bỏ `min-height:min(900px, ...)`. Desktop ≥1280 cao tối thiểu 560px (trang quỹ 600px), 768–1279 480px, mobile không đặt; khoảng trên/dưới 64px (mobile 32px/40px). Ảnh hero trang dịch vụ đổi khung cắt từ tỉ lệ 4/5 sang 10/9 (mobile 16/10), ảnh giữ nguyên; ảnh Quỹ thành viên cắt về bên trái (`object-position:20% 30%`) để desktop chỉ còn anh tư vấn trẻ; mobile Về chúng tôi ảnh dưới chữ cao 320px; mobile khoảng cách breadcrumb → nội dung và chữ → ảnh thu còn 28px. Khoảng 64px chỉ áp từ 1280px; hero Học viện layout hẹp dùng chung `.hero-in`; layout hẹp (About, Học viện, dưới 1400px) đánh dấu `.hero-nar`, giữ padding cũ ở 1280–1399. Luật chung ở `.hero-sub` / `.hero-in` / `.hero-pic` trong `r4.css` | Hero cao 775–795px đẩy nội dung xuống dưới màn hình đầu; cao hero 1440 nay 560–625px |
| Về chúng tôi | Hero chuyển sang nền teal đậm `#0A3440`, chữ trắng, ảnh `r5_about_hero` bên phải (kiểu hero trang con, class `dh`); lớp mờ chuyển từ trắng sang teal, rộng hơn để chữ trên ảnh đạt tương phản ≥ 4.5:1. Chiều cao không tăng (1440: 563px, 1366–1024: 951px VI) | Cùng kiểu với hero các trang con khác (R4-09) |
| PHVSF, VNSHINE, Quỹ thành viên, Danh mục, Tư vấn, Học viện, Tuyển dụng, 2 trang Hướng dẫn | Thay ảnh hero theo từng vị trí bằng bộ stock `r5_*` (H2–H10). Khung cắt: ảnh quỹ 75% 50% (mobile 80%), Hướng dẫn PHVSF 85% (mobile 88%), Hướng dẫn VNSHINE 75% (mobile 80%), ảnh dịch vụ theo chủ thể. Hero Học viện đổi lớp mờ sang teal rộng hơn vì ảnh mới sáng. Alt hai trang Hướng dẫn đổi theo nội dung ảnh (VI/EN/中文). Hero Hướng dẫn (≥ 701px): lớp mờ trắng rộng hơn (đặc đến 55%, hết ở 82%) và tiêu đề tối đa `min(720px, 60vw)` vì ảnh mới tối, chữ tối trên ảnh chỉ 1,3–2,3:1; hero cao thêm 56px. Khung cắt mobile của hai ảnh Hướng dẫn thêm `!important` để thắng luật cũ ≤ 700px | Bớt ảnh AI quá lố, thêm ảnh tài chính theo giờ xanh khớp trang chủ (#14) |
| Góc nhìn & Tin tức | Thay 10 ảnh bài viết (N1–N10) bằng `r5_nw_*`; ba ảnh tin sự kiện giữ nguyên | Ảnh báo tài chính ban ngày, mỗi bài một ảnh (#14) |
| Toàn site | Xoá 16 ảnh cũ không còn dùng khỏi `assets/img` (ab_hero, advisor, team, nw_city, pk_I05, pk_I07, pk_I12–I15, pk_I17, pk_I18, r3_adv_hero, r3_vns_hero, r3_nw_msci, r3_nw_rot). Thêm `qa/check-images.js` kiểm từng vị trí hiện đúng khoá ảnh và không trùng khoá | Dọn ảnh thừa sau R4-09 |
| VNSHINE, PHVSF | Ô giá ở hero: hàng chỉ số (Giá đóng cửa · NAV/CCQ · Ngày) thành lưới `.px-row`, số 28px, nhãn và đơn vị 12px, đơn vị nằm dưới số; không còn `flex-wrap` đẩy Ngày xuống hàng. Desktop VNSHINE 3 cột cách đều, PHVSF 2 cột; mobile VNSHINE Giá + NAV một hàng, Ngày hàng dưới thẳng cột, PHVSF mỗi chỉ số một hàng. Bảng hiệu quả giữ nguyên, kể cả cột 3 tháng của VNSHINE (ô trống hiện "—"; Rin quyết giữ). Số liệu không đổi | Bỏ khoảng trống thừa trong ô giá (#5) |
| Về chúng tôi | Lịch sử hình thành (`#ab-journey`): nền teal đậm `#0A3440`, ba giai đoạn thành ba cột (năm lớn vàng `#E9C46A` 44px, tên giai đoạn trắng, danh sách năm/sự kiện chữ trắng và mist), trục ngang vàng nối ba điểm mốc. Bỏ khung thẻ trắng cao bằng nhau. Từ 1024px cột 3 (nhiều mốc nhất) rộng gấp 1,6 lần để ba cột cao gần bằng nhau (chênh ~135px ở 1440 VI). Dưới 1024px: một cột, trục dọc bên trái. Dữ liệu `phases` giữ nguyên (10 mốc, chữ VI/EN/中文 không đổi) | Khung trắng kéo cao bằng nhau để trống nhiều dưới cột 1 và 2 (#4) |
