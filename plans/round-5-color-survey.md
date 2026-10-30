# Vòng 5: khảo sát nền teal đậm #0A3440 trên 19 trang con

Lập 30/10/2026 (nhánh `r5/color-preview`). Số đo lấy bằng `node qa/survey-teal.js` (bản VI; bản EN cùng cấu trúc khối). Số liệu chạy trên bản build `main` trước khi áp A hoặc B.

## Cách đo

- **Khối nền #0A3440**: mọi phần tử nhìn thấy có `background-color` #0A3440, gradient chứa #0A3440 hoặc lớp phủ rgba(10,52,64,≥0,3). Danh sách ở bảng dưới (kích thước 1440 / 390).
- **Phẳng**: tỉ lệ điểm ảnh của màn hình đầu (1440×900, 390×844) gần #0A3440 (lệch ≤10 mỗi kênh). Đã gồm dải trên cùng 44 px (≈5% ở 1440).
- **Tối**: tỉ lệ điểm ảnh có độ sáng tương đối <0,06, tính cả ảnh giờ xanh tối. Đây mới là cảm giác "nặng" mà mắt thấy.
- Mảng #0B6274 không tính vào "phẳng" vì không phải teal đậm.

## Khối #0A3440 dùng chung mọi trang

- Dải trên cùng `.tb-bar` (44 px, toàn rộng) và nút nổi "Công cụ" (120×48). Giống trang chủ, giữ nguyên.
- Chân trang là mist #E3EEF0, không có teal đậm.

## Các loại khối teal đậm

| Loại khối | Trang | Ghi chú |
|---|---|---|
| Hero toàn khung `.dh` (r3.css) | about, member, portfolio, advisory, academy, careers | Cao 560-625 px ở 1440; ảnh giờ xanh đặt trên nền hoặc lớp mờ teal |
| Hero toàn khung `.fh` + gradient (r3.css) | phvsf, vnshine | Cao 600 px; ảnh giờ xanh phủ gradient #0A3440 → trong suốt |
| Thanh mục con `.nm-sbar` (r3.css) | about, phvsf, vnshine | 56 px, dính dưới header, nằm liền ngay dưới hero teal đậm nên hai khối nối thành một mảng |
| Lịch sử hình thành `.ab-j` (r4.css) | about | 679 px ở 1440 |
| Quỹ phù hợp `.fit` (r3.css) | phvsf | Thẻ bo 16 px trên nền trắng |
| Ô chênh lệch giá/NAV `.pd-cell` (r3.css) | vnshine | Một ô trong dải 3 ô |
| Vòng tròn viết tắt, chấm số bước | about, phvsf, vnshine | Nhỏ (56-84 px), nhấn vàng, không tính là mảng nặng |
| Khối kêu gọi cuối trang (gradient teal đậm trên ảnh) | news, guidePhvsf, guideVnshine | Cuối trang, giống dải "Bắt đầu tích luỹ" của trang chủ |
| Nút/chip đang chọn | guidePhvsf, glossary, academy | Nhỏ |

## Bảng theo trang: khối teal đậm và tỉ lệ ở màn hình đầu

Trang chủ (mốc): 1440 phẳng **29.9%**, tối **34.9%** · 390 phẳng **46.8%**, tối **54.3%**.

