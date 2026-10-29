# Bộ ảnh stock mới (R4-09, issue #14)

Lập 30/10/2026 (Cowork). Rin góp ý:
- Bớt ảnh AI quá lố, bớt ảnh chỉ có người. Thêm ảnh stock tài chính, chứng khoán, giữ phong cách Vanguard.
- Thay hết ảnh hero trang con cho khớp với trang chủ.
- Mỗi vị trí một phương án.

Bộ này thay luôn bộ ảnh của R4-02 (#3, hero Về chúng tôi) và R4-08 (#11 / PR #12).

## Cách làm ảnh

- Higgsfield, model Nano Banana Pro, 2k. Ảnh gốc: `assets/source/generated/r5_*.webp`. Bản web: `assets/img/r5_*.webp`.
- **Hero trang con (H1–H10)** chụp giờ xanh (blue hour): trời teal đậm, đèn thành phố HCMC, cùng tông với ảnh hero trang chủ (`hm_h2`) và nền teal đậm `#0A3440` của hero trang con.
- **Ảnh bài viết (N1–N10)** là ảnh ban ngày, sáng, kiểu ảnh báo tài chính.
- Tỉ lệ ảnh có người làm chủ thể: 3/20 (H6 Tư vấn, H7 Học viện, H8 Tuyển dụng). H9 và N6 chỉ thấy tay.
- Không chữ và số đọc được, không logo, không biểu đồ phát sáng, không mũi tên đi lên, không be/nâu.
  - N4 có vài số % rất nhỏ trên biểu đồ tròn.
  - N6 có chữ "Fund Factsheet" chung chung.
  - H3 có số mờ trên bảng điện.
  - Ở cỡ hiển thị không đọc được các chi tiết trên. Rin thấy cần thì Cowork tạo lại.
- Xem nhanh: `plans/stock-r5/contact-sheet.jpg`.

## Bảng kiểm kê

Chỗ trong code: số dòng trong `src/src_o8.html` (đọc, không sửa). Khoá cũ là khoá sau các bản vá vòng 1–3 (`p_imgmap`, `p_r3img`). Thay theo **từng vị trí**: một khoá cũ có thể đang dùng ở nhiều chỗ, ví dụ `pk_I03` ở hero PHVSF, hero Hướng dẫn PHVSF và thẻ Học viện; `team` ở hero Tuyển dụng và một bài viết.

| Mã | Trang | Vị trí | Chỗ trong code | Khoá cũ | Khái niệm mới | Có người? | Khung | Khoá mới |
|---|---|---|---|---|---|---|---|---|
| H1 | Về chúng tôi | Hero `#ab-overview` | template ~7749 (ảnh I01) | `ab_hero` | Phòng họp tầng cao, bàn trắng có laptop và tài liệu, cửa kính nhìn ra sông Sài Gòn lúc lên đèn | Không | 4:3 | `r5_about_hero` |
| H2 | PHVSF | Hero `.fh` | `funds.phvsf.heroImg` ~6200 | `pk_I03` | Bàn chuyên viên phân tích, 2 màn hình biểu đồ mờ, cửa sổ nhìn ra thành phố | Không | 16:9 | `r5_phvsf_hero` |
| H3 | VNSHINE | Hero `.fh` | `funds.vnshine.heroImg` ~6265 (đã đổi ở `p_r3img`) | `r3_vns_hero` | Bảng điện chứng khoán chụp xiên, xoá phông, cửa sổ lúc tối | Không | 16:9 | `r5_vns_hero` |
| H4 | Quỹ thành viên | Ảnh hero `.dh` | `services.member.img` ~6339 | `advisor` | Phòng họp hội đồng, tài liệu đóng bìa, ghế trống, kính nhìn ra thành phố | Không | 4:5 | `r5_member_hero` |
| H5 | Quản lý danh mục | Ảnh hero `.dh` | `services.portfolio.img` ~6343 | `pk_I05` | Báo cáo phân bổ danh mục in và tablet trên bàn trắng, nhìn từ trên | Không | 4:5 | `r5_pf_hero` |
| H6 | Tư vấn đầu tư | Ảnh hero `.dh` | `services.advisory.img` ~6347 (đã đổi ở `p_r3img`) | `r3_adv_hero` | Chuyên viên tư vấn trẻ trao đổi với khách (khách quay lưng), thành phố lúc lên đèn | Có | 4:5 | `r5_adv_hero` |
| H7 | Học viện | Hero `.dh` | template hero Học viện (ảnh I07) | `pk_I07` | Buổi workshop nhà đầu tư trẻ, nhìn từ cuối phòng | Có (nhỏ) | 4:3 | `r5_acad_hero` |
| H8 | Tuyển dụng | Hero `.dh` | template hero Tuyển dụng | `team` | Nhóm 4 người trẻ làm việc ở bàn đứng, bảng trắng | Có | 4:3 | `r5_cr_hero` |
| H9 | Hướng dẫn PHVSF | Dải ảnh `.nm-ghero` (VI/EN/中文) | 3 thẻ `<img>` alt "Chồng đá cân bằng…" ~8042, 8276, 8508 | `pk_I03` | Tay cầm điện thoại xem app đầu tư bên cửa kính quán cà phê, phố xe máy lúc tối | Chỉ tay | 21:9 | `r5_gp_hero` |
| H10 | Hướng dẫn VNSHINE | Dải ảnh `.nm-ghero` (VI/EN/中文) | 3 thẻ `<img>` alt "Tòa tháp kính vàng…" ~8742, 8934, 9126 | `vn_city` | Ba màn hình biểu đồ trên bàn giao dịch, kính nhìn ra sông | Không | 21:9 | `r5_gv_hero` |
| N1 | Góc nhìn | Bài nổi bật "MSCI và bài toán tín nhiệm thị trường" | `news` ~6462 | `r3_nw_msci` | Khu tài chính Q1 và Thủ Thiêm nhìn từ trên cao, buổi sáng | Không | 16:9 | `r5_nw_msci` |
| N2 | Góc nhìn | "Triển vọng luân chuyển và phân bổ nhóm ngành" | ~6463 | `r3_nw_rot` | Cảng container trên sông Sài Gòn nhìn từ trên cao | Không | 16:9 | `r5_nw_rot` |
| N3 | Góc nhìn | "Cập nhật vĩ mô tháng 8: lãi suất và tỷ giá" | ~6464 | `pk_I12` | Laptop biểu đồ mờ và báo cáo kinh tế in trên bàn trắng | Không | 16:9 | `r5_nw_macro` |
| N4 | Góc nhìn | "Kỷ luật tái cân bằng trong giai đoạn biến động" | ~6465 | `pk_I14` | Trang biểu đồ phân bổ tài sản, bút chì, thước | Không | 16:9 | `r5_nw_rebal` |
| N5 | Góc nhìn | "Báo cáo thị trường tháng 8/2026" | ~6466 | `nw_city` | Văn phòng nghiên cứu ban ngày, dãy màn hình biểu đồ mờ | Không | 16:9 | `r5_nw_aug` |
| N6 | Góc nhìn | "Đọc báo cáo tài chính quỹ: năm chỉ số cần biết" | ~6467 | `pk_I15` | Tay lật tờ thông tin quỹ in, bút dạ quang, cà phê | Chỉ tay | 16:9 | `r5_nw_fund` |
| N7 | Góc nhìn | "Ngành ngân hàng nửa cuối 2026…" | ~6468 | `team` | Sảnh ngân hàng hiện đại trước giờ mở cửa, không người | Không | 16:9 | `r5_nw_bank` |
| N8 | Góc nhìn | "Đầu tư định kỳ và bình quân giá vốn" | ~6469 | `pk_I13` | Lịch tháng đánh dấu vài ngày, điện thoại mở app, bút | Không | 16:9 | `r5_nw_dca` |
| N9 | Góc nhìn | "Triển vọng thị trường nửa cuối năm 2026" | ~6470 | `pk_I17` | Nhìn qua cửa kính tầng cao ra Thủ Thiêm, sổ tay trên bậu cửa | Không | 16:9 | `r5_nw_h2` |
| N10 | Góc nhìn | "Cổ tức tiền mặt và mua lại cổ phiếu tại Việt Nam" | ~6471 | `pk_I18` | Hội trường đại hội cổ đông trống, bàn có tài liệu | Không | 16:9 | `r5_nw_div` |

## Giữ nguyên

- Ảnh trang chủ (`hm_*`), logo đối tác, icon mạng xã hội.
- Ảnh trụ sở Phú Mỹ Hưng (`pmh`, ảnh thật) và dải Sứ mệnh/Tầm nhìn (`pk_I02`).
- Ba ảnh tin sự kiện có thật (`nw_etf1`, `nw_etf2`, `nw_pet`).
- Bốn ảnh thẻ Tuyển dụng (`pk_I08`, `cr_team`, `cr_grow`, `pk_I11`).
- Hai thẻ Học viện (`pk_I03`, `vn_city`) và nền khối kêu gọi cuối 2 trang Hướng dẫn (`th_cta`…). Các ảnh này không trùng hero mới.

## Alt cho ảnh có nội dung

- H9 Hướng dẫn PHVSF: "Nhà đầu tư xem ứng dụng đầu tư trên điện thoại" / "An investor checking an investing app on a phone" / "投資人在手機上查看投資應用程式"
- H10 Hướng dẫn VNSHINE: "Màn hình theo dõi giá và NAV của quỹ ETF" / "Screens tracking ETF price and NAV" / "追蹤 ETF 價格與 NAV 的螢幕"
- Các ảnh còn lại là ảnh trang trí: giữ `alt=""` như hiện tại.

## Gợi ý `object-position`

| Ảnh | Desktop | Mobile ≤760px |
|---|---|---|
| H1 | `70% 50%` (bàn bên phải, trời bên trái cho chữ) | `75% 50%` |
| H2, H3, H10 | `75% 50%` | `80% 50%` |
| H9 | `85% 50%` (tay cầm điện thoại bên phải) | `88% 50%` |
| H4–H8 | `50% 50%` | `50% 40%` |
