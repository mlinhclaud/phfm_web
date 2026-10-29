# Plan vòng 4 · website PHFM

- Lập: 30/10/2026 (Cowork, Opus 5.5). Rin giao cho Claude tự quyết B1, B2, B4. Plan này coi như đã duyệt.
- Go-live dự kiến **02/11/2026**: ưu tiên R4-05 (chữ Hán mất) và R4-01/R4-04 trước.
- Mỗi mục một nhánh `r4/<mã>`, một PR. CSS mới để ở `src/parts/r4.css`; vá template/logic ở `src/patches4.py` (tạo mới, đăng ký sau `_p2.POST` trong `PATCHES` của `src/patches.py`).
- Ảnh hiện trạng để so: chạy `node qa/qa.js`, hoặc xem `plans/round-4/` (ảnh chụp lúc lập plan).

## Bảng việc

| Mã | Trang | Việc cần làm | File đụng tới | Tiêu chí nghiệm thu | Agent | Trạng thái |
|---|---|---|---|---|---|---|
| R4-00 (#1) | Toàn site | Tạo khung vòng 4: `src/patches4.py` (rỗng, có `PATCHES4`), `src/parts/r4.css` nạp sau `r3.css`, đăng ký trong `src/patches.py` | `src/patches.py`, `src/patches4.py`, `src/parts/r4.css` | Build ra file giống hệt trước (so `md5`), QA xanh | frontend | Chờ làm |
| R4-01 (#2) | Mọi trang con có hero (about, phvsf, vnshine, member, portfolio, advisory, academy, careers, guidePhvsf, guideVnshine) | Thu chiều cao hero. Bỏ `min-height:min(900px, calc(100vh - …))`. Desktop ≥1280: `min-height:560px` (trang quỹ 600px vì có ô giá), padding trên/dưới 64px. 768–1279: 480px. Mobile ≤760: không min-height, padding 32px trên, 40px dưới | `src/patches4.py` (thay chuỗi min-height ở các `<section>` hero: `#ab-overview`, `.fh`, `.dh`), `src/parts/r4.css` | 1440×900: tiêu đề + đoạn mô tả + nút + mép trên của mục kế tiếp đều nằm trong màn hình đầu. Chiều cao hero 1440 ≤ 640px. Mobile 390: hero ≤ 1 màn hình + ô giá. Không tràn ngang | frontend | Chờ làm |
| R4-02 (#3) | Về chúng tôi | Thay ảnh hero bằng `r4_ab_hero` (desktop) và `r4_ab_hero_m` (mobile ≤760, dùng `<picture>`/`srcset` hoặc CSS). Ảnh nằm nửa phải, gradient trắng sang trong suốt từ trái như hiện tại. `object-position` để nhóm người không bị chữ đè | `src/patches4.py` (ảnh hero about trong template, khoá hiện là `ab_hero`), `src/parts/r4.css` | Ảnh mới hiện ở VI/EN, 1440 và 390. Không ô chữ nào đè lên mặt người. Ảnh cũ `ab_hero` không còn được dùng (xoá khỏi `assets/img`) | frontend | Ảnh đã có |
| R4-03 (#4) | Về chúng tôi | Thiết kế lại "Lịch sử hình thành" (`#ab-journey`) theo style Vanguard: nền teal đậm `#0A3440`, ba giai đoạn thành ba cột; mỗi cột có năm lớn (vàng `#E9C46A`, 40–48px) và tên giai đoạn, các mốc là danh sách năm–sự kiện chữ trắng/mist. Một đường trục ngang mảnh màu vàng nối ba điểm mốc. Mobile: một cột dọc, trục dọc bên trái. Bỏ khung thẻ trắng cao bằng nhau đang để trống nhiều | `src/patches4.py` (template `#ab-journey`), `src/parts/r4.css` | Giữ nguyên nội dung các mốc (VI/EN). Không còn khoảng trống lớn dưới cột 1 và 2 (chênh chiều cao nội dung giữa các cột không tạo khung trống). Tương phản chữ ≥ 4.5:1. 390px đọc được, không tràn | frontend | Chờ làm |
| R4-04 (#5) | VNSHINE (và PHVSF cho đồng bộ) | Làm lại ô giá ở hero. Hàng chỉ số dùng lưới 3 cột đều: Giá đóng cửa · NAV/CCQ · Ngày (PHVSF: NAV/CCQ · Ngày, 2 cột). Cỡ số 28–30px, nhãn 12px. Bỏ `flex-wrap` đang đẩy "Ngày" xuống hàng gây khoảng trống. Bảng hiệu quả: cột nào toàn giá trị trống ("—", vd 3 tháng của VNSHINE vì quỹ niêm yết 10/09/2026) thì ẩn, thêm 1 dòng ghi chú "Quỹ niêm yết ngày 10/09/2026, chưa đủ dữ liệu 3 tháng." (EN tương ứng) | `src/patches4.py` (khối ô giá trong template trang quỹ, logic `f.heroColsL`/`f.cuRows` trong class `Component`), `src/parts/r4.css` | 1440: ba chỉ số cùng một hàng, cách đều, không có khoảng trống thừa. 390: Giá + NAV một hàng, Ngày hàng dưới, thẳng cột. Số liệu không đổi so với trước. Cột trống không còn hiện | frontend | Chờ làm |
| R4-05 (#6) | Về chúng tôi | Bổ sung chữ Hán 新 速 實 簡 cho bốn giá trị Tân · Tốc · Thực · Giản. Dữ liệu đã có (`d.about.values[].c`), template chưa hiển thị. Thêm dòng `{{ v.c }}` trên tên giá trị, font Noto Serif TC, 56–64px, màu vàng logo `#C0962D`. Nhúng font subset chỉ gồm các chữ cần dùng (lấy từ npm `@fontsource/noto-serif-tc` hoặc tương đương, subset bằng `fonttools`), base64 vào CSS như Inter | `src/patches4.py`, `src/parts/r4.css`, `vendor/fonts/` (file subset), `scripts/setup.sh` nếu cần thêm `fonttools` | Bốn chữ Hán hiện đúng ở VI và EN, 1440 và 390, kể cả máy không cài font Hán. Dung lượng font thêm ≤ 30 KB | frontend | Chờ làm |
| R4-08 (#11) | PHVSF, VNSHINE, 2 trang Hướng dẫn, Quản lý danh mục, Góc nhìn | Thay ảnh bằng bộ stock tài chính/chứng khoán mới (bảng ở mục "Bộ ảnh stock vòng 4"). Thay theo từng vị trí, không thay hàng loạt theo khoá cũ. Cập nhật luôn `alt` của các ảnh hero Hướng dẫn (VI/EN/中文) cho đúng ảnh mới | `src/patches4.py` | Mỗi vị trí trong bảng hiện đúng ảnh mới ở VI/EN, 1440 và 390. Không còn alt "chồng đá", "tòa tháp vàng". Ảnh không bị chữ đè mất phần chính (chỉnh `object-position` nếu cần). Các khoá không còn dùng (`r3_vns_hero`…) xoá khỏi `assets/img` | frontend | Ảnh đã có |
| R4-06 (#7) | Toàn site | QA tổng sau khi merge R4-01 đến R4-05: chạy `node qa/qa.js` 20 trang × VI/EN × 1440/390, xem ảnh các trang có hero | `specs/changelog.md` | QA xanh. Không hỏng các thay đổi vòng 1–3 (header 1 gạch, nút Công cụ, tài liệu quỹ, logo đối tác, footer 5 icon) | reviewer | Chờ làm |
| R4-07 (#8) | Canvas trang con | Sau khi merge: Cowork chạy `tools/canvas_gen.py`, upload ảnh `r4_ab_hero*` lên canvas, đăng lại canvas Trang con, cập nhật `specs/canvas/published/` | `specs/canvas/*` | Canvas khớp bản build | Cowork | Chờ làm |

## Ảnh đã chuẩn bị (Cowork, Higgsfield Nano Banana Pro, 2k)

- Ba phương án hero Về chúng tôi trong `assets/source/generated/`: `about_hero_r4_window` (đã chọn), `about_hero_r4_team`, `about_hero_r4_desk`. Xem nhanh: `plans/round-4/about-hero-options.jpg`.
- Chọn `window`: một chuyên viên trẻ đứng bên cửa kính nhìn ra trung tâm tài chính và sông Sài Gòn. Người ở phần ba bên phải, nửa trái là trời và thành phố, hợp với bố cục chữ bên trái và lớp gradient trắng. Ảnh tư vấn khách hàng cũ giống trang dịch vụ hơn trang giới thiệu công ty.
- Đã nén: `assets/img/r4_ab_hero.webp` (1920px) và `assets/img/r4_ab_hero_m.webp` (900×1097, crop phần người cho mobile).
- Rin muốn đổi sang `team` hoặc `desk`: chạy lại `tools/add_image.py` với file tương ứng, giữ nguyên khoá.

## Bộ ảnh stock vòng 4 (Cowork, Nano Banana Pro)

Rin góp ý 30/10: bớt ảnh AI quá lố, bớt ảnh chỉ có người; thêm ảnh stock tài chính, chứng khoán. Bộ ảnh mới chụp theo kiểu ảnh báo, ánh sáng tự nhiên, không hiệu ứng phát sáng. Xem nhanh: `plans/round-4/stock-r4.jpg`. Ảnh gốc: `assets/source/generated/stock_*.webp`.

| Vị trí | Chỗ trong code (`src/src_o8.html`, sau `p_imgmap`) | Khoá cũ | Khoá mới | Ảnh |
|---|---|---|---|---|
| Hero PHVSF | dữ liệu `funds.phvsf.heroImg` (dòng ~6200) | `pk_I03` | `r4_phvsf_hero` | Bàn làm việc, laptop và màn hình biểu đồ, cửa kính |
| Hero VNSHINE | `funds.vnshine.heroImg` (đã đổi ở `p_r3img`) | `r3_vns_hero` | `r4_vns_hero` | Bảng điện chứng khoán, xoá phông |
| Hero Hướng dẫn PHVSF (VI/EN/中文) | 3 thẻ `<img>` alt "Chồng đá cân bằng…" (~8042, 8276, 8508) | `pk_I03` | `r4_gp_hero` | Tay cầm điện thoại xem app đầu tư, quán cà phê Sài Gòn |
| Hero Hướng dẫn VNSHINE (VI/EN/中文) | 3 thẻ `<img>` alt "Tòa tháp kính vàng…" (~8742, 8934, 9126) | `vn_city` | `r4_gv_hero` | Bàn giao dịch, biểu đồ giá ETF và NAV, cửa kính nhìn ra thành phố |
| Hero Quản lý danh mục | `services.portfolio.img` (~6343) | `pk_I05` | `r4_pf_hero` | Báo cáo danh mục in, tablet, bút, nhìn từ trên |
| Bài "Cập nhật vĩ mô tháng 8" | `news` dòng ~6464 | `pk_I12` | `r4_nw_macro` | Màn hình biểu đồ nến cận cảnh |
| Bài "Kỷ luật tái cân bằng…" | `news` dòng ~6465 | `pk_I14` | `r4_nw_rebal` | Tay chỉnh bảng phân bổ tài sản |
| Bài "Đầu tư định kỳ và bình quân giá vốn" | `news` dòng ~6469 | `pk_I13` | `r4_nw_dca` | Lịch đánh dấu ngày, điện thoại, tiền VND |

Giữ nguyên: thẻ PHVSF/VNSHINE ở Học viện và khối kêu gọi cuối 2 trang Hướng dẫn (dòng ~6324, 6325, 10016) vẫn dùng ảnh cũ để mỗi vị trí một ảnh.

Alt mới gợi ý:
- Hướng dẫn PHVSF: "Nhà đầu tư xem ứng dụng đầu tư trên điện thoại" / "An investor checking an investing app on a phone" / "投資人在手機上查看投資應用程式"
- Hướng dẫn VNSHINE: "Màn hình theo dõi giá ETF và NAV" / "Screens tracking ETF price and NAV" / "追蹤 ETF 價格與 NAV 的螢幕"
- Ảnh hero trang quỹ, danh mục, bài viết: alt rỗng như hiện tại (ảnh trang trí).

## Cần Rin quyết (không tự sửa)

1. (#9) Trang VNSHINE còn dòng "Chiến lược Lợi suất Cổ đông - Shareholder Yield". Theo chuẩn thương hiệu đã chốt, tiếng Việt của Shareholder Yield là "Tỷ suất Lợi nhuận Cổ đông". Có đổi trên web không?
2. (#10) Hero trang quỹ PHVSF trên mobile: ảnh gần như bị lớp teal phủ kín. Giữ như vậy (gọn, dễ đọc) hay cho hiện ảnh thành một dải riêng dưới phần chữ?
