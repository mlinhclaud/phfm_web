# Specs giao diện (UI/UX) · website PHFM bản Teal

Bản này mô tả giao diện đã chốt tới vòng 6 (30/10/2026) để dev dựng lại trên nền tảng thật (CMS/frontend framework). Nguồn chuẩn để so là file `dist/phfm-website.html` và bộ ảnh toàn trang trong gói bàn giao. Số đo lấy trực tiếp từ bản build (đo bằng trình duyệt), bản VI.

## 1. Màu

| Token | Mã | Dùng cho |
|---|---|---|
| Teal đậm | `#0A3440` | Nền hero trang con (mảng trái), tiêu đề H1/H2 trên nền sáng, chữ đậm |
| Teal | `#0B6274` | Mảng chéo hero, link, nút phụ, icon, viền focus |
| Mist | `#E3EEF0` | Nền section xen kẽ, thanh mục con, chân trang |
| Đường kẻ | `#D8E7EA` | Viền thẻ, đường kẻ 1px giữa khối (giữ theo Q1) |
| Vàng nút | `#E9C46A` (hover `#F2D27D`) | Nút chính, nhãn nhỏ trên nền teal, gạch dưới tiêu đề hero, gạch menu |
| Vàng logo | `#C0962D` | Chữ Hán 新 速 實 簡, nhấn nhỏ |
| Vàng chữ (trên nền sáng) | `#7D5F1A` | Nhãn nhỏ (eyebrow), số liệu nổi bật trên nền trắng (đạt tương phản AA) |
| Chữ chính / phụ | `#16262B` / `#4D6066` | Thân bài / mô tả, ghi chú |
| Tăng / giảm | `#15897D` / đỏ dữ liệu; riêng thẻ giá ở hero quỹ: `#0F7468` / `#B4472E` | Chỉ dùng cho số liệu tăng giảm. Thẻ giá dùng màu đậm hơn để đạt tương phản ≥ 4,7:1 trên nền ảnh (issue #47, PR #53) |

Không dùng nền đen/than chì, không be/kem/nâu (`specs/brand-rules.md`).

## 2. Chữ

- Font: **Inter** 300–700 (latin + vietnamese), nhúng sẵn. Chữ Hán: Noto Serif TC subset (chỉ 新 速 實 簡). Bản 中文 dùng font hệ thống cho chữ Hán thân bài.
- Thang chữ đo ở 1440 / 1024 / 390:

| Vai trò | 1440 | 1024 | 390 | Ghi chú |
|---|---|---|---|---|
| H1 hero trang quỹ | 60/66 bold, -0.02em | 43/47 | 35/39 | `clamp()` theo bề rộng |
| H1 hero trang con khác | 48–52/56–60 bold | 37–52 | 35/39 | Học viện co theo bề rộng |
| H2 tiêu đề khối | 48/56 (trang quỹ, Về chúng tôi); 28–36 (trang nội dung) | 28–48 | 25.7/30.9 | |
| H3 thẻ/bài | 20/28 semibold | 20/28 | 20/28 | |
| Thân bài | 15–17/24–28 | như 1440 | 15–17 | Đoạn mô tả hero 17–20/28–30 |
| Nhãn nhỏ (eyebrow) | 12–13, chữ hoa, giãn chữ 0.08–0.18em, semibold | | | Vàng `#E9C46A` trên teal, `#7D5F1A` trên nền sáng |
| Ghi chú số liệu | 12px nghiêng, `#4D6066` | | | "Số liệu minh hoạ…", ghi chú dưới bảng |
| Nút chính | 18px semibold, giãn chữ 0.08em, cao 56px | | | Nút nhỏ 14px, cao 36–52px |

Không ép giãn chữ (letter-spacing âm) để chữ vừa một dòng; chữ dài thì xuống dòng.

## 3. Khoảng cách và khung

- Khung nội dung: rộng tối đa **1280px**, lề trái/phải **48px** (desktop), **18px** (mobile ≤760px).
- Section: đệm trên/dưới **60px** desktop, **34px** mobile (một số khối 56–72px theo bản gốc).
- Hero trang con (đo ở 1440): Về chúng tôi, PHVSF, VNSHINE, Học viện, Tuyển dụng **775px**; Quỹ thành viên, Quản lý danh mục, Tư vấn **795px**; Hướng dẫn PHVSF **345px**, Hướng dẫn VNSHINE **327px**. Công thức gốc: `min-height: min(900px, calc(100vh - chiều cao header))`.
- Bo góc: thẻ 12–16px, nút bo tròn (pill), khung ảnh hero 20px.
- Vùng chạm tối thiểu **44px** trên mobile (nút, ô tick, link trong bảng).

## 4. Thành phần chính

| Thành phần | Mô tả |
|---|---|
| Header | Thanh trên (hotline, email, tìm kiếm, VI/EN/中文) teal đậm, không dính. Thanh menu trắng dính khi cuộn, menu chữ 600, mục đang mở có **một** gạch vàng 2px. Nút "PHFM Trading" teal. Mobile: nút tìm kiếm + menu 3 gạch, menu mở toàn màn hình |
| Hero trang con | Mảng trái teal đậm, mảng chéo teal bên phải (skewX -16°, mốc 55%), vòng vàng mảnh ở góc, ảnh trong khung bo 20px. Breadcrumb, nhãn vàng, H1 trắng, gạch vàng 48×3px, đoạn mô tả mist, hàng nút |
| Thẻ giá (trang quỹ) | Thẻ trắng mờ trên ảnh hero: Giá đóng cửa (ETF) · NAV/CCQ · Ngày, bảng hiệu quả 1 tháng / 3 tháng / từ khi thành lập, ghi chú nghiêng |
| Thanh mục con | Dính dưới header, nền mist, chữ teal, mục đang xem có gạch vàng 3px |
| Bảng hiệu quả, Lịch sử NAV | Bảng số căn phải, số tabular, tăng xanh/giảm đỏ có mũi tên; tab kỳ; ô chọn ngày dd/mm/yyyy |
| Tài liệu quỹ | Lọc Loại tài liệu (9 loại) + Năm, dòng "Chọn tất cả" (bấm cả dòng), ô tick từng tài liệu, nút "Tải tài liệu đã chọn (n)", nút tải từng file |
| Ban điều hành | Thẻ có chữ viết tắt tên, bấm cả thẻ mở hộp thoại giới thiệu |
| Quỹ phù hợp | Khối nền mist, danh sách có ô tích |
| Lịch sử hình thành | 3 thẻ trắng (3 giai đoạn) trên nền mist, mốc năm vàng |
| Giá trị cốt lõi | 4 cột: chữ Hán 新 速 實 簡 (vàng logo, serif) trên tên Tân · Tốc · Thực · Giản; mobile 2×2 |
| Form | Ô nhập cao 44–48px, nhãn trên ô, ô đồng ý xử lý dữ liệu cá nhân, nút gửi vàng |
| Thông báo (toast) | Hộp teal đậm giữa đáy màn hình, 2,8 giây |
| Nút Công cụ nổi | Góc phải dưới, mở 3 công cụ minh hoạ |
| Footer | Nền mist, viền vàng 4px trên, logo, địa chỉ, 5 icon mạng xã hội, App Store/Google Play, dòng cảnh báo rủi ro |

## 5. Responsive

| Mốc | Thay đổi |
|---|---|
| ≥1400px | Hero hai cột (chữ trái, ảnh phải) ở Về chúng tôi, Học viện |
| 1100–1399px | Về chúng tôi, Học viện chuyển ảnh xuống dưới chữ (bản gốc); trang quỹ vẫn hai cột |
| <1100px | Trang quỹ xếp dọc: chữ, nút, rồi thẻ giá trên dải teal |
| ≤1279px | Menu chuyển sang nút 3 gạch |
| ≤760px | Lề 18px, chữ căn trái, bảng rộng cuộn ngang trong khung riêng, lưới 4 cột thành 2 hoặc 1 |
| 390px | Mốc kiểm thử mobile chính; không có cuộn ngang ở cả 20 trang × 3 ngôn ngữ |

## 6. Trạng thái và tương tác

- Hover thẻ bấm được: nền `#F2F8F9`, viền `#86B4BE`, nhấc 4px. Focus bàn phím: viền teal 2px.
- Hiệu ứng hiện dần khi cuộn (`.cr`) tắt khi người dùng bật giảm chuyển động.
- Link `href="#"` không đổi trang. Nút tải tài liệu chưa có file hiện thông báo thay vì mở link hỏng.