| Trang | Khối #0A3440 (1440 / 390, ngoài dải trên cùng và nút Công cụ) | 1440 phẳng | ×trang chủ | 1440 tối | 390 phẳng | ×trang chủ | 390 tối |
|---|---|---|---|---|---|---|---|
| about | Hero `.dh` toàn khung (563 px / 797 px) · thanh mục con `.nm-sbar` (57 px / 49 px) · Lịch sử hình thành `#ab-journey` (679 px / 1299 px) · 3 vòng tròn tên viết tắt Ban lãnh đạo (84 px) | 37.3% | 1.2 | 46.1% | 54.3% | 1.2 | 59.8% |
| funds | Chỉ dải trên cùng và nút Công cụ | 5.3% | 0.2 | 6.0% | 5.7% | 0.1 | 6.0% |
| phvsf | Hero `.fh` toàn khung kèm lớp gradient teal (600 px / 952 px) · thanh mục con · khối "Quỹ phù hợp với bạn" `.fit` (1184×414 / 354×539) · 2 vòng tròn viết tắt Ban điều hành (72 px) | 38.1% | 1.3 | 56.4% | 51.6% | 1.1 | 57.8% |
| vnshine | Hero `.fh` toàn khung kèm gradient (600 px / 1051 px) · thanh mục con · ô chênh lệch giá/NAV `.pd-cell` (394×107) · 4 chấm số bước 01-04 (56 px, màu nội tuyến) · 2 vòng tròn viết tắt Ban điều hành | 39.3% | 1.3 | 50.7% | 48.0% | 1.0 | 66.2% |
| member | Hero `.dh` toàn khung (625 px / 810 px) · ảnh hero có nền #0A3440 phía sau (không thấy) | 57.7% | 1.9 | 63.1% | 65.2% | 1.4 | 74.4% |
| portfolio | Hero `.dh` toàn khung (625 px / 728 px) | 57.2% | 1.9 | 58.7% | 59.5% | 1.3 | 61.1% |
| advisory | Hero `.dh` toàn khung (625 px / 697 px) | 58.4% | 2.0 | 65.8% | 59.1% | 1.3 | 72.5% |
| ir | Chỉ dải trên cùng và nút Công cụ | 5.3% | 0.2 | 5.9% | 5.6% | 0.1 | 5.8% |
| news | Khối đăng ký báo cáo thị trường (gradient teal đậm, 1184×302 / 354×462) | 5.8% | 0.2 | 7.1% | 6.7% | 0.1 | 7.5% |
| academy | Hero `.dh` toàn khung (560 px / 599 px) · nhãn "Hướng dẫn đầu tư Quỹ mở" (240×47) | 30.6% | 1.0 | 39.5% | 50.4% | 1.1 | 54.0% |
| careers | Hero `.dh` toàn khung (625 px / 641 px) | 54.7% | 1.8 | 60.3% | 48.3% | 1.0 | 56.5% |
| contact | Chỉ dải trên cùng và nút Công cụ | 5.4% | 0.2 | 6.2% | 5.6% | 0.1 | 6.2% |
| guidePhvsf | Nút tab đang chọn "Nhà đầu tư cá nhân" (163×44) · khối CTA cuối trang `.cta-img` (gradient teal đậm trên ảnh, 1184×337) · dải ảnh hero là ảnh tối (không phải nền phẳng) | 5.7% | 0.2 | 10.8% | 7.7% | 0.2 | 16.4% |
| guideVnshine | Khối CTA cuối trang `.cta-img` (1184×271) · dải ảnh hero là ảnh tối | 6.0% | 0.2 | 8.5% | 7.1% | 0.2 | 16.9% |
| faq | Chỉ dải trên cùng và nút Công cụ | 5.5% | 0.2 | 6.2% | 5.4% | 0.1 | 6.2% |
| glossary | Chip "Tất cả" đang chọn (74×44) | 5.6% | 0.2 | 6.6% | 6.4% | 0.1 | 7.3% |
| forms | Chỉ dải trên cùng và nút Công cụ | 5.2% | 0.2 | 5.9% | 5.7% | 0.1 | 6.2% |
| terms | Chỉ dải trên cùng và nút Công cụ | 5.0% | 0.2 | 6.4% | 5.3% | 0.1 | 8.2% |
| privacy | Chỉ dải trên cùng và nút Công cụ | 5.0% | 0.2 | 6.3% | 5.2% | 0.1 | 7.7% |

## Nhận xét

