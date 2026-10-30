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
| Về chúng tôi (中文) | Lịch sử hình thành: mốc 2026 cuối đổi 總管理資產突破 12,000 億越南盾 thành 20,000 億 (khớp 2.000 tỷ VNĐ ở bản VI/EN); tên giai đoạn 2 "Growth phase" dịch thành 成長. Chữ Trung mới cần cô Helena duyệt. Mốc khác đã đối chiếu, khớp | Sửa #27 |
| VNSHINE, PHVSF | Ô giá ở hero: hàng chỉ số (Giá đóng cửa · NAV/CCQ · Ngày) thành lưới `.px-row`, số 28px, nhãn và đơn vị 12px, đơn vị nằm dưới số; không còn `flex-wrap` đẩy Ngày xuống hàng. Desktop VNSHINE 3 cột cách đều, PHVSF 2 cột; mobile VNSHINE Giá + NAV một hàng, Ngày hàng dưới thẳng cột, PHVSF mỗi chỉ số một hàng. Bảng hiệu quả giữ nguyên, kể cả cột 3 tháng của VNSHINE (ô trống hiện "—"; Rin quyết giữ). Số liệu không đổi | Bỏ khoảng trống thừa trong ô giá (#5) |
| Về chúng tôi | Lịch sử hình thành (`#ab-journey`): nền teal đậm `#0A3440`, ba giai đoạn thành ba cột (năm lớn vàng `#E9C46A` 44px, tên giai đoạn trắng, danh sách năm/sự kiện chữ trắng và mist), trục ngang vàng nối ba điểm mốc. Bỏ khung thẻ trắng cao bằng nhau. Từ 1024px cột 3 (nhiều mốc nhất) rộng gấp 1,6 lần để ba cột cao gần bằng nhau (chênh ~135px ở 1440 VI). Dưới 1024px: một cột, trục dọc bên trái. Dữ liệu `phases` giữ nguyên (10 mốc, chữ VI/EN/中文 không đổi) | Khung trắng kéo cao bằng nhau để trống nhiều dưới cột 1 và 2 (#4) |
| QA (không đổi giao diện) | `qa/qa.js`: `NaN` tách riêng, khớp đúng từ `\bNaN\b` và phân biệt hoa thường (cả trong chữ lẫn thuộc tính title/alt/placeholder/aria-label); các mẫu undefined, `{{`, null, `[object`, Lorem giữ nguyên. Cột `bad` các trang EN từ 1–7 về 0 | "NaN" khớp "fi**nan**cial" làm `bad` báo nhầm (#18) |
| Về chúng tôi | Lưới Giá trị cốt lõi (`#ab-values`) ≤760px: bỏ padding 18px thừa của luật mobile cũ `main section>div` ở riêng khối này (`r4.css`). Lưới khớp mép ô, viền đủ bốn phía như desktop (390: lưới 18→372, ô 19→372; trước đây ô 37→354, mất viền phải). Desktop không đổi | Lưới thụt 2 lần, viền trên thừa ra mép phải (#17) |
| Về chúng tôi, Học viện | Hero dùng layout rộng (ảnh bên phải) từ 1280px thay vì 1400px (`heroNarrow = vw < 1280`, hàm `p_fix20`). Hero 1280–1399 còn 560px (VI, EN, 中文), trước đây 840–1133px; 1024–1279 vẫn layout hẹp, không đổi; mobile không đổi. Chữ trắng trên ảnh tương phản tối thiểu khoảng 7:1 ở 1280–1440. Hero Học viện 1280–1399 thêm `text-wrap:pretty` (class `.ac-h1`) để chữ "tư" không bị xuống dòng một mình | Plan R4-01 ghi "≥1280: 560px", nhưng laptop 1280 và 1366 thấy hero cao ~1000px (#20) |
| VNSHINE, PHVSF | Mô tả hero trang quỹ bản EN và 中文 căn trái, khoảng cách chữ về mặc định, hai dòng cân nhau (EN VNSHINE trước đây dính chữ do word-spacing -0.2em, 中文 giãn khoảng trắng trong "Shareholder Yield", EN PHVSF giãn khoảng trắng dòng đầu). Bản VI không đổi | Sửa #24 |

## Vòng 5

| Trang | Thay đổi | Lý do |
|---|---|---|
| Toàn site (19 trang con) | Thêm `src/patches5.py`, `src/parts/r5.css` (nạp sau `r4.css`). Trang chủ và chân trang so từng điểm ảnh với bản main (VI/EN, 1440/390): 0 điểm khác | Khung vòng 5 (R5-01) |
| Về chúng tôi, PHVSF, VNSHINE, Quỹ thành viên, Quản lý danh mục, Tư vấn, Học viện, Tuyển dụng | Hero phương án A "chéo như trang chủ": nền teal đậm `#0A3440` trái, mảng chéo teal `#0B6274` phải (skewX -16deg, mốc 55%), vòng vàng góc phải. Ảnh trong khung bo 20px có bóng (trang quỹ: ảnh cắt theo cạnh chéo, mờ 60%, bỏ gradient teal đậm). Hero hai cột (Quỹ thành viên, Quản lý danh mục, Tư vấn, Tuyển dụng) giữ mảng chéo và vòng vàng từ 761px trở lên. Khi bố cục xếp dọc (Về chúng tôi và Học viện dưới 1400px, trang khác dưới 761px): ảnh nằm dưới chữ trên dải teal chính cắt chéo. Trang quỹ xếp dọc dưới 1100px: thẻ giá bọc trong dải teal có ảnh, dải bắt đầu dưới hàng nút "Tải Bản cáo bạch" (không còn dải cao cố định 480px cắt ngang nút); chữ hero nằm trên nền `#0A3440` phẳng. Cỡ chữ, dòng, độ đậm, giãn chữ của nhãn, h1, nút, breadcrumb giữ như bản main (đo ở 1440, 1024, 390) | Rin chọn phương án A |
| Về chúng tôi, PHVSF, VNSHINE | Thanh mục con đổi từ teal đậm sang mist `#E3EEF0`, chữ teal, gạch vàng 3px khi rê chuột hoặc focus | Rin chọn A; mist để hero teal đậm, thanh mục con, section đầu (trắng) là ba màu khác nhau |
| Về chúng tôi | Lịch sử hình thành: nền mist `#E3EEF0`, trục vàng giữ. Cỡ chữ nhỏ lại: năm giai đoạn 28-32px (trước 40-44px), tên giai đoạn 18px (trước 20px), năm mốc và sự kiện 15px (trước 16px); cột năm 96px và `white-space:nowrap` để "2012 - 2013" nằm một dòng ở 1440, 1280, 1024, 768, 390, 360 (VI/EN/中文; đo bằng `qa/r5year.js`) | Rin: chữ to quá |
| PHVSF | Khối "Quỹ phù hợp": nền mist, ô tích trắng, chữ `#16262B`. Tiêu đề khối không còn letter-spacing âm | Rin chọn A |
| VNSHINE | Ô chênh lệch giá/NAV: teal chính `#0B6274`, số trắng, vạch vàng phía trên | Rin chọn A |
| Về chúng tôi, PHVSF, VNSHINE, Công bố thông tin, Góc nhìn & Tin tức, Học viện, Hỏi đáp, Thuật ngữ, 2 trang Hướng dẫn | Xen kẽ nền section trắng ↔ mist, không còn hai section liền nhau cùng nền (trước: about 3 cặp, PHVSF 3, VNSHINE 2, IR 1, Góc nhìn 4, Học viện 2, Hướng dẫn PHVSF 4, Hướng dẫn VNSHINE 4, Hỏi đáp 2, Thuật ngữ 2). Hero Hướng dẫn VNSHINE `#EEF3F4` (ngoài bảng màu) đổi sang mist. Chân trang (mist, viền vàng 4px) không tính | Rin: không hai section liền nhau cùng màu nền |
| Header (mọi trang trừ trang chủ) | Menu chỉ còn một gạch vàng mỗi mục. Nguyên nhân: gạch "mục đang chọn" là `<div style="...height:2px...">`, trình duyệt ghi lại thành `height: 2px` (có dấu cách) nên luật `[style*="height:2px"]` ở vòng 3 không khớp: gạch active (vàng đậm, `bottom:-1px`) hiện cùng gạch hover (`::after`, vàng sáng, `bottom:4px`). Sửa: class `th-act` cho gạch active, ẩn gạch hover ở mục đó, đặt cùng vị trí và màu; vòng focus bàn phím đổi từ vòng đen sát gạch sang vòng teal cách chữ 4px. Trang chủ không có mục đang chọn nên không đổi | Rin báo menu vẫn hiện 2 gạch |
| Trang con (VI/EN/中文) | Bỏ ép chữ: đoạn căn trái (không justify), `text-wrap:pretty`, tiêu đề `text-wrap:balance`; tắt script căn đều `okBlock`/`fit` trong `<main>` và bài đọc (trước đây word-spacing tới -3,2px, letter-spacing tới -0,34px, ví dụ mô tả hero Tư vấn đầu tư). Trang chủ và chân trang không đổi | Rin: chữ dính sát |
| Tuyển dụng | `.hero-sub` là `position:relative; overflow:hidden` cho mọi hero (careers trước đây `position:static` nên mảng chéo và vòng vàng bám khung trang: phủ header, che thẻ "Văn hoá", dải teal ở 390 tràn quá đáy hero). Ảnh hero vào khung bo 20px có bóng như ba trang dịch vụ | Sửa review PR #36 |
| Hướng dẫn đầu tư (VNSHINE, PHVSF) | Số bước 01-04 đổi từ `#C0962D` sang vàng đậm `#7D5F1A`: 5,04:1 trên mist, 5,96:1 trên trắng (trước 2,32:1 trên mist) | Tương phản chữ lớn trên nền sáng |
| Menu header | Vòng focus bàn phím đổi sang teal đậm `#0A3440` (13,3:1 trên nền trắng) | Brief: viền focus teal đậm trên nền sáng |
| Công cụ QA | `qa.js`, `shot.js`, `insp.js` nhận biến `HTML`. Thêm `r5sections.js` (thứ tự nền section), `r5menu.js` (gạch menu), `r5spacing.js` (chữ ép), `r5hero.js` + `r5herocmp.py` (cỡ chữ hero), `r5contrast.js` (tương phản), `r5pixdiff.py` (so điểm ảnh), `survey-teal.js`, `r5bgprobe.js`, `r5shots.js` | Kiểm vòng 5 |

## Vòng 6

| Trang | Thay đổi | Lý do |
|---|---|---|
| Toàn site (19 trang con) | R6-01: bố cục trang con về bản gốc (build `3131e7e`), giữ màu A. Thêm `src/patches6.py` và `src/parts/r6.css` (nạp sau `r5.css`). Cách làm: gỡ trực tiếp trong `patches4.py`, `r4.css`, `r5.css` các khối R4-01, R4-03, R4-04, `p_fix20`, cỡ chữ Lịch sử hình thành vòng 5; chỗ cần giữ màu A viết lại trong `r6.css`. So hình học 19 trang ở 1440/1024/390 (VI, EN mẫu): lệch ≤2px so với bản gốc cộng các sửa phải giữ, chỉ còn khung ảnh hero (màu A) khác. Trang chủ và chân trang 0 điểm ảnh khác so với main | Rin chọn "bố cục, cỡ chữ, khoảng cách về bản gốc, màu theo A, giữ sửa lỗi" (`plans/round-6.md`, R6-01, #45) |
| Về chúng tôi, PHVSF, VNSHINE, Quỹ thành viên, Danh mục, Tư vấn, Học viện, Tuyển dụng | Hero về chiều cao gốc: `min-height:min(900px,...)` và padding gốc (775px, Quỹ thành viên/Danh mục/Tư vấn 795px ở 1440), ảnh dịch vụ khung 4/5, khối ảnh About mobile 420px, đoạn mô tả không bị hẹp 500px. Mảng chéo, vòng vàng, khung ảnh bo góc của màu A giữ nguyên (vị trí tuyệt đối, không đổi kích thước khối) | Gỡ R4-01 |
| Về chúng tôi, Học viện | Layout hẹp (ảnh dưới chữ) lại là dưới 1400px (gỡ `p_fix20`). Ở 1280–1399px hero lại cao 950–1074px như bản gốc (lỗi #20 quay lại, theo ý Rin) | Gỡ #20 theo plan R6-01 |
| Về chúng tôi | Lịch sử hình thành về khung thẻ gốc: 3 thẻ trắng cao bằng nhau, trục ngang vàng, cỡ chữ gốc (nhãn giai đoạn 14px, tên 22px, năm mốc và sự kiện 15px). Nền mist, chữ `#0A3440`/`#7D5F1A`/`#16262B` (tương phản thấp nhất 5,96:1). Cột năm "2012 - 2013" xuống dòng như bản gốc | Gỡ R4-03 và cỡ chữ vòng 5; Rin chọn "về bản gốc, màu mới" (Q3) |
| VNSHINE, PHVSF | Ô giá về hàng `flex-wrap` gốc (Giá đóng cửa, NAV/CCQ, Ngày), gỡ lưới `.px-row`. Cột 3 tháng và ô "—" giữ như bản gốc | Gỡ R4-04 |
| Hướng dẫn PHVSF, Hướng dẫn VNSHINE | Hero về 345px và 327px (1440), bỏ `max-width` tiêu đề. Lớp mờ trắng kéo dài hơn (đến 100% thay vì 82%) vì tiêu đề một dòng chạy dài hơn lên vùng ảnh mới tối hơn: chữ lớn đạt tối thiểu 3:1 (đo 1440/1024/768/390, VI/EN) | Gỡ R4-09 56px nhưng giữ tương phản |
| Trang quỹ (dưới 1100px) | Dải teal chính và ảnh sau thẻ giá là phần tử tuyệt đối (`.r5-fhc::before`), không còn padding/margin âm làm hero cao hơn gốc. Thẻ giá: bỏ viền 1px và bóng thừa do khung bọc `.r5-fhc` trúng luật `r3.css` theo vị trí; hết lệch lề trong 20px thành 16px ở 390 | Hình học về gốc; sửa lỗi lộ ra khi gỡ |
| Hướng dẫn PHVSF, VNSHINE (≤760px) | Nền xen kẽ của bước chuyển sang `::before` rộng đúng khổ màn hình. Section không còn màu nền nên script mobile cũ không coi là thẻ: hết thụt gấp đôi (36px thay vì 18px), bước 1 PHVSF hết cao thêm 254px | Hình học về gốc |
| VNSHINE | Ô chênh lệch giá/NAV: vạch vàng trên là `box-shadow inset` thay cho `border-top` (không cộng thêm 3px chiều cao) | Hình học về gốc, màu A giữ |
| Về chúng tôi, PHVSF, VNSHINE | Thanh mục con mist: đường kẻ dưới là `box-shadow inset` thay cho `border-bottom` (không cộng thêm 1px) | Hình học về gốc, màu A giữ |
| Công bố thông tin, Góc nhìn & Tin tức, Hỏi đáp, Thuật ngữ | Bỏ `padding-bottom:40px` của khối đầu trang (vòng 5); xen kẽ nền mist/trắng giữ nguyên | Hình học về gốc |
| Công cụ QA | Thêm `qa/r6geo.js`, `qa/r6geocmp.py`, `qa/r6herotable.py`, `qa/r6contrastcmp.py`, `qa/r6review.py`, `qa/r6preview.py` | Đo hình học so với build gốc |
| Hướng dẫn VNSHINE (EN, 中文) | Hai thẻ phương thức ("View details" / "查看詳情") đổi `href="#so-cap"`, `href="#thu-cap"` thành `href="#"` (site.js đã chặn), thêm `cursor:pointer` như bản VI. Bấm thẻ cuộn mượt tới mục, giữ `#/en/guideVnshine`, `#/zh/guideVnshine`. Hàm vá `p_r6_02_anchor` trong `src/patches6b.py` (mới). Thêm `qa/r6anchors.js` (bấm mọi link neo ở hai trang Hướng dẫn, VI/EN/中文, báo link làm đổi route) và `qa/r6click.js` | Bình luận #34, #84: bấm thẻ làm hash đổi sang `#so-cap` nên mất route, về trang chủ. Các link neo còn lại ở hai trang Hướng dẫn đã kiểm: không còn link nào làm mất route |
| Hướng dẫn VNSHINE (EN, 中文) | Bước 03 của Giao dịch thứ cấp: bỏ ô tròn teal đậm "✓" và nhãn "Step 03" / "步驟 03", đổi thành ô tròn vàng có số "03" và đường vàng chạy dài, cùng kiểu bước 01, 02 (bản VI vốn đã đúng). Hàm vá `p_r6_03_step03` trong `src/patches6b.py` (mới) | Bình luận #30 |
| Hướng dẫn PHVSF (VI/EN/中文) | Nút "Tải về ↓" (40px trên máy tính, 44px trên điện thoại) dưới mục "Phiếu đăng ký mở tài khoản giao dịch chứng chỉ quỹ mở" trong Hồ sơ Nhà đầu tư cá nhân. Chưa có file: bấm hiện "Tài liệu đang được cập nhật" (cơ chế A05, thêm nhận `data-dl` ở `src/parts/site.js`). File PDF ghi `[placeholder]` ở `specs/dev-handoff.md` mục 3 | Bình luận #16 |
| Hướng dẫn PHVSF (VI/EN/中文) | Khối "Biểu mẫu" mới sau bước 04, trước Đại lý phân phối: lead trang Biểu mẫu, 4 biểu mẫu Quỹ mở PHVSF (lấy từ `d.forms.groups[0]`), nút "Tải về" theo A05, link "Xem tất cả biểu mẫu" sang trang Biểu mẫu. Nền mist `#E3EEF0`; khối Đại lý phân phối liền sau đổi sang trắng để hai khối không cùng nền (R5). CSS ở `src/parts/r6b.css` (mới, nạp sau r5.css). Chữ mới chờ pháp chế: "Xem tất cả biểu mẫu" / "View all forms" | Bình luận #81 |
| Học viện (VI/EN/中文) | Thẻ "Biểu mẫu" dưới Thuật ngữ đầu tư (cột trái): tiêu đề và lead lấy từ trang Biểu mẫu, nút "Xem tất cả biểu mẫu →" sang trang Biểu mẫu (không phải Công bố thông tin) | Bình luận #79 |
| Công cụ QA | Thêm `qa/r6forms.js` (nút Tải về, link Biểu mẫu, bước 03, tràn ngang ở VI/EN/中文, 1440 và 390), `qa/r6shot.js` (chụp dải trang từ một phần tử, nhận `HTML=` để chụp bản khác) | Kiểm R6-03 |
| Toàn site (VI) | R6-04, Q5: "Lợi suất Cổ đông" đổi thành "Tỷ suất Lợi nhuận Cổ đông" ở 11 chỗ (hero và thẻ VNSHINE, tổng quan, tiêu đề chiến lược, FAQ, thuật ngữ, phụ đề Học viện, tiêu đề tab) và tiêu đề tin 10.09.2026. Bản EN giữ "Shareholder Yield". Hàm vá `p_r6_04_yield` trong `src/patches6c.py` (mới, đăng ký sau `PATCHES6B`) | Rin chốt Q5 theo brand-rules. Đóng issue #9 |
| PHVSF | R6-04: nhãn hero "QUỸ MỞ · GIAO DỊCH HẰNG NGÀY" / "OPEN-ENDED FUND · DAILY DEALING" đổi thành "QUỸ MỞ" / "OPEN-ENDED FUND". 中文 không đổi (đã hiện chữ EN từ trước), chờ cô Helena | Bình luận #111, #100 |
| PHVSF, VNSHINE, Danh sách quỹ | R6-04: ghi chú dưới bảng và biểu đồ thống nhất 12px, in nghiêng, màu `--muted` ("Số liệu minh hoạ, cập nhật đến ngày…" nay in nghiêng, ghi chú hiệu quả 12,5px và "*Theo dữ liệu tại ngày" 13px về 12px). Nội dung giữ nguyên | Bình luận #50, #72; Rin chốt Q7: giữ dòng, chữ nhỏ nghiêng |
| PHVSF, VNSHINE | R6-04: chữ "Chọn tất cả" bấm được cả dòng (chữ + ô tick), dùng được bằng bàn phím (Tab, Space/Enter, aria-checked), ẩn khi loại tài liệu chưa có file | Bình luận #3 |
| PHVSF, VNSHINE | R6-04: bộ lọc Tài liệu quỹ hiện đủ 9 loại (Báo cáo ngày, tuần / Báo cáo tài chính / Báo cáo hoạt động tháng / Factsheets / Bản cáo bạch / Điều lệ quỹ / Thông tin quỹ / Giấy phép / Khác). Chọn loại chưa có file thì hiện một dòng "Tài liệu đang được cập nhật", nút tải báo thông báo. Bỏ biểu mẫu khỏi Tài liệu quỹ ("Mẫu đăng ký mua/bán chứng chỉ quỹ" ở PHVSF, "Bộ tài liệu dành cho thành viên lập quỹ" ở VNSHINE; đã có ở trang Biểu mẫu). Công bố thông tin đã dùng sẵn đủ 8 loại của #116, không đổi | Bình luận #94, #98, #115, #116, #130, #134; Rin chốt Q8 |
| Danh sách quỹ | R6-04: tiêu đề cột và ô "Giao dịch" không xuống dòng (`white-space:nowrap` ở `src/parts/r6c.css`, nạp sau `r6.css`). Đo 1440, 1280, 1024, VI và EN: tiêu đề cao 40px một dòng, không tràn ngang | Bình luận #71 |