1. **Nặng nhất là hero toàn khung.** member, portfolio, advisory, careers: 55-58% màn hình đầu là teal đậm phẳng ở 1440 (trang chủ 30%), tối 60-66%. Ảnh giờ xanh làm phần "tối" cao hơn phần "phẳng".
2. **Hero + thanh mục con thành một mảng liền** ở about, phvsf, vnshine (600 + 56 px). Trang chủ có thẻ "Tôi muốn…" trắng đè lên mép hero nên mảng teal đậm đứt ra.
3. **Trong thân trang** mỗi trang con có thêm 1-2 mảng teal đậm (Lịch sử hình thành, Quỹ phù hợp, ô chênh lệch). Trang chủ chỉ có 2 dải teal đậm ngoài hero (câu thông điệp, dải "Bắt đầu tích luỹ"), mỗi dải ngắn.
4. **7 trang không có mảng teal đậm** nào ngoài dải trên cùng (funds, ir, contact, faq, forms, terms, privacy): đã nhẹ, không cần đổi.
5. **Mobile:** trang chủ mobile cũng tối (46,8% phẳng) vì chữ xếp trên nền #0A3440, nên trang con mobile (48-65%) chỉ nặng hơn trang chủ khoảng 1,0-1,4 lần.
6. **Hero Hướng dẫn** (guidePhvsf, guideVnshine) dùng nền sáng nhưng ảnh dải mới tối (tối 10-17% ở màn hình đầu). Không thuộc phạm vi hai phương án này.

## Sau khi áp phương án (cùng phép đo, 3 trang mẫu và các trang cùng khối)

| Trang | 1440 phẳng: hiện tại → A → B | 1440 tối: hiện tại → A → B | 390 phẳng: hiện tại → A → B | 390 tối: hiện tại → A → B |
|---|---|---|---|---|
| about | 37.3 → 33.6 → 6.1 | 46.1 → 38.3 → 11.2 | 54.3 → 56.8 → 7.6 | 59.8 → 61.2 → 13.9 |
| phvsf | 38.1 → 39.1 → 6.1 | 56.4 → 47.9 → 15.2 | 51.6 → 53.5 → 6.1 | 57.8 → 56.0 → 7.7 |
| vnshine | 39.3 → 39.0 → 5.8 | 50.7 → 44.6 → 13.3 | 48.0 → 63.0 → 5.6 | 66.2 → 64.3 → 7.1 |
| member | 57.7 → 37.0 → 5.8 | 63.1 → 42.5 → 11.5 | 65.2 → 61.9 → 6.3 | 74.4 → 71.1 → 16.8 |
| portfolio | 57.2 → 36.5 → 5.1 | 58.7 → 38.0 → 6.9 | 59.5 → 51.7 → 5.1 | 61.1 → 53.4 → 7.8 |
| advisory | 58.4 → 37.8 → 5.8 | 65.8 → 45.2 → 13.4 | 59.1 → 50.9 → 6.6 | 72.5 → 64.4 → 20.8 |
| academy | 30.6 → 34.3 → 5.7 | 39.5 → 38.3 → 12.3 | 50.4 → 34.0 → 5.6 | 54.0 → 37.6 → 9.6 |
| careers | 54.7 → 35.3 → 5.2 | 60.3 → 40.7 → 10.7 | 48.3 → 41.6 → 5.1 | 56.5 → 49.0 → 13.5 |

Đọc bảng:
- **1440, A:** các hero toàn khung (member, portfolio, advisory, careers, about) giảm từ 55-58% (about 37%) xuống 33-38%, sát trang chủ (30%). phvsf và vnshine không giảm (39%) vì nửa trái vẫn là #0A3440 như trang chủ; phần "tối" giảm 6-10 điểm nhờ ảnh không còn phủ gradient.
- **1440, B:** còn 5-6% (chỉ dải trên cùng và nút Công cụ), nhẹ hơn trang chủ.
- **390, A:** about, phvsf, vnshine không giảm, vnshine còn tăng (48 → 63%) vì chữ xếp trên nền #0A3440 và ảnh chỉ còn ở dải dưới, giống trang chủ mobile (46,8%). Các trang dịch vụ giảm 8-13 điểm.
- **390, B:** 5-8%.

## Đánh giá ảnh hero (ảnh giờ xanh `r5_*_hero`, chưa đổi)

Số đo trên ảnh gốc: about độ sáng TB 0,48 (4% điểm ảnh tối); member 0,40 (10%); vnshine 0,30 (**47%** điểm ảnh tối, 3% điểm ảnh ấm cam/hồng ở các con số trên bảng điện).

| Trang | Ảnh | A (khung trên mảng #0B6274) | B (nền mist) |
|---|---|---|---|
| Về chúng tôi | `r5_about_hero`: phòng họp tầng cao giờ xanh, bàn trắng, sông Sài Gòn lên đèn | **Hợp.** Trời xanh cùng tông mảng #0B6274, đèn thành phố chỉ là vài điểm nhỏ. Giữ. | **Tạm được.** Giờ xanh sẫm cạnh nền mist tương phản mạnh, hơi nặng. Nên có bản ban ngày. |
| VNSHINE | `r5_vns_hero`: phòng tối, bảng điện chứng khoán xoá phông | **Chưa hợp.** Thẻ giá che gần hết ảnh, phần còn thấy là mảng tối và chữ số sáng cam/hồng (gần tông cam, trái luật màu). Phải hạ độ mờ xuống 60% mới dùng được. | **Không hợp.** Phòng tối là mảng nặng nhất trang cạnh nền mist; số cam/hồng. Cần ảnh ban ngày. |
| Quỹ thành viên | `r5_member_hero` (4:5): phòng họp giờ xanh, tài liệu đóng bìa | **Hợp.** Khung nhỏ trên mảng teal. Có thể giữ. | **Hơi tối** so với nền mist. Nên có bản ban ngày. |

### Ảnh cần tạo lại (Higgsfield, Nano Banana Pro, 2k trở lên; chưa tạo)

1. **VNSHINE, dùng cho B** (và nên dùng cho A): ban ngày, trắng và teal. Một chuyên viên trẻ Việt (28-35 tuổi, sơ mi trắng hoặc xanh nhạt, nhìn nghiêng hoặc từ lưng) làm việc trước màn hình lớn có biểu đồ đường màu teal, không số đọc được. Cửa kính nhìn ra HCMC ban ngày. Khung ngang 16:9 (hero hiển thị khoảng 1440×600). Chủ thể ở nửa phải khung (khoảng 55-95% ngang), nửa trái là tường hoặc trời sáng ít chi tiết để lớp mờ mist hoà vào. Với A, chủ thể đặt nửa trên bên phải: thẻ giá che vùng giữa và dưới. Không phòng tối, không chữ số cam/hồng, không be/nâu.
2. **Về chúng tôi, dùng cho B** (A không bắt buộc): cùng phòng họp tầng cao, đổi sang ban ngày: trời xanh nhạt, sông Sài Gòn, Landmark 81 hoặc Bitexco, bàn trắng có laptop và tài liệu. Có thể thêm 1-2 người trẻ ngồi xa, nhìn ra cửa sổ. Khung 4:3, hero hiển thị 1037×563 nên chủ thể (bàn và cửa sổ) nằm trong dải giữa 70% chiều cao và ở nửa phải; nửa trái là kính và tường sáng cho chữ.
3. **Quỹ thành viên, dùng cho B** (A giữ được): phòng họp hội đồng ban ngày, bàn tròn trắng, tài liệu đóng bìa và tablet như ảnh cũ, thêm 1-2 người trẻ nhìn nghiêng hoặc từ lưng, áo trắng hoặc xanh nhạt. Cửa sổ trời xanh nhạt. Khung 4:5 (cắt ngang thành 10:9 trên máy tính, 16:10 trên điện thoại), chủ thể ở giữa, giữ 80% chiều cao ở giữa.

Ghi chú: trang chủ và chân trang so từng điểm ảnh giữa bản build main và hai bản A, B (VI, EN, 1440, 390, cả trang): giống hệt (0 điểm ảnh khác).

