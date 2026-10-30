# Plan vòng 6 · website PHFM

- Lập: 30/10/2026 (Claude, theo yêu cầu của Rin). Chưa duyệt. Rin duyệt plan và trả lời mục "Cần hỏi Rin" trước khi `frontend` làm.
- Nguồn: 173 bình luận của Rin và đồng nghiệp trên bản demo cũ (133 bình luận Option E = `#o8`, 40 bình luận Option C = `#o5`). Option A, B, D bỏ qua theo quyết định của Rin.
- Đối chiếu từng bình luận với build `a203de4` (origin/main sau PR #33, ngày 30/10/2026): bấm thử, đo DOM, chụp ảnh. Chưa gồm PR #36 (R5-01, đang mở).
- Mỗi nhóm một nhánh `r6/<mã>`, một PR. CSS mới viết vào `src/parts/r6.css` (nạp sau `r4.css` và CSS vòng 5), vá template/logic ở `src/patches6.py` (tạo mới ở R6-01, đăng ký sau `PATCHES4` trong `PATCHES` của `src/patches.py`).

## Quyết định của Rin (áp dụng cho cả vòng)

1. Trang con về bố cục, cỡ chữ, khoảng cách của bản gốc (build commit `3131e7e`), màu theo phương án A của vòng 5. Bình luận về bố cục hay cỡ chữ vẫn áp lên bản gốc đó.
2. Đổi câu chữ: áp ngay ở bản VI, viết bản EN tương đương, ghi "chờ pháp chế". Bản 中文 không tự dịch (cô Helena duyệt).
3. File hoặc link ngoài chưa có: để `[placeholder]` và ghi vào bàn giao (`specs/dev-handoff.md`).
4. Trang chủ (`[data-hm]`) giữ nguyên. Bình luận về trang chủ xếp "Cần hỏi Rin", trừ lỗi rõ ở phần dùng chung (vd nút lệch hàng ở header).

## Kết quả phân loại 173 bình luận

| Trạng thái | Số bình luận |
|---|---|
| Đã xong (có trên build `a203de4`) | **120** |
| Cần làm | **31** |
| Cần hỏi Rin | **18** (11 câu hỏi, mục dưới) |
| Không còn áp dụng | **4** (#42, #46, #55, #137) |

Phần lớn bình luận đã được vòng 1 đến 5 và các lần cập nhật nội dung xử lý: câu chữ của Linh, Phương, Việt đã nằm trong `src/src_o8.html`; Tài liệu quỹ có lọc và tick chọn; Ban lãnh đạo bấm mở hộp thoại; Công cụ có ô nhập số; CTA Hướng dẫn có ảnh nền. Việc còn lại tập trung ở bảy chỗ: link EN/中文 ở Hướng dẫn VNSHINE, đường kẻ ngang giữa các khối (19 bình luận), khối Biểu mẫu, ghi chú số liệu, số liệu Về chúng tôi, tiêu đề cột Danh sách quỹ, nhãn hero PHVSF.

## Nhóm việc

Thứ tự đề xuất: merge PR #36, rồi R6-01, rồi các nhóm còn lại. R6-02 và R6-03 chỉ đụng template Hướng dẫn nên có thể làm song song với R6-01, nhưng R6-01 tạo khung `patches6.py` và `r6.css` nên các nhóm khác rebase sau R6-01.

| Mã | Trang | Việc cần làm | Bình luận | File đụng tới | Tiêu chí nghiệm thu |
|---|---|---|---|---|---|
| R6-01 | Mọi trang con có hero, Lịch sử hình thành, ô giá | Bố cục trang con về bản gốc, màu A (mục riêng bên dưới) | không có bình luận riêng; theo quyết định 1 | `src/patches4.py`, `src/parts/r4.css`, CSS vòng 5, `src/patches6.py` (mới), `src/parts/r6.css` (mới) | Chiều cao hero khớp bảng số đo của `3131e7e` (sai lệch ≤ 4px), màu theo A, QA xanh |
| R6-02 | Hướng dẫn VNSHINE (EN, 中文) | Hai thẻ "View details" và hai thẻ phương thức không còn `href="#so-cap"`/`#thu-cap`: bấm giữ nguyên `#/en/guideVnshine` và cuộn tới mục như bản VI | #34, #84 (2) | `src/patches6.py` (`rep()` các dòng 9143, 9152 và khối 中文 trong `src/src_o8.html`), `src/parts/site.js` nếu chặn chung `href^="#"` không phải `#/` | EN và 中文: bấm thẻ không đổi route, cuộn tới `#so-cap`, `#thu-cap`. QA xanh |
| R6-03 | Hướng dẫn PHVSF, Hướng dẫn VNSHINE, Học viện | (1) Nút "Tải về ↓" cho "Phiếu đăng ký mở tài khoản…" trong Hồ sơ cá nhân, thông báo "Tài liệu đang được cập nhật" khi chưa có file. (2) Bước 03 Giao dịch thứ cấp bản EN và 中文 có số "03" và đường vàng như bước 01, 02, bỏ "✓ Step 03". (3) Khối "Biểu mẫu" sau bước 04 ở Hướng dẫn PHVSF (4 biểu mẫu Quỹ mở PHVSF lấy từ dữ liệu trang Biểu mẫu). (4) Thẻ "Biểu mẫu" ở Học viện, dưới Thuật ngữ đầu tư, nối sang trang Biểu mẫu | #16, #30, #79, #81 (4) | `src/patches6.py`, `src/parts/r6.css`, `specs/dev-handoff.md` | Bước 03 ba bản ngôn ngữ cùng kiểu với bước 01, 02. Biểu mẫu bấm ra thông báo hoặc file. Không tràn ngang 390. Chữ mới ghi "chờ pháp chế" |
| R6-04 | PHVSF, VNSHINE, Danh sách quỹ | (1) Chữ "Chọn tất cả" bấm được cả dòng. (2) Ghi chú dưới bảng và biểu đồ thống nhất in nghiêng 12px, màu `--muted`. (3) Danh sách quỹ: tiêu đề cột "Giao dịch" và ô "Hằng ngày" một dòng, "Lợi nhuận từ đầu năm" cân với các cột khác (1440, 1280, 1024). (4) Nhãn nhỏ hero PHVSF: VI "QUỸ MỞ", EN "OPEN-ENDED FUND". Sau khi Rin trả lời: Q5 đến Q10 (loại tài liệu, thuật ngữ Shareholder Yield, nội dung từ phfm.vn) | #3, #50, #71, #100, #111 (5), sau Q: #72, #94, #98, #103, #106, #115, #116, #120, #130, #134, #166 | `src/patches6.py`, `src/parts/r6.css`, khoá `heroEyebrow` (dòng 6201) | Danh sách quỹ không còn tiêu đề cột xuống dòng. Hero PHVSF nhãn đúng 2 ngôn ngữ. Bấm chữ "Chọn tất cả" chọn 6/6 tài liệu |
| R6-05 | Về chúng tôi | Bốn số liệu đầu: ba số đầu lấy đúng chuỗi trang chủ (VI "+18 / năm hoạt động", "+2.000 / tỷ VND AUM", "4 / sản phẩm quỹ"; EN "18+ / years of operation", "2,000+ / bn VND AUM", "4 / fund products"); số thứ tư giữ, EN "88.45 bn VND". Sau khi Rin trả lời: Q3 (Lịch sử hình thành), Q4 (tên giá trị EN) | #64 (1), sau Q: #65, #66, #90 | `about.stats` (dòng 6362 `src/src_o8.html`), `src/patches6.py` | Ba số đầu giống trang chủ ở VI và EN. Không đổi số |
| R6-06 | Về chúng tôi, PHVSF, VNSHINE, Quỹ thành viên, Quản lý danh mục, Tư vấn, Tuyển dụng | Bỏ đường kẻ ngang 1px (`#D8E7EA`) ở đầu 19 khối Linh nêu (bảng bình luận, cột "Việc"). Giữ gạch vàng dưới tiêu đề hero và nhãn có đường kẻ. Sửa mẫu bằng `rep()`, chỉ dùng `!important` ở `r6.css` khi chuỗi style trùng nhiều chỗ. Làm sau Q1 và Q2 | #144 đến #148, #151 đến #155, #160 đến #165, #167, #170, #173 (19), sau Q2: #141, #142 | `src/patches6.py`, `src/parts/r6.css` | 19 chỗ không còn `border-top` 1px của section. Hai khối cạnh nhau vẫn phân biệt được bằng nền (xen kẽ nền của vòng 5). Không chồng chéo màu. QA xanh |

Không có nhóm "Góc nhìn, Công bố thông tin, Liên hệ, header, footer": các bình luận ở đó đã xong hoặc đang chờ Rin (Q2, Q11).

### Phụ thuộc và rủi ro xung đột

- R6-01 sửa `patches4.py` (gỡ `p_r4_01`, `p_fix20`, `p_r4_03`, `p_r4_04`), `r4.css` và CSS vòng 5. R6-04 (ô giá `.px-row`, hero trang quỹ), R6-05 (Lịch sử hình thành) và R6-06 (viền section, nền xen kẽ) cùng đụng các tệp này: làm sau khi R6-01 merge và rebase.
- R6-06 và R6-01 cùng đụng nền xen kẽ của PR #36. Nên chạy `qa/r5sections.js` (từ PR #36) trước và sau R6-06.
- R6-02, R6-03 chỉ thêm hàm vá mới, ít xung đột. Cả hai thêm hàm vào `patches6.py`: PR đến sau gộp `PATCHES6`, như cách đã làm ở vòng 4.
- R6-03 thêm khối vào hai trang Hướng dẫn: R6-01 cũng trả chiều cao hero của hai trang này (345px và 327px ở 1440). Chỉ đụng hero ở R6-01, khối Biểu mẫu nằm sau bước 04.
- Các câu hỏi chặn: R6-05 chờ Q3 và Q4; R6-04 chờ Q5 đến Q10 cho phần còn lại; R6-06 chờ Q1 và Q2. Phần "Cần làm" không phụ thuộc câu hỏi vẫn làm được.
- `specs/changelog.md`: mỗi PR nối dòng của mình vào mục "Vòng 6" (gộp khi xung đột, giữ cả hai dòng).

## R6-01 · Bố cục trang con về bản gốc, màu A

Làm sau khi merge PR #36 (R5-01). Mục tiêu: trang con có hình học của build commit `3131e7e` (bố cục, cỡ chữ, khoảng cách) và màu phương án A của vòng 5. Không đụng trang chủ (`[data-hm]`) và footer (`.ft`).

Tham chiếu hình học: build của `3131e7e`. Dựng bằng:

```bash
mkdir /tmp/r6ref && git archive 3131e7e | tar -x -C /tmp/r6ref && python3 /tmp/r6ref/src/build.py
# -> /tmp/r6ref/dist/phfm-website.html ; so với dist của nhánh bằng biến HTML=... của qa/shot.js, qa/insp.js
```

Số đo chiều cao hero (px, bản VI, đo ở `3131e7e`, hero là `section` chứa `h1`). Bản hiện tại (`a203de4`) để so:

| Rộng | Trang | `3131e7e` (đích) | `a203de4` (hiện tại) |
|---|---|---|---|
| 1440 | Về chúng tôi, Học viện, Tuyển dụng | 775 | 563, 560, 625 |
| 1440 | PHVSF, VNSHINE | 775 | 600 |
| 1440 | Quỹ thành viên, Quản lý danh mục, Tư vấn | 795 | 625 |
| 1440 | Hướng dẫn PHVSF, Hướng dẫn VNSHINE | 345, 327 | 401, 383 |
| 1366 và 1280 | Về chúng tôi | 952 | 560 |
| 1366 | Học viện | 1074 | 560 |
| 1280 | Học viện | 1070 | 560 |
| 1024 | Về chúng tôi, PHVSF, VNSHINE | 952, 803, 844 | đo lại khi làm |
| 1024 | Quỹ thành viên, Học viện, Tuyển dụng | 803, 915, 803 | đo lại khi làm |
| 390 | Về chúng tôi, PHVSF, VNSHINE | 944, 996, 1197 | đo lại khi làm |
| 390 | Quỹ thành viên, Quản lý danh mục, Tư vấn | 1169, 1087, 1056 | đo lại khi làm |
| 390 | Học viện, Tuyển dụng, Hướng dẫn PHVSF, Hướng dẫn VNSHINE | 803, 803, 468, 489 | đo lại khi làm |

Dùng `qa/r5hero.js` và `qa/r5herocmp.py` (từ PR #36) để đo cả hai build, lưu số vào `qa/review/r6-01/`.

### Gỡ (các thay đổi bố cục của vòng 4 và 5)

| Mục | Thay đổi cần gỡ | Chỗ sửa |
|---|---|---|
| R4-01 chiều cao hero | Trả `min-height:min(900px, calc(100vh - …))` và padding gốc của hero About, PHVSF, VNSHINE, Quỹ thành viên, Danh mục, Tư vấn, Học viện, Tuyển dụng. Bỏ luật `.hero-sub`, `.hero-in`, `.hero-pic`, `.hero-nar` trong `r4.css`. Trả khung cắt ảnh hero dịch vụ từ 10/9 về 4/5 (mobile 16/10 về gốc), mobile About ảnh dưới chữ về gốc (không ép 320px), khoảng breadcrumb → nội dung về gốc | `p_r4_01` trong `src/patches4.py`, `src/parts/r4.css` |
| #20 ngưỡng 1280 | `heroNarrow` về `vw < 1400` (hàm `p_fix20`). Giữ `text-wrap:pretty` của `.ac-h1` nếu không ảnh hưởng hình học | `p_fix20` |
| R4-03 Lịch sử hình thành | Gỡ 3 cột, trục ngang vàng, bố cục năm lớn; về khung thẻ trắng cao bằng nhau của bản gốc (có Q3: nếu Rin giữ thiết kế mới cho khối này thì bỏ mục này) | `p_r4_03`, `r4.css` |
| R4-04 ô giá | Gỡ lưới `.px-row`, về hàng `flex-wrap` gốc (Giá đóng cửa, NAV/CCQ, Ngày). Số liệu, bảng hiệu quả và ô "—" ở cột 3 tháng giữ nguyên (Rin đã quyết giữ) | `p_r4_04`, `r4.css` |
| Vòng 5: cỡ chữ Lịch sử hình thành | Năm giai đoạn 28–32px, tên 18px, năm mốc và sự kiện 15px: trả về cỡ gốc (năm 40–44px, theo bản gốc của `3131e7e`) | CSS của R5-01 |
| R4-09 hero Hướng dẫn | Hero cao thêm 56px: trả 345px và 327px (1440). Lớp mờ trắng rộng và `min(720px, 60vw)` giữ nếu ảnh mới còn cần để đạt tương phản ≥ 4.5:1 | `src/parts/r4.css` |

### Giữ (không gỡ)

- Màu phương án A của vòng 5: hero chéo `#0A3440` / `#0B6274`, thanh mục con mist, xen kẽ nền section, khối nhấn, menu một gạch vàng (#37).
- Sửa lỗi, không phải bố cục: chữ Hán 新 速 實 簡 (R4-05), lưới Giá trị cốt lõi ≤760px (#17), 中文 Lịch sử hình thành (#27), mô tả hero EN/中文 hết dính chữ (#24), "chữ không bị ép" của vòng 5 (script `fit` ép `letter-spacing` âm), QA `NaN` (#18), nội dung dữ liệu, dòng "Số liệu minh hoạ".
- Bộ ảnh `r5_*` (R4-09), alt đã đổi, ảnh cũ đã xoá. Khung cắt `object-position` của từng ảnh cần chỉnh lại cho khung 4/5 gốc: xem từng ảnh sau khi gỡ.
- Công cụ QA vòng 5 (`r5*.js`, `r5*.py`, `qa/review/r5-color-a/`).

### Rủi ro cần Rin biết

- Về chúng tôi và Học viện ở 1280 đến 1399: hero lại cao 950 đến 1074px (layout hẹp, ảnh dưới chữ). Đây là lỗi issue #20 đã sửa ở vòng 4. Về bản gốc nghĩa là lỗi này quay lại.
- 1440: hero cao 775–795px, mép trên khối kế tiếp nằm dưới màn hình đầu (lý do gốc của R4-01).
- Ô giá: hàng chỉ số lại có thể xuống hàng và để khoảng trống (lý do gốc của R4-04). Issue #22 (ô giá che ảnh hero PHVSF) có thể nặng hơn.
- Lịch sử hình thành: Linh đã yêu cầu thiết kế lại (#65, #90). Xem Q3.
- Ảnh hero mới `r5_*` được chọn cho khung 10/9: có thể cần cắt lại ở khung 4/5, hoặc đổi vị trí chủ thể.
- Bản 中文: chiều cao hero cần đo riêng (issue #31 hero trang quỹ 中文 hẹp hơn 44px).

### Nghiệm thu R6-01

Số đo hero khớp bảng trên (≤ 4px) ở 1440, 1366, 1280, 1024, 390, VI và EN. Màu theo A (chạy `qa/r5contrast.js`, tương phản chữ ≥ 4.5:1). `node qa/qa.js` xanh toàn site. Ảnh trước/sau 1440 và 390 ở `qa/review/r6-01/`.

## Cần hỏi Rin

Mỗi câu có đề xuất. Chưa trả lời thì nhóm tương ứng chỉ làm phần "Cần làm" đã rõ.

1. **"Line" của Linh là đường kẻ nào?** Mình hiểu là đường kẻ ngang 1px giữa các khối (`border-top` của section, màu `#D8E7EA`). Linh nêu 19 chỗ (R6-06). Gạch vàng dưới tiêu đề hero và đường kẻ cạnh nhãn nhỏ không bị nêu. CLAUDE.md coi đường kẻ mảnh là phong cách PHFM. Chọn: (a) bỏ đúng 19 chỗ Linh nêu, giữ chỗ khác (đề xuất); (b) bỏ mọi đường kẻ giữa khối ở trang con; (c) giữ nguyên.
2. **Trang Liên hệ (#141, #142): "line trên" và "line" ở nút Gửi yêu cầu là đường nào?** Bản gốc Liên hệ không có đường kẻ trang trí: chỉ có viền dưới header và viền khung form "Gửi yêu cầu". Chọn: (a) bỏ viền dưới header ở trang Liên hệ; (b) bỏ viền khung form; (c) bỏ cả hai; (d) không làm, vì Linh nhìn bản C cũ.
3. **Lịch sử hình thành (#65, #90): Linh nói "chưa phù hợp, cần design lại". Rin lại muốn về bản gốc.** Vòng 4 đã làm 3 cột nền teal; vòng 5 đổi nền mist, cỡ chữ nhỏ. Chọn: (a) giữ thiết kế 3 cột của vòng 4 riêng cho khối này (đề xuất, vì Linh đã yêu cầu thiết kế lại và R4-03 là câu trả lời); (b) về khung thẻ của bản gốc; (c) Rin gửi lại ý Linh muốn thiết kế thế nào.
4. **Tên bốn giá trị ở bản EN (#66):** Linh muốn dùng chữ tiếng Anh thay "Tân, Tốc, Thực, Giản". Chọn: (a) đề xuất "Innovation, Agility, Integrity, Simplicity" (chờ pháp chế/thương hiệu); (b) Rin gửi tên EN chính thức của PHFM; (c) giữ tên Việt kèm chữ Hán (không đổi). Bản 中文 theo issue #34, không tự dịch.
5. **Thuật ngữ Shareholder Yield (#54, #120, #166, #77; issue #9):** Linh và Phương dùng "Lợi suất Cổ đông" và đặt tiêu đề "Chiến lược lợi suất cổ đông". Brand-rules đã chốt "Tỷ suất Lợi nhuận Cổ đông". Web đang dùng "Lợi suất Cổ đông". Chọn: (a) đổi toàn site sang "Tỷ suất Lợi nhuận Cổ đông" (theo brand-rules, đề xuất); (b) giữ "Lợi suất Cổ đông" như Linh và sửa brand-rules; (c) dùng "Chiến lược lợi suất cổ đông" ở tiêu đề (như #120) và "Tỷ suất…" ở thân bài.
6. **Câu hero VNSHINE "Quỹ ETF đầu tiên tại Việt Nam được xây dựng theo Chiến lược Lợi suất Cổ đông" (#166):** "đầu tiên" là tuyên bố cần pháp chế xác nhận; brand-rules nói PHFM là quỹ tiên phong, không viết như độc quyền. Chọn: (a) giữ nguyên chữ của Linh, ghi "chờ pháp chế xác nhận 'đầu tiên'"; (b) đổi thành "Một trong những quỹ ETF tiên phong tại Việt Nam áp dụng Chiến lược Lợi suất Cổ đông" (đề xuất); (c) Rin có tài liệu chứng minh "đầu tiên".
7. **Dòng "Số liệu minh hoạ, cập nhật đến ngày…" (#72, nối #49, #109):** Linh muốn bỏ phần ngày. Hero đã bỏ "Số liệu tại ngày". Các khối bên dưới (Kết quả hoạt động, Lịch sử NAV, Thông tin giao dịch, Danh sách quỹ) còn dòng này; brand-rules bắt giữ đến khi có số thật từ CMS. Chọn: (a) giữ, chuyển thành chữ nhỏ in nghiêng (khớp #50, đề xuất); (b) giữ "Số liệu minh hoạ", bỏ phần ngày; (c) bỏ hẳn (chỉ khi dev đã nối số thật).
8. **Loại tài liệu ở trang quỹ (#94, #98, #115, #116, #130, #134):** Linh đưa hai danh sách. Danh sách A (#94, #98, #134): Báo cáo ngày, tuần / Báo cáo tài chính / Báo cáo hoạt động tháng / Factsheets / Bản cáo bạch / Điều lệ quỹ / Thông tin quỹ / Giấy phép / Khác (9 loại, không có Biểu mẫu). Danh sách B (#116): Thông báo quỹ / Điều lệ quỹ / Bản cáo bạch / Báo cáo tài chính / Báo cáo hoạt động tháng / Báo cáo NAV ngày, tuần / Biểu mẫu / Factsheet (8 loại, giống trang Công bố thông tin), trong khi #115 và #130 nói "biểu mẫu bỏ riêng". Hiện lọc chỉ hiện loại đang có tài liệu. Chọn: (a) dùng danh sách A cho cả hai quỹ, hiện đủ 9 loại kể cả loại chưa có file (ghi "Chưa có tài liệu"), bỏ "Mẫu đăng ký" và "Bộ tài liệu thành viên lập quỹ" khỏi tài liệu quỹ, để Biểu mẫu ở trang riêng (đề xuất); (b) danh sách B cho trang Công bố thông tin, A cho trang quỹ; (c) giữ như hiện tại.
9. **PHVSF: "THAY ĐỔI bị mất update cũ, bổ sung lại" (#106):** cột "Thay đổi" của Lịch sử NAV đã có (theo ngày). Mình không mở được phfm.vn nên không biết phần "update cũ" là gì. Rin gửi nội dung hoặc ảnh chụp trang `phfm.vn/vi/product-service/performance` và chỉ phần cần bổ sung (bảng hiệu quả theo kỳ? tin cập nhật hằng tháng?). Nếu là số liệu thật thì để `[placeholder]` chờ nguồn.
10. **PHVSF bản EN (#103):** Linh muốn lấy đúng nội dung EN gốc ở `phfm.vn/product-service/overview`. Mình không mở được phfm.vn. Rin dán nội dung EN (tên quỹ, loại quỹ, ngân hàng giám sát, phí…) để thay phần "Thông tin quỹ" EN. Hiện EN đã đổi tên quỹ và đoạn mô tả theo Linh.
11. **Trang chủ (2 bình luận của Option C):** (#2) thêm ảnh nền cho từng sản phẩm đầu tư ở "Giải pháp cho từng mục tiêu đầu tư"; (#138) bỏ đường kẻ ở "Bắt đầu tích luỹ từ hôm nay". Trang chủ Teal Vanguard Rin yêu cầu giữ nguyên. Chọn: (a) không làm (đề xuất); (b) làm riêng một PR cho trang chủ.

## Placeholder và bàn giao (Rin gửi file/link, hoặc ghi cho dev)

File và link ngoài chưa có, để `[placeholder]` và nút hiện "Tài liệu đang được cập nhật":

1. Phiếu đăng ký mở tài khoản giao dịch chứng chỉ quỹ mở (PDF), ở Hướng dẫn PHVSF (#16, #81) và trang Biểu mẫu.
2. Các biểu mẫu trang Biểu mẫu: Phiếu đăng ký mua/bán CCQ mở; Mẫu thông tin bổ sung nhà đầu tư tổ chức; Biểu mẫu FATCA và AML; Phiếu đăng ký quỹ thành viên; Biểu mẫu đặt lệnh hoán đổi (thành viên lập quỹ).
3. Tài liệu quỹ nếu Rin chọn Q8(a): Factsheet, Thông tin quỹ, Giấy phép của PHVSF và VNSHINE.
4. File danh mục cơ cấu (PCF) cho nút "Tải danh mục cơ cấu (PCF)", file CSV/Excel Lịch sử NAV.
5. Nội dung từ phfm.vn: `product-service/overview` (EN) và `product-service/performance` (Q9, Q10).
6. Nguồn NAV thật và ngày `PHFM_ASOF` do CMS cấp (B01): ngày số liệu nhảy theo ngày dữ liệu, không theo ngày mở trang. Ghi cho dev.
7. Tên EN chính thức của bốn giá trị (Q4).
8. Nội dung Điều khoản sử dụng và Chính sách bảo mật: chờ pháp chế.

Chữ mới chờ pháp chế (áp ngay ở VI, EN tương đương, 中文 không dịch):

- R6-04: nhãn hero PHVSF "QUỸ MỞ" / "OPEN-ENDED FUND".
- R6-05: nhãn số liệu Về chúng tôi theo trang chủ (không có chữ mới, chỉ đồng bộ).
- R6-03: khối "Biểu mẫu" (VI "Tải các biểu mẫu giao dịch và hồ sơ cần thiết khi đầu tư cùng PHFM." / EN "Download the transaction forms and documents you need to invest with PHFM."), nút "Tải về" / "Download".
- Mọi câu của Linh, Phương, Việt đã áp trên build vẫn chờ pháp chế duyệt trước go-live (brand-rules).

## Lỗi phụ ngoài bảng (ghi issue, hỏi Rin trước khi sửa)

1. Form Quỹ thành viên, Quản lý danh mục, Tư vấn: "Chính sách bảo mật" trong dòng đồng ý là chữ (`span`), không bấm được. Trang Liên hệ thì là link.
2. VNSHINE (EN): "Fund information" cùng thứ tự với bản VI (A đến Z theo nhãn Việt), nên EN không theo A đến Z. #117 chỉ nêu bản VI.
3. Tên "Chứng khoán Thành phố Hồ Chí Minh" ghi "Hồ Chí Minh" ở trang VNSHINE và "Thành phố Hồ Chí Minh" ở Hướng dẫn VNSHINE (VI), nên thứ tự A đến Z khác nhau giữa hai trang.
4. Danh sách quỹ còn dòng "+ Quỹ mới thêm trong CMS sẽ tự hiện ở đây" (đã có issue #39).
5. Trang Công bố thông tin bản EN không hiện nhãn nhỏ (trùng tiêu đề), nên không có đường kẻ cạnh nhãn như bản VI (#136 chỉ nêu VI).

## Bảng 173 bình luận

Nhóm "(sau Qn)": việc làm sau khi Rin trả lời câu hỏi n. Cột "Trang" là trang web hiện tại ứng với tiêu đề hero lúc Rin bình luận. Cột "Vị trí" bị cắt ở 60 ký tự như bản gốc.

| # | Option | Trang | Vị trí | Bình luận | Trạng thái | Việc / lý do | Nhóm |
|---|---|---|---|---|---|---|---|
| 1 | C | Trang chủ | PHFM Trading | button bị lỗi lệch hàng so với thanh menu | Đã xong | Header dùng chung: nút PHFM Trading và menu cùng tâm dọc (84px) ở 1280, 1440, 1920. Dưới 1280 header thu thành menu di động | - |
| 2 | C | Trang chủ | Giải pháp cho từng mục tiêu đầu tư | đề xuất set thêm background hình ảnh cho từng sản phẩm đầu tư | Cần hỏi Rin | Trang chủ giữ nguyên. Hỏi Rin ở câu 11 | (sau Q11) |
| 3 | E | Công bố thông tin | Chọn tất cả | cân nhắc bỏ button này vì ko bấm được chọn tất cả mà ô ngày mục Tài liệu lại chọn được tất cả. Hoặc giữ button này thì bỏ ô ngày chỗ Tài liệu | Cần làm | Trang Công bố thông tin hiện không còn nút "Chọn tất cả" (chỉ còn ô tick ở đầu cột, chạy tốt). Ở trang quỹ, chữ "Chọn tất cả" chưa bấm được, chỉ ô tick bấm được: cho cả dòng (chữ + ô) bấm được. Mẫu `selAll` trong `src/src_o8.html` (vùng Tài liệu quỹ), vá bằng `src/patches6.py` | R6-04 |
| 4 | E | Trang chủ | PHFM Trading | button bị lỗi lệch hàng so với thanh menu | Đã xong | Header dùng chung: nút PHFM Trading và menu cùng tâm dọc (84px) ở 1280, 1440, 1920. Dưới 1280 header thu thành menu di động | - |
| 5 | E | Trang chủ | TẢI PHFM MOBILE | chưa link sang trang tải App PHFM Mobile | Đã xong | Trang chủ: nút "Tải PHFM Mobile" trỏ Google Play. Footer có App Store và Google Play | - |
| 6 | E | Trang chủ | Copyright © 2026 Phu Hung Fund Management. Bảo lưu mọi quyền | Chưa link sang các trang điều khoản | Đã xong | Footer: "Điều khoản sử dụng", "Chính sách bảo mật", "Biểu mẫu" trỏ trang riêng (#/vi/terms, #/vi/privacy, #/vi/forms). Nội dung hai trang điều khoản ghi "chờ pháp chế" | - |
| 7 | E | Góc nhìn & Tin tức | BÁO CÁO CHIẾN LƯỢC · 01.10.2026 Triển vọng thị trường quý IV | đề xuất thêm 1 thanh tìm kiếm bài viết | Đã xong | Có ô "Tìm bài viết…" ở Góc nhìn & Tin tức | - |
| 8 | E | Góc nhìn & Tin tức | BÁO CÁO THỊ TRƯỜNG Đăng ký để nhận Báo cáo thị trường qua em | đề xuất đổi background nền kem thành 1 hình ảnh thực nào đó và phân bổ màu chữ, hiệu ứng lại sao cho nổi bật chữ | Đã xong | Khối đăng ký nhận Báo cáo thị trường dùng ảnh nền teal, chữ trắng, nút vàng | - |
| 9 | E | Góc nhìn & Tin tức | GÓC NHÌN | bỏ phần này, chỉ để ngày | Đã xong | Nhãn "Góc nhìn" đã bỏ, bài chỉ còn ngày. Các nhãn khác (Báo cáo chiến lược, Kiến thức đầu tư…) còn, Linh không nêu | - |
| 10 | E | Góc nhìn & Tin tức | Tóm tắt diễn biến thị trường và góc nhìn của đội ngũ đầu tư | Cập nhật diễn biến thị trường và nhận định từ đội ngũ đầu tư PHFM, gửi định kỳ trực tiếp đến hộp thư của bạn. | Đã xong | Đã dùng đúng câu của Linh | - |
| 11 | E | Học viện | Giao dịch sơ cấp và giao dịch thứ cấp chứng chỉ quỹ ETF trên | Đề xuất đôi thành: " Bạn muốn đầu tư ETF? Khám phá quy trình đầu tư và các tài liệu cần thiết tại đây. | Đã xong | Thẻ VNSHINE ở Học viện đã dùng đúng câu của Linh | - |
| 12 | E | Học viện | Kiến thức nền tảng về quỹ mở và ETF, viết cho người mới bắt | Đổi thành: "Khám phá kiến thức về quỹ mở, ETF và các nguyên tắc đầu tư dành cho người mới bắt đầu." | Đã xong | Đã dùng đúng câu của Linh (VI). Bản EN ở #56 | - |
| 13 | E | Học viện | Hiểu trước khi đầu tư | Đổi thành: Hiểu đúng trước khi đầu tư | Đã xong | Tiêu đề Học viện nay là "Hiểu đúng trước khi đầu tư" | - |
| 14 | E | Học viện | Mở tài khoản, đặt lệnh, chuyển tiền và xác nhận giao dịch ch | Đề xuất đổi thành: "Bạn muốn đầu tư quỹ mở? Khám phá quy trình đầu tư và các tài liệu cần thiết tại đây. | Đã xong | Thẻ PHVSF ở Học viện đã dùng đúng câu của Linh | - |
| 15 | E | Hướng dẫn PHVSF (EN) | HOW TO INVEST How to invest in the PHVSF open-ended fund 4 s | Bị lỗi có 2 line | Đã xong | Hero Hướng dẫn PHVSF (EN) chỉ còn một gạch vàng dưới tiêu đề (đo ở build a203de4 và 3131e7e) | - |
| 16 | E | Hướng dẫn PHVSF | Phiếu đăng ký mở tài khoản giao dịch chứng chỉ quỹ mở. | Đính kèm file Phiếu đăng ký | Cần làm | Mục "Phiếu đăng ký mở tài khoản giao dịch chứng chỉ quỹ mở" trong Hồ sơ cá nhân: thêm nút "Tải về ↓". Chưa có file: dùng thông báo "Tài liệu đang được cập nhật" như trang Biểu mẫu. [placeholder] file PDF, ghi vào `specs/dev-handoff.md` | R6-03 |
| 17 | E | Hướng dẫn PHVSF | Biểu mẫu giao dịch → | Đang trỏ vào Trang Công bố thông tin. Phải trỏ vào trang Biểu mẫu mới đúng | Đã xong | Nút "Biểu mẫu giao dịch →" mở #/vi/forms (đã bấm thử) | - |
| 18 | E | Hướng dẫn PHVSF | 01 BƯỚC 01 Mở tài khoản | Xem lại các đường link đang gắn, tất cả đều đang trỏ vào homepage | Đã xong | Bước 01 đến 04 cuộn đúng tới từng mục (VI, EN đã bấm thử). Không còn nhảy về trang chủ | - |
| 19 | E | Hướng dẫn PHVSF | Biểu mẫu giao dịch | Đang trỏ vào trang Công bố thông tin -> Sai chỗ | Đã xong | Hai liên kết "Biểu mẫu giao dịch" mở #/vi/forms | - |
| 20 | E | Hướng dẫn PHVSF | trước 14h30 ngày T-1 | ...trước 14h30 ngày T-1 cho Ngày Giao Dịch (Ngày T) | Đã xong | Đã dùng đúng câu của Linh: "…trước 14h30 ngày T-1 cho Ngày Giao Dịch (Ngày T)" | - |
| 21 | E | Hướng dẫn PHVSF | Sau khi hoàn tất việc đặt lệnh và chuyển tiền theo đúng thời | Chỉnh lại kích cỡ nội dung sao cho đồng bộ với ở trên | Đã xong | Chữ bước 04 là 16px, bằng chữ dẫn của bước 01 và 03 | - |
| 22 | E | Hướng dẫn PHVSF | Thời gian giao dịch, thời hạn nhận lệnh và các điều kiện liê | In nghiên, kích cỡ nhỏ xuống cho phân biệt với tiêu đề và nội dung | Đã xong | Ghi chú "Thời gian giao dịch…" đã in nghiêng 14px, nhạt hơn nội dung | - |
| 23 | E | Hướng dẫn PHVSF | BẮT ĐẦU ĐẦU TƯ | Đổi thành: "Bắt đầu đầu tư hôm nay, hướng đến mục tiêu ngày mai" | Đã xong | Đã dùng đúng câu của Linh | - |
| 24 | E | Hướng dẫn PHVSF | Sẵn sàng đầu tư vào Quỹ mở PHVSF? | Đổi thành: "Sẵn sàng đồng hành cùng PHVSF trên hành trình tích lũy tài sản?" | Đã xong | Đã dùng đúng câu của Linh | - |
| 25 | E | Hướng dẫn PHVSF | Mở tài khoản và đặt lệnh trực tuyến trên ứng dụng PHFM Mobil | Đổi thành: "Mở tài khoản và bắt đầu đầu tư vào Quỹ mở PHVSF dễ dàng, thuận tiện ngay trên PHFM Mobile hoặc PHFM Trading." | Đã xong | Đã dùng đúng câu của Linh | - |
| 26 | E | Hướng dẫn PHVSF | HƯỚNG DẪN ĐẦU TƯ Hướng dẫn đầu tư Quỹ mở PHVSF 4 bước đầu tư | Bị lỗi có 2 line | Đã xong | Như #15 | - |
| 27 | E | Hướng dẫn PHVSF | BẮT ĐẦU ĐẦU TƯ Sẵn sàng đầu tư vào Quỹ mở PHVSF? Mở tài khoả | Visualize lại, thêm hình background, hiệu ứng,... / Button chỉnh kích cỡ vừa đủ, có thể dồn thành 1 hàng dọc bên phải | Đã xong | Khối CTA có ảnh nền, tiêu đề, nút App Store / Google Play / PHFM Trading xếp cột bên phải, nút vừa chữ | - |
| 28 | E | Hướng dẫn VNSHINE | LỆNH HOÁN ĐỔI MUA TỐI THIỂU 01 lô chứng chỉ quỹ, tương đương | visualize và chỉnh lại hai ô này sao cho phân biệt được giữa title, subtitle và nội dung | Đã xong | Hai ô lệnh hoán đổi đã phân biệt nhãn nhỏ, số lô và số đơn vị quỹ (VNSHINE guide) | - |
| 29 | E | Hướng dẫn VNSHINE | THÔNG TIN GIAO DỊCH QUY ĐỊNH | Bảng này cũng chỉnh lại kích cỡ chữ | Đã xong | Bảng "Thông tin giao dịch" có hàng tiêu đề riêng, hàng "14:40 ngày T" nổi bật | - |
| 30 | E | Hướng dẫn VNSHINE | BƯỚC 03 | ô này bị lỗi, ko đồng bộ định dạng so với 2 ô trước | Cần làm | Bản EN (và 中文) bước 03 của Giao dịch thứ cấp khác hai bước trước: ô tròn hiện dấu ✓ và nhãn "Step 03", không có số "03" và đường vàng như bước 01 và 02. Mẫu `<li>` có "✓" ở `src/src_o8.html` (khoảng dòng 9073 EN, 9280 中文). Sửa cho giống bước 01 và 02. Bản VI đã đúng | R6-03 |
| 31 | E | Hướng dẫn VNSHINE | Hoạt động giao dịch và thanh toán được thực hiện theo quy đị | Chỉnh cỡ chữ nhỏ lại, in nghiên, background màu nhạt hơn hoặc bỏ nền kem | Đã xong | Ghi chú "Hoạt động giao dịch và thanh toán…" đã in nghiêng, nhỏ, không có nền | - |
| 32 | E | Hướng dẫn VNSHINE | BẮT ĐẦU ĐẦU TƯ Cần tư vấn thêm về VNSHINE ETF? Đội ngũ PHFM | Visualize lại, thêm hình background, hiệu ứng,... / Button chỉnh kích cỡ vừa đủ, có thể dồn qua bên phải | Đã xong | Như #27 | - |
| 33 | E | Hướng dẫn VNSHINE | Cần tư vấn thêm về VNSHINE ETF? | Đổi thành: " Tìm hiểu thêm về VNSHINE ETF cùng PHFM" | Đã xong | Đã dùng đúng câu của Linh: "Tìm hiểu thêm về VNSHINE ETF cùng PHFM" | - |
| 34 | E | Hướng dẫn VNSHINE | PHƯƠNG THỨC 02 | Link bị lỗi | Cần làm | Bản VI chạy. Bản EN và 中文: hai thẻ "Xem chi tiết / View details" (và 2 thẻ phương thức) còn `href="#so-cap"`, `href="#thu-cap"` nên bấm vào mất đường dẫn, nhảy về trang chủ. Cần cuộn mượt như VI và giữ `#/en/guideVnshine`. Các dòng 9143 và 9152 `src/src_o8.html` (EN, 中文), `src/parts/site.js` đã chặn `href="#"` nhưng không chặn `#so-cap`. Ghi thêm: mở issue riêng sau khi Rin duyệt | R6-02 |
| 35 | E | Hướng dẫn VNSHINE | PHFM Trading | Button đang bị lệch hàng so với thanh menu | Đã xong | Header dùng chung: nút PHFM Trading và menu cùng tâm dọc (84px) ở 1280, 1440, 1920. Dưới 1280 header thu thành menu di động | - |
| 36 | E | Về chúng tôi | Ông Winston tốt nghiệp Cử nhân Kinh tế tại Đại học Quốc gia | Đề xuất thêm effect dấu +,- để ng đọc mở ra hoặc thu gọn text lại cho đỡ nhiều chữ (áp dụng cho cả 3 ô) | Đã xong | Thẻ Ban lãnh đạo chỉ hiện tên và chức danh. Bấm thẻ mở hộp thoại thông tin chi tiết (áp cho cả 3 thẻ) | - |
| 37 | E | Tuyển dụng (EN) | 01 Learn from practice Work directly with an experienced tea | Visualize + thêm hình ảnh vào cho sinh động, bắt mắt | Đã xong | Bốn thẻ văn hóa (EN) đã có ảnh riêng | - |
| 38 | E | VNSHINE (EN) | Fund | Đổi thành mã quỹ FUEPHVNS (cho cả 3 ver ngôn ngữ) | Đã xong | Hero VNSHINE dùng mã FUEPHVNS (VI, EN). Bản 中文 cô Helena duyệt | - |
| 39 | E | VNSHINE (EN) | CASH DIVIDEND | bỏ | Đã xong | Ba thẻ chiến lược không còn nhãn tiếng Anh CASH DIVIDEND, LOW DILUTION, DEBT REDUCTION | - |
| 40 | E | VNSHINE (EN) | LOW DILUTION | bỏ | Đã xong | Như #39 | - |
| 41 | E | VNSHINE (EN) | DEBT REDUCTION | bỏ | Đã xong | Như #39 | - |
| 42 | E | VNSHINE (EN) | Primary market: authorised participants (APs) exchange ETF c | visualize lại 3 ô này | Không còn áp dụng | Ba ô Giao dịch sơ cấp / thứ cấp / Lưu ý ở trang VNSHINE đã bỏ theo #127. Nội dung này nằm ở trang Hướng dẫn VNSHINE | - |
| 43 | E | PHVSF | Ông Nguyễn Hoài Sơn có hơn 20 năm kinh nghiệm trong lĩnh vực | Đề xuất thêm effect dấu +,- để ng đọc mở ra hoặc thu gọn text lại cho đỡ nhiều chữ (áp dụng cho cả 3 ô) | Đã xong | Ban điều hành quỹ PHVSF: bấm thẻ mở hộp thoại, chữ không còn dài trên trang | - |
| 44 | E | VNSHINE | Lịch sử NAV | thêm mục chọn ngày | Đã xong | Lịch sử NAV VNSHINE có ô chọn ngày Từ ngày / Đến ngày và nút "Xem thêm" | - |
| 45 | E | VNSHINE | VỀ PHFM SẢN PHẨM & DỊCH VỤ ▼ CÔNG BỐ THÔNG TIN GÓC NHÌN CHUY | thành menu chính và sub-menu ở dưới đang bị chồng chéo lên nhau | Đã xong | Header (sticky 60px) và thanh mục con (từ 61px) không chồng nhau ở 390, 768, 1024, 1280, 1440 | - |
| 46 | E | VNSHINE | Giao dịch sơ cấp: thành viên lập quỹ (AP) hoán đổi lô ETF lấ | visualize lại 3 ô này | Không còn áp dụng | Như #42 | - |
| 47 | E | VNSHINE | Tải xuống | đề xuất đề dấu download là được | Đã xong | Mỗi tài liệu có icon tải xuống thay chữ "Tải xuống" | - |
| 48 | E | VNSHINE | Xem hướng dẫn đầu tư chi tiết | thu nhỏ button này lại, hơi to | Đã xong | Nút "Xem hướng dẫn đầu tư chi tiết →" là nút viền mảnh 14px, vừa chữ | - |
| 49 | E | VNSHINE | Số liệu tại ngày 03.10.2026. Hiệu suất trong quá khứ không đ | bỏ câu "Số liệu tại ngày...", giữ phần sau | Đã xong | Hero đã bỏ "Số liệu tại ngày…", chỉ còn "Hiệu suất tính trên NAV/CCQ. Hiệu suất trong quá khứ không đảm bảo kết quả trong tương lai." Dòng "Số liệu minh hoạ, cập nhật đến ngày…" ở các khối bên dưới giữ theo brand-rules (câu hỏi 7) | - |
| 50 | E | VNSHINE | Số liệu tại ngày 03.10.2026. Hiệu suất trong quá khứ không đ | để xuất chỉnh định dạng các note thành in nghiên, thu nhỏ cỡ chữ xuống 1 tí nữa | Cần làm | Các ghi chú dưới bảng và biểu đồ ("* Tất cả các giao dịch…", "Số liệu minh hoạ…", "Sai lệch so với chỉ số…", "Hiệu suất tính trên…"): thống nhất in nghiêng, 12px, màu `--muted`. Hiện "Số liệu minh hoạ" chưa nghiêng. Vẫn giữ nội dung "Số liệu minh hoạ" (brand-rules, câu hỏi 7). `src/parts/r6.css` | R6-04 |
| 51 | E | VNSHINE | CASH DIVIDEND | Xem lại bản EN ở cả ba ô, để như vầy qua bản EN thì 2 dòng lặp chữ | Đã xong | Bản EN ba thẻ chiến lược không còn lặp chữ | - |
| 52 | E | VNSHINE | Trên thị trường chứng khoán Việt Nam, ba vấn đề khá phổ biến | Trên thị trường chứng khoán Việt Nam, ba vấn đề phổ biến tại nhiều doanh nghiệp niêm yết bao gồm dòng tiền cổ tức thực chi thấp, pha loãng cổ phiếu do phát hành thêm và phụ thuộc vào đòn bẩy tài chính để mở rộng hoạt động. Ba tiêu chí lựa chọn cổ phiếu của chỉ số VNSHINE được xây dựng nhằm hạn chế những vấn đề này, hướng đến các doanh nghiệp có chất lượng tài chính và chính sách phân bổ vốn hiệu quả hơn. | Đã xong | Đã dùng đúng đoạn của Linh. Thuật ngữ "Lợi suất Cổ đông" xem câu hỏi 5 | - |
| 53 | E | VNSHINE | Tập trung vào các công ty có xu hướng giảm đòn bẩy tài chính | Ưu tiên doanh nghiệp có xu hướng giảm đòn bẩy tài chính, qua đó tối ưu chi phí lãi vay và gia tăng nguồn lực cho việc chi trả cổ tức tiền mặt cho cổ đông. | Đã xong | Đã dùng đúng câu của Linh | - |
| 54 | E | VNSHINE | Quỹ PHFM VNSHINE ETF là quỹ hoán đổi danh mục mô phỏng VNSHI | Quỹ PHFM VNSHINE ETF là quỹ hoán đổi danh mục mô phỏng VNSHINE Index, gồm 15–30 cổ phiếu được lựa chọn theo bộ quy tắc “Vietnam Shareholder Interest Enhanced Index” do Sở Giao dịch Chứng khoán TP.HCM (HSX) ban hành. / Là một trong những đơn vị tiên phong triển khai chiến lược Smart Beta tại Việt Nam, PHFM tập trung khai thác Lợi suất Cổ đông (Shareholder Yield) thông qua kết hợp sàng lọc định lượng và phân tích cơ bản, hướng đến các doanh nghiệp có nền tảng tài chính vững mạnh, khả năng gia tăng giá trị cho cổ đông và sức chống chịu trước biến động thị trường. / Thông qua phương pháp đầu tư có hệ thống và kỷ luật, PHFM VNSHINE hướng đến việc mang lại một giải pháp đầu tư minh bạch, hiệu quả và bền vững cho nhà đầu tư trong dài hạn. | Đã xong | Đã dùng đúng ba đoạn của Linh. Thuật ngữ "Lợi suất Cổ đông" xem câu hỏi 5 | - |
| 55 | E | Học viện (EN) | ETF vs open-ended fund vs single stock | Comparing ETFs, open-ended funds, and Single stocks | Không còn áp dụng | Phần "So sánh ETF, quỹ mở và cổ phiếu lẻ" đã bỏ khỏi Học viện (#76) | - |
| 56 | E | Học viện (EN) | Foundational knowledge on open-ended funds and ETFs, written | đổi thành: Explore insights into open-ended funds, ETFs, and investment principles for beginners | Đã xong | EN: "Explore insights into open-ended funds, ETFs, and investment principles for beginners" | - |
| 57 | E | Tuyển dụng | Vị trí đang tuyển | thiếu phần sổ ra thông tin JD | Đã xong | Mỗi vị trí có nút "JD +" xổ ra Trách nhiệm chính và Yêu cầu | - |
| 58 | E | Tuyển dụng | 01 Học hỏi từ thực tiễn Làm việc trực tiếp cùng đội ngũ giàu | Visualize + thêm hình ảnh vào cho sinh động và bắt mắt | Đã xong | Bốn thẻ văn hóa (VI) đã có ảnh riêng | - |
| 59 | E | Công bố thông tin | Tất cả Báo cáo định kỳ Nghị quyết & Biên bản Tài liệu Đại hộ | Thêm báo cáo NAV | Đã xong | Công bố thông tin có loại "Báo cáo NAV ngày, tuần" và dòng "Báo cáo giá trị tài sản ròng tuần 40/2026" | - |
| 60 | E | Công bố thông tin | Tải tài liệu đã chọn | đổi thành "Tải về" | Đã xong | Nút đổi thành "Tải về" (EN "Download") | - |
| 61 | E | Về chúng tôi (EN) | Mr. Winston graduated with a Bachelor of Economics from Nati | Mr. Winston holds a Bachelor’s degree in Economics from National Taiwan University (NTU) and a Master of Business Administration (MBA) from Rotterdam School of Management in the Netherlands. With over 25 years of experience in finance and business management, he was appointed General Director of Phu Hung Fund Management Joint Stock Company (PHFM) in June 2020 and became the Company’s legal representative in December 2025. Prior to joining PHFM, he held key positions at First Commercial Bank in Taiwan and served as Director of the Analysis, Proprietary Trading, Advisory and Underwriting Division at Phu Hung Securities Corporation. | Đã xong | EN dùng đúng đoạn của Linh (hộp thoại Winston Lu) | - |
| 62 | E | Về chúng tôi (EN) | Creating investment value, guiding the way to a prosperous f | Creating Lasting Value, Enriching Your Future. | Đã xong | EN: "Creating Lasting Value, Enriching Your Future." | - |
| 63 | E | Về chúng tôi (EN) | Drawing on its expertise, research capability and deep under | With a strong foundation in investment expertise, research capabilities, and in-depth knowledge of Vietnam’s capital markets, PHFM develops investment solutions grounded in discipline, professionalism, and a long-term perspective to meet the diverse needs of individual and institutional clients. Leveraging the strengths of the Phu Hung Financial Group ecosystem, PHFM draws on the collective resources and expertise across the Group to deliver more comprehensive financial solutions. / Beyond providing investment solutions, PHFM aspires to be a trusted partner throughout each client’s financial journey, from saving and investing to managing and growing wealth. Through this commitment, PHFM aims to empower clients to shape their financial futures with confidence and pursue lasting prosperity. | Đã xong | EN dùng đúng hai đoạn giới thiệu của Linh | - |
| 64 | E | Về chúng tôi (EN) | bn VND | 3 cái đầu đồng bộ với trang chủ | Cần làm | Bốn số liệu đầu của Về chúng tôi: ba số đầu lấy đúng chuỗi trang chủ. VI: "+18" năm hoạt động; "+2.000" tỷ VND AUM; "4" sản phẩm quỹ (hiện "tỷ VNĐ", nhãn "Năm hoạt động", "Tổng tài sản quản lý"). EN: "18+" years of operation; "2,000+" bn VND AUM; "4" fund products (hiện "+2.000" dùng dấu chấm kiểu Việt trong bản EN). Số thứ tư (Vốn điều lệ 88,45 tỷ VNĐ) giữ, EN viết "88.45 bn VND". Dữ liệu `about.stats` (dòng 6362 `src/src_o8.html`). Số chưa đổi so với trang chủ | R6-05 |
| 65 | E | Về chúng tôi (EN) | Growth | chưa phù hợp nên cần design lại | Cần hỏi Rin | Linh muốn thiết kế lại khối "Lịch sử hình thành". Vòng 4 đã làm 3 cột, Rin lại muốn về bản gốc. Câu hỏi 3 | (sau Q3) |
| 66 | E | Về chúng tôi (EN) | Tân | sử dụng chữ tiếng anh | Cần hỏi Rin | Tên giá trị bằng tiếng Anh thay "Tân, Tốc, Thực, Giản" ở bản EN. Câu hỏi 4 | (sau Q4) |
| 67 | E | Về chúng tôi (EN) | Chief Executive Officer | General Director | Đã xong | EN: General Director | - |
| 68 | E | Về chúng tôi (EN) | Deputy Chief Executive Officer | Deputy General Director | Đã xong | EN: Deputy General Director | - |
| 69 | E | Về chúng tôi (EN) | Deputy Chief Executive Officer | Deputy General Director | Đã xong | EN: Deputy General Director | - |
| 70 | E | Danh sách quỹ | Các quỹ đại chúng do PHFM quản lý. Chọn một quỹ để xem chi t | bỏ câu này | Đã xong | Câu "Các quỹ đại chúng do PHFM quản lý…" đã bỏ | - |
| 71 | E | Danh sách quỹ | LỢI NHUẬN TỪ ĐẦU NĂM | tôi ưu lại hiển thị của tiêu đề, hiện đang xuống dòng mất cân đối | Cần làm | Danh sách quỹ ở 1440: tiêu đề cột "GIAO DỊCH" xuống dòng thành "GIAO / DỊCH" còn "LỢI NHUẬN TỪ ĐẦU NĂM" nằm một dòng, ô "Hằng ngày" cũng xuống dòng. Chia lại độ rộng cột (cột Giao dịch rộng hơn, `white-space:nowrap` cho tiêu đề), kiểm 1280 và 1024. Mẫu bảng quanh dòng 9555 `src/src_o8.html` | R6-04 |
| 72 | E | Danh sách quỹ | Nguồn: phfm.vn, số liệu đến ngày 14/10/2026. Hiệu suất trong | bỏ nguồm phfm.vn, số liệu tới ngày.... chỉ giữ phần còn lại | Cần hỏi Rin | "Nguồn: phfm.vn" đã bỏ. Còn "Số liệu minh hoạ, cập nhật đến ngày…". Brand-rules bắt giữ. Câu hỏi 7 | (sau Q7) |
| 73 | E | Trang chủ | Định hướng tương lai thịnh vượng PHFM là đơn vị quản lý đầu | Đáp án của quiz bỏ nút dẫn về link sản phẩm mà hãy để nút "Tìm giải pháp phù hợp" -> liên hệ | Đã xong | Công cụ trắc nghiệm: kết quả là câu "Liên hệ để tìm giải pháp dành riêng cho bạn." và nút "Tìm giải pháp phù hợp" mở trang Liên hệ. Không còn nút về trang sản phẩm | - |
| 74 | E | Trang chủ | Định hướng tương lai thịnh vượng PHFM là đơn vị quản lý đầu | Chỗ took đầu tư định kỳ cho phép thêm option gõ số ngoài việc kéo thanh công cụ | Đã xong | Công cụ đầu tư định kỳ: có ô nhập số cạnh thanh kéo (`pt-n`) | - |
| 75 | E | Góc nhìn & Tin tức | TIN PHFM | Đổi "TIN PHFM" thành "TIN TỨC" | Đã xong | Không còn chữ "TIN PHFM". Tab là "Tin tức – Sự kiện" | - |
| 76 | E | Học viện | So sánh ETF, quỹ mở và cổ phiếu lẻ | Đoạn này bỏ | Đã xong | Phần "So sánh ETF, quỹ mở và cổ phiếu lẻ" đã bỏ | - |
| 77 | E | Học viện | Chiến lược Lợi suất Cổ đông - Shareholder Yield là gì? | chỗ này bị lỗi đè chữ | Đã xong | Bước 03 của Học viện (tab Quỹ ETF) không đè chữ ở 1440 (đã chụp). Kiểm lại ở 390 và 1024 trong R6-01 | - |
| 78 | E | Học viện | Xem trang VNSHINE ETF | đổi tên nút này "Khám phả FUEPHVNS" | Đã xong | Nút là "Khám phá FUEPHVNS →" | - |
| 79 | E | Học viện | Thuật ngữ đầu tư NAV Giá trị tài sản ròng: tổng tài sản của | Thêm phần biểu mẫu ở đây và ở footer | Cần làm | Học viện đầu tư: thêm khối/thẻ "Biểu mẫu" (dưới Thuật ngữ đầu tư) nối sang trang Biểu mẫu, dùng lại chữ trang Biểu mẫu: VI "Tải các biểu mẫu giao dịch và hồ sơ cần thiết khi đầu tư cùng PHFM." EN "Download the transaction forms and documents you need to invest with PHFM." (chờ pháp chế). Footer đã có link "Biểu mẫu" | R6-03 |
| 80 | E | Hướng dẫn PHVSF (EN) | Transfer money | các nút bấm đang bị lỗi ko nhảy | Đã xong | EN: các bước Transfer money, Step 03, Step 04 cuộn đúng (đã bấm thử) | - |
| 81 | E | Hướng dẫn PHVSF | HƯỚNG DẪN ĐẦU TƯ Hướng dẫn đầu tư Quỹ mở PHVSF 4 bước đầu tư | Bổ sung thêm phần biểu mẫu | Cần làm | Hướng dẫn PHVSF: thêm khối "Biểu mẫu" (VI) / "Forms" (EN) sau bước 04, trước Đại lý phân phối. Liệt kê 4 biểu mẫu của Quỹ mở PHVSF từ dữ liệu trang Biểu mẫu, nút "Tải về" dùng thông báo "đang cập nhật" khi chưa có file. File: [placeholder] | R6-03 |
| 82 | E | Hướng dẫn PHVSF | Nhà đầu tư thực hiện các bước sau: | thêm note: Lưu ý: Nhà đầu tư đã có tài khoản chứng khoán có thể bỏ qua bước này. | Đã xong | Đã có "Lưu ý: Nhà đầu tư đã có tài khoản chứng khoán có thể bỏ qua bước này." | - |
| 83 | E | Hướng dẫn PHVSF | Chuyển tiền | các nút bấm bị lỗi ko nhảy | Đã xong | Như #18 | - |
| 84 | E | Hướng dẫn VNSHINE | 02 Xem chi tiết → | Link ở đây bị lỗi | Cần làm | Như #34 (VI chạy, EN và 中文 mất đường dẫn) | R6-02 |
| 85 | E | Hướng dẫn VNSHINE | Thành viên lập quỹ / Đại lý phân phối chứng chỉ quỹ Điểm nhậ | update lại logo, không cần chia HCM và HN vì ở đâu cũng có thể đky được, để tên công ty ko cần địa chỉ và sdt nữa | Đã xong | Danh sách Thành viên lập quỹ chỉ còn logo và tên công ty, không chia HCM/HN, không địa chỉ, số điện thoại | - |
| 86 | E | Hướng dẫn VNSHINE | Thành viên lập quỹ / Đại lý phân phối chứng chỉ quỹ Điểm nhậ | xếp theo thứ tự alphabet | Đã xong | Xếp theo thứ tự chữ cái (VI và EN) | - |
| 87 | E | Công bố thông tin (EN) | INVESTOR RELATIONS | Information Disclosure | Đã xong | EN trang Công bố thông tin: tiêu đề "Information Disclosure", không còn "INVESTOR RELATIONS" (dòng nhãn nhỏ ẩn vì trùng tiêu đề) | - |
| 88 | E | Về chúng tôi | Ông Winston tốt nghiệp Cử nhân Kinh tế tại Đại học Quốc gia | Ông Winston tốt nghiệp Cử nhân Kinh tế tại Đại học Quốc gia Đài Loan (NTU) và Thạc sĩ Quản trị Kinh doanh (MBA) tại Trường Quản lý Rotterdam, Hà Lan. Với hơn 25 năm kinh nghiệm trong lĩnh vực tài chính và quản lý kinh doanh, ông được bổ nhiệm làm Tổng Giám đốc Công ty Cổ phần Quản lý Quỹ Phú Hưng (PHFM) vào tháng 6/2020 và trở thành người đại diện theo pháp luật của Công ty vào tháng 12/2025. Trước đó, ông từng đảm nhiệm các vị trí quan trọng tại Ngân hàng First Commercial Bank (Đài Loan) và giữ chức Giám đốc Khối Phân tích, Tự doanh, Tư vấn và Bảo lãnh phát hành tại Công ty Cổ phần Chứng khoán Phú Hưng. | Đã xong | VI dùng đúng đoạn của Linh (hộp thoại Winston Lu) | - |
| 89 | E | Về chúng tôi | GIỚI THIỆU Người đồng hành đáng tin cậy trên hành trình tài | Với nền tảng chuyên môn vững chắc, năng lực nghiên cứu và sự am hiểu sâu sắc thị trường vốn Việt Nam, PHFM phát triển các giải pháp đầu tư dựa trên nguyên tắc kỷ luật, tính chuyên nghiệp và tầm nhìn dài hạn, đáp ứng nhu cầu đa dạng của khách hàng cá nhân và tổ chức. Đồng thời, kế thừa lợi thế từ hệ sinh thái Tập đoàn Tài chính Phú Hưng, PHFM phát huy nguồn lực và chuyên môn trong toàn hệ thống để mở rộng khả năng cung cấp các giải pháp tài chính toàn diện cho khách hàng. / Không chỉ dừng lại ở việc cung cấp giải pháp đầu tư, PHFM hướng đến trở thành đối tác đồng hành đáng tin cậy trên hành trình tài chính của mỗi khách hàng, từ tích lũy, đầu tư đến quản lý và phát triển tài sản. Qua đó, PHFM mong muốn góp phần giúp khách hàng chủ động hoạch định tương lai tài chính và hướng đến cuộc sống thịnh vượng bền vững. | Đã xong | VI dùng đúng hai đoạn giới thiệu của Linh | - |
| 90 | E | Về chúng tôi | 2013 – 2019 | chưa phù hợp nên cần design lại | Cần hỏi Rin | Như #65. Câu hỏi 3 | (sau Q3) |
| 91 | E | VNSHINE (EN) | Mr. Winston graduated with a Bachelor of Economics from Nati | Mr. Winston holds a Bachelor’s degree in Economics from National Taiwan University (NTU) and a Master of Business Administration (MBA) from Rotterdam School of Management in the Netherlands. With over 25 years of experience in finance and business management, he was appointed General Director of Phu Hung Fund Management Joint Stock Company (PHFM) in June 2020 and became the Company’s legal representative in December 2025. Prior to joining PHFM, he held key positions at First Commercial Bank in Taiwan and served as Director of the Analysis, Proprietary Trading, Advisory and Underwriting Division at Phu Hung Securities Corporation. | Đã xong | EN dùng đúng đoạn của Linh (hộp thoại Winston Lu, trang VNSHINE) | - |
| 92 | E | VNSHINE (EN) | Firmly excludes companies that overuse capital raising, pres | Prioritizes companies with prudent capital-raising policies to help limit ownership dilution and protect existing shareholders’ interests. | Đã xong | EN: "Prioritizes companies with prudent capital-raising policies…" | - |
| 93 | E | VNSHINE (EN) | NAV PER UNIT (VND) | -	NAV Date / -	Fund NAV (VND) / -	Closing price / -	Premium / Discount | Đã xong | Cột bảng NAV: "NAV Date", "Fund NAV (VND)", "Closing price", "Premium / Discount" | - |
| 94 | E | VNSHINE (EN) | Index rules | Daily & Weekly Reports / Financial Reports / Monthly Reports / Factsheets / Prospectus / Fund Charter / Fund Information / Licenses / Other | Cần hỏi Rin | Danh sách Loại tài liệu. Hai danh sách Linh đưa không khớp nhau. Câu hỏi 8 | (sau Q8) |
| 95 | E | VNSHINE (EN) | Deputy Chief Executive Officer | Deputy General Director | Đã xong | EN: Deputy General Director | - |
| 96 | E | VNSHINE (EN) | View trading information | Nút này bị xuống dòng | Đã xong | Nút "View trading information" một dòng ở 390, 768, 1024, 1280, 1440 (EN) | - |
| 97 | E | VNSHINE (EN) | About the fund | About PHFM VNSHINE ETF | Đã xong | Tiêu đề EN: "About PHFM VNSHINE ETF" | - |
| 98 | E | PHVSF (EN) | All Prospectus Fund charter Monthly report NAV report Financ | Daily & Weekly Reports / Financial Reports / Monthly Reports / Factsheets / Prospectus / Fund Charter / Fund Information / Licenses / Other | Cần hỏi Rin | Như #94. Câu hỏi 8 | (sau Q8) |
| 99 | E | PHVSF (EN) | Deputy Chief Executive Officer | Deputy General Director | Đã xong | EN: Deputy General Director | - |
| 100 | E | PHVSF (EN) | OPEN-ENDED EQUITY FUND · DAILY DEALING | Open-ended fund | Cần làm | Nhãn nhỏ trên tiêu đề hero PHVSF (EN): "OPEN-ENDED FUND · DAILY DEALING" đổi thành "OPEN-ENDED FUND" (đã bỏ chữ EQUITY). Khoá `heroEyebrow` dòng 6201 `src/src_o8.html`, vá `src/patches6.py`. 中文 giữ, chờ cô Helena | R6-04 |
| 101 | E | PHVSF (EN) | Phu Hung Vietnam Selective Fund | PHU HUNG VIETNAM SELECT INVESTMENT FUND | Đã xong | Hero EN: "PHU HUNG VIETNAM SELECT INVESTMENT FUND" | - |
| 102 | E | PHVSF (EN) | Phu Hung Vietnam Selective Fund (PHVSF) is the first open-en | Phu Hung Vietnam Select Investment Fund (PHVSF) follows an active investment strategy, focusing on companies with strong financial fundamentals, growth prospects, and reasonable valuations. Combining internationally aligned research standards with a diversified portfolio and disciplined risk management, PHVSF offers investors a professional and convenient way to access Vietnam’s equity market without the time and effort required for individual stock analysis, while targeting sustainable wealth growth over the medium to long term. | Đã xong | EN dùng đúng đoạn mô tả của Linh | - |
| 103 | E | PHVSF (EN) | Fund name PHU HUNG VIETNAM SELECTIVE FUND Fund code PHVSF Fu | lấy đúng nội dung bản tiếng anh gốc tại: https://www.phfm.vn/product-service/overview/ | Cần hỏi Rin | Cần nội dung gốc phfm.vn/product-service/overview. Claude không mở được phfm.vn. Câu hỏi 10 | (sau Q10) |
| 104 | E | PHVSF (EN) | Source: PHFM · Updated 15:00, 05/10/2026 | Bỏ Source PHFM | Đã xong | Hero không còn dòng "Source: PHFM · Updated 15:00…" | - |
| 105 | E | PHVSF (EN) | * All transactions are based solely on the NAV determined on | * All trades are only based on NAV determined on the trading day (T day), NAV not determined on the trading day is for reference only | Đã xong | EN: "* All trades are only based on NAV determined on the trading day (T day), NAV not determined on the trading day is for reference only" | - |
| 106 | E | PHVSF | THAY ĐỔI | bị mất update cũ, bổ sung lại https://www.phfm.vn/vi/product-service/performance/ | Cần hỏi Rin | Cột "THAY ĐỔI" ở Lịch sử NAV đã có (theo ngày). "Bị mất update cũ" chưa rõ: cần xem trang phfm.vn/vi/product-service/performance. Câu hỏi 9 | (sau Q9) |
| 107 | E | PHVSF | Lịch sử NAV NAV/CCQ là giá trị tài sản ròng của quỹ chia cho | Thiếu filter cho chọn ngày và trang để hiển thị hết nội dung | Đã xong | Tab Lịch sử NAV có Từ ngày / Đến ngày và nút "Xem thêm" (10 dòng mỗi lần, đã bấm thử) | - |
| 108 | E | PHVSF | PHFM · Demo website Bản mẫu thiết kế, chưa phải website chín | Phần kết quả của quiz đổi thành 1 câu kiểu: "Liên hệ để tìm giải pháp dành riêng cho bạn" | Đã xong | Như #73. Chuỗi "PHFM · Demo website…" không còn trên trang | - |
| 109 | E | PHVSF | Số liệu tại ngày 03.10.2026. Hiệu suất trong quá khứ không đ | Bỏ câu: "số liệu tại ngày" vẫn giữ câu "Hiệu suất..." | Đã xong | Như #49 | - |
| 110 | E | PHVSF | Quỹ phù hợp với bạn nếu: | Quỹ phù hợp với bạn nếu bạn muốn: / - Đầu tư cổ phiếu mà không mất thời gian tự nghiên cứu. / - Sở hữu danh mục được quản lý chuyên nghiệp, kỷ luật. / - Bắt đầu với số vốn phù hợp. / - Đầu tư định kỳ để tích lũy tài sản. / - Hướng đến các mục tiêu tài chính dài hạn. | Đã xong | Đã dùng đúng 5 gạch đầu dòng của Linh | - |
| 111 | E | PHVSF | Trang chủ / Sản phẩm & Dịch vụ / Quỹ mở PHVSF QUỸ MỞ CỔ PHIẾ | Đổi thành "QŨY MỞ" | Cần làm | Nhãn nhỏ trên tiêu đề hero PHVSF (VI): "QUỸ MỞ · GIAO DỊCH HẰNG NGÀY" đổi thành "QUỸ MỞ" (đã bỏ chữ CỔ PHIẾU). Cùng chỗ sửa với #100 | R6-04 |
| 112 | E | PHVSF | PHVSF | BỎ NÚT NÀY | Đã xong | Chip mã quỹ "PHVSF" dưới tiêu đề hero PHVSF không còn | - |
| 113 | E | PHVSF | Quỹ Đầu tư Chọn lọc Phú Hưng Việt Nam (PHVSF) là quỹ mở đầu | Quỹ Đầu tư Chọn lọc Phú Hưng Việt Nam (PHVSF) nổi bật với chiến lược đầu tư chủ động, tập trung lựa chọn các doanh nghiệp có nền tảng tài chính vững chắc, triển vọng tăng trưởng và định giá hợp lý. Kết hợp nghiên cứu theo tiêu chuẩn quốc tế, danh mục đa dạng và quản trị rủi ro chặt chẽ, PHVSF mang đến cho nhà đầu tư giải pháp tiếp cận thị trường cổ phiếu Việt Nam một cách chuyên nghiệp, tiết kiệm thời gian tự phân tích và hướng đến tăng trưởng tài sản bền vững trong trung và dài hạn. | Đã xong | Đã dùng đúng đoạn mô tả của Linh | - |
| 114 | E | PHVSF | Nguồn: PHFM · Cập nhật lúc 15:00 ngày 05/10/2026 | Đoạn này có tự update được không? | Đã xong | Dòng "Nguồn: PHFM · Cập nhật lúc 15:00…" đã bỏ. Dòng ngày còn lại là "cập nhật đến ngày 14/10/2026" lấy từ `PHFM_ASOF` (ngày dữ liệu), không phải giờ mở trang. Trả lời Linh: tự cập nhật khi dev nối nguồn NAV (specs/dev-handoff.md, B01) | - |
| 115 | E | PHVSF | Tài liệu quỹ | đổi thành filter cho tài liệu riêng, biểu mẫu bỏ riêng | Cần hỏi Rin | Như #94. Câu hỏi 8 | (sau Q8) |
| 116 | E | PHVSF | Biểu mẫu | Thông báo quỹ / Điều lệ quỹ / Bản cáo bạch / Báo cáo tài chính / Báo cáo hoạt động tháng / Báo cáo NAV ngày, tuần / Biểu mẫu / Factsheet | Cần hỏi Rin | Như #94. Danh sách 8 loại của Linh có "Biểu mẫu", nhưng #115 nói biểu mẫu để riêng. Câu hỏi 8 | (sau Q8) |
| 117 | E | VNSHINE | Thông tin quỹ Đơn vị quản lý PHFM Loại tài sản Chứng khoán M | sắp xếp lại theo thứ tự ABC | Đã xong | Thông tin quỹ VNSHINE (VI) xếp A đến Z theo nhãn. Bản EN cùng thứ tự nên không theo A–Z (ghi ở mục Lỗi phụ) | - |
| 118 | E | VNSHINE | Kết quả hoạt động 1 tháng 3 tháng 6 tháng YTD 1 năm Tất cả → | bỏ chỉ số VN-Index, 2 cái còn lại là PHFM VNSHINE ETF và VNSHINE Index | Đã xong | Biểu đồ chỉ còn FUEPHVNS và VNSHINE Index, không có VN-Index | - |
| 119 | E | VNSHINE | KHỐI LƯỢNG 182.400 | bỏ phần khối lượng | Đã xong | Không còn ô Khối lượng | - |
| 120 | E | VNSHINE | Shareholder Yield | đổi thành "Chiến lược lợi suất cổ đông" | Cần hỏi Rin | Linh đổi tiêu đề thành "Chiến lược lợi suất cổ đông". Brand-rules chốt "Tỷ suất Lợi nhuận Cổ đông" (issue #9 còn mở). Câu hỏi 5 | (sau Q5) |
| 121 | E | VNSHINE | Lưu ý khi đầu tư ETF ETF được mua bán trên sàn HOSE qua tài | bỏ ra | Đã xong | Khối "Lưu ý khi đầu tư ETF" đã bỏ | - |
| 122 | E | VNSHINE | Chứng khoán | bỏ ra | Đã xong | Dòng "Loại tài sản: Chứng khoán" đã bỏ | - |
| 123 | E | VNSHINE | HSX | HOSE | Đã xong | Dùng "HOSE" | - |
| 124 | E | VNSHINE | VND 100,000 | sửa: 100,000 ccq/lô | Đã xong | Lô chứng chỉ quỹ: "100,000 ccq/lô" | - |
| 125 | E | VNSHINE | Lô chứng chỉ quỹ (CCQ/Lô) | bỏ: (CCQ/Lô) | Đã xong | Nhãn là "Lô chứng chỉ quỹ", đã bỏ "(CCQ/Lô)" | - |
| 126 | E | VNSHINE | THÀNH VIÊN LẬP QUỸ VÀ ĐỐI TÁC PHÂN PHỐI | xếp theo thứ tự alphabet | Đã xong | Xếp theo thứ tự chữ cái | - |
| 127 | E | VNSHINE | Giá trên sàn do cung cầu quyết định nên có thể lệch nhẹ so v | phần này có nói tham khảo DC nhưng chưa thấy, xem lại wording câu này, bỏ 3 ô dưới, thêm nút "Tải danh mục cơ cấu (PCF)” như option A | Đã xong | Ba ô dưới đã bỏ, có nút "Tải danh mục cơ cấu (PCF) ↓". Câu về giá sàn và NAV đã viết lại | - |
| 128 | E | VNSHINE | WL Ông Winston Lu Tổng Giám đốc Ông Winston tốt nghiệp Cử nh | Chỉ hiển thị Tên & Title. Khi click vào profile mới pop-up ra thông tin chi tiết | Đã xong | Như #36 | - |
| 129 | E | VNSHINE | Ông Winston tốt nghiệp Cử nhân Kinh tế tại Đại học Quốc gia | Ông Winston tốt nghiệp Cử nhân Kinh tế tại Đại học Quốc gia Đài Loan (NTU) và Thạc sĩ Quản trị Kinh doanh (MBA) tại Trường Quản lý Rotterdam, Hà Lan. Với hơn 25 năm kinh nghiệm trong lĩnh vực tài chính và quản lý kinh doanh, ông được bổ nhiệm làm Tổng Giám đốc Công ty Cổ phần Quản lý Quỹ Phú Hưng (PHFM) vào tháng 6/2020 và trở thành người đại diện theo pháp luật của Công ty vào tháng 12/2025. Trước đó, ông từng đảm nhiệm các vị trí quan trọng tại Ngân hàng First Commercial Bank (Đài Loan) và giữ chức Giám đốc Khối Phân tích, Tự doanh, Tư vấn và Bảo lãnh phát hành tại Công ty Cổ phần Chứng khoán Phú Hưng. | Đã xong | Như #88 (VI), đoạn của Linh | - |
| 130 | E | VNSHINE | Báo cáo tháng | các loại tài liệu đổi thành filter sổ xuống / Linh: biểu mẫu bỏ riêng | Cần hỏi Rin | Như #94. Câu hỏi 8 | (sau Q8) |
| 131 | E | VNSHINE | Kiên quyết loại bỏ các doanh nghiệp lạm dụng việc tăng vốn, | Ưu tiên doanh nghiệp có chính sách tăng vốn hợp lý, hạn chế nguy cơ pha loãng tỷ lệ sở hữu và lợi ích của cổ đông hiện hữu. | Đã xong | Đã dùng đúng câu của Linh | - |
| 132 | E | VNSHINE | PHFM · Demo website Bản mẫu thiết kế, chưa phải website chín | NAV tại ngày / NAV của quỹ (VND) / Giá đóng cửa / Premium / Discount | Đã xong | Như #93 (cột bảng NAV) | - |
| 133 | E | VNSHINE | NAV/CCQ (VND) | NAV tại ngày / NAV của quỹ (VND) / Giá đóng cửa / Premium / Discount | Đã xong | Như #93 | - |
| 134 | E | VNSHINE | Bộ quy tắc chỉ số | Báo cáo ngày, tuần / Báo cáo tài chính / Báo cáo hoạt động tháng / Factsheets / Bản cáo bạch / Điều lệ quỹ / Thông tin quỹ / Giấy phép / Khác | Cần hỏi Rin | Như #94. Câu hỏi 8 | (sau Q8) |
| 135 | E | Về chúng tôi | Công ty Cổ phần Quản lý Quỹ Phú Hưng (PHFM), thành viên Tập | Công ty Cổ phần Quản lý Quỹ Phú Hưng (PHFM) — thành viên Tập đoàn Tài chính Phú Hưng — Chuyên cung cấp các giải pháp quản lý tài sản và tư vấn đầu tư chuyên nghiệp cho các khách hàng cá nhân lẫn tổ chức trong và ngoài nước. | Đã xong | Hero Về chúng tôi dùng đúng câu của Việt | - |
| 136 | C | Công bố thông tin | QUAN HỆ NHÀ ĐẦU TƯ | để line ngang chỗ Quan hệ nhà đầu tư | Đã xong | Trang Công bố thông tin: nhãn "QUAN HỆ NHÀ ĐẦU TƯ" có đường kẻ ngang 64px bên cạnh (VI) | - |
| 137 | C | Trang chủ | FUND.PHFM.VN · PHFM MOBILE | bỏ dòng này | Không còn áp dụng | Dòng "FUND.PHFM.VN · PHFM MOBILE" không có trên trang chủ Teal Vanguard hiện tại | - |
| 138 | C | Trang chủ | Bắt đầu tích luỹ từ hôm nay | bỏ line | Cần hỏi Rin | Trang chủ giữ nguyên. Câu hỏi 11 | (sau Q11) |
| 139 | C | Liên hệ (EN) | Get in touch | Contact us | Đã xong | Liên hệ (EN): tiêu đề "Contact us" | - |
| 140 | C | Góc nhìn & Tin tức | GÓC NHÌN CHUYÊN SÂU & TIN TỨC | Bỏ 1 cái góc nhìn chuyên sâu & tin tức | Đã xong | Tiêu đề Góc nhìn & Tin tức chỉ còn một lần | - |
| 141 | C | Liên hệ | Trang chủ / Liên hệ Kết nối với PHFM Thông tin liên hệ Trụ s | bỏ line trên | Cần hỏi Rin | Trang Liên hệ bản gốc không có đường kẻ nào trang trí. Không rõ "line trên" là đường nào. Câu hỏi 2 | (sau Q2) |
| 142 | C | Liên hệ | Gửi yêu cầu | bỏ line | Cần hỏi Rin | Như #141. Câu hỏi 2 | (sau Q2) |
| 143 | C | Về chúng tôi | HS Bà Helena Shiu, CFA Phó Tổng Giám đốc Bà Helena là Thạc s | Cho 3 khung ban lãnh đạo bằng nhau | Đã xong | Ba thẻ Ban lãnh đạo bằng nhau (376×242 ở 1440) | - |
| 144 | C | Về chúng tôi | Đối tác | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Đối tác (Về chúng tôi) | R6-06 |
| 145 | C | Về chúng tôi | Ban lãnh đạo | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Ban lãnh đạo | R6-06 |
| 146 | C | Về chúng tôi | Giá trị cốt lõi | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Giá trị cốt lõi (đường kẻ giữa Sứ mệnh/Tầm nhìn và khối giá trị) | R6-06 |
| 147 | C | Về chúng tôi | Lịch sử hình thành | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Lịch sử hình thành (làm sau khi Q3 quyết kiểu khối) | R6-06 |
| 148 | C | Quản lý danh mục | Liên hệ với bộ phận khách hàng tổ chức | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối "Liên hệ với bộ phận khách hàng tổ chức" (Quản lý danh mục) | R6-06 |
| 149 | C | Quản lý danh mục | PHFM · Demo website Bản mẫu thiết kế, chưa phải website chín | bỏ câu này | Đã xong | Chuỗi "PHFM · Demo website…" không còn trên trang | - |
| 150 | C | Quản lý danh mục | Đầu tư vào quỹ có thể phát sinh rủi ro. Nhà đầu tư nên đọc k | bỏ câu này | Đã xong | Câu dài "Đầu tư vào quỹ có thể phát sinh rủi ro…" không còn trên trang Quản lý danh mục. Footer vẫn giữ "Đầu tư có rủi ro. Vui lòng đọc kỹ Bản cáo bạch." theo brand-rules | - |
| 151 | C | PHVSF | Thông tin quỹ | bỏ line ở đây | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Thông tin quỹ (PHVSF) | R6-06 |
| 152 | C | PHVSF | Kết quả hoạt động | bỏ line ở đây | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Kết quả hoạt động (PHVSF) | R6-06 |
| 153 | C | PHVSF | Ban điều hành quỹ HS Ông Nguyễn Hoài Sơn Giám đốc Phòng Đầu | bỏ line ở đây | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Ban điều hành quỹ (PHVSF) | R6-06 |
| 154 | C | PHVSF | Tài liệu quỹ | bỏ line ở đây | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Tài liệu quỹ (PHVSF) | R6-06 |
| 155 | C | PHVSF | Hướng dẫn đầu tư | bỏ line ở đây | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) nằm dưới tiêu đề Hướng dẫn đầu tư (PHVSF) | R6-06 |
| 156 | C | PHVSF | Trang chủ / Sản phẩm & Dịch vụ / Quỹ mở PHVSF QUỸ MỞ CỔ PHIẾ | line chuyển xuống dưới "Quỹ đầu tư chọn lọc..." | Đã xong | Gạch vàng của hero PHVSF nằm dưới tiêu đề "Quỹ Đầu tư Chọn lọc Phú Hưng Việt Nam" | - |
| 157 | C | PHVSF | 1.5% NAV/ năm | Giá dịch vụ quản lý đưa lên ngang Giá dịch vụ phát hành để cho gọn | Đã xong | Ở 1440, "Giá dịch vụ quản lý quỹ" nằm cùng hàng với "Giá dịch vụ phát hành" (hai cột). Một cột ở mobile | - |
| 158 | C | VNSHINE | CHIẾN LƯỢC SHAREHOLDER YIELD | CHIẾN LƯỢC ĐẦU TƯ | Đã xong | Nhãn là "CHIẾN LƯỢC ĐẦU TƯ" | - |
| 159 | C | VNSHINE | Quỹ PHFM VNSHINE ETF | line chuyển xuống dưới "Quỹ PHFM..." | Đã xong | Gạch vàng của hero VNSHINE nằm dưới tiêu đề "Quỹ PHFM VNSHINE ETF" | - |
| 160 | C | VNSHINE | Thông tin quỹ | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Thông tin quỹ (VNSHINE) | R6-06 |
| 161 | C | VNSHINE | Kết quả hoạt động | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Kết quả hoạt động (VNSHINE) | R6-06 |
| 162 | C | VNSHINE | Thông tin giao dịch | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Thông tin giao dịch (VNSHINE) | R6-06 |
| 163 | C | VNSHINE | Ban điều hành quỹ | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Ban điều hành quỹ (VNSHINE) | R6-06 |
| 164 | C | VNSHINE | Tài liệu quỹ | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối Tài liệu quỹ (VNSHINE) | R6-06 |
| 165 | C | VNSHINE | Hướng dẫn đầu tư | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) nằm dưới tiêu đề Hướng dẫn đầu tư (VNSHINE) | R6-06 |
| 166 | C | VNSHINE | Đầu tư theo tiền thật doanh nghiệp trả cho cổ đông. | Quỹ ETF đầu tiên tại Việt Nam được xây dựng theo Chiến lược Lợi suất Cổ đông - Shareholder Yield. | Cần hỏi Rin | Câu hero đã dùng đúng chữ của Linh, nhưng "đầu tiên" và "Lợi suất Cổ đông" đụng brand-rules. Câu hỏi 5 và 6 | (sau Q5, Q6) |
| 167 | C | Quỹ thành viên | Liên hệ với bộ phận khách hàng tổ chức | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối "Liên hệ với bộ phận khách hàng tổ chức" (Quỹ thành viên) | R6-06 |
| 168 | C | Quỹ thành viên | Tôi đồng ý để PHFM xử lý dữ liệu cá nhân nhằm phản hồi yêu c | thiếu ô tick | Đã xong | Form Quỹ thành viên có ô tick đồng ý (18px, hiện rõ) | - |
| 169 | C | Quỹ thành viên | Đầu tư vào quỹ có thể phát sinh rủi ro. Nhà đầu tư nên đọc k | bỏ câu này | Đã xong | Như #150 (Quỹ thành viên) | - |
| 170 | C | Tư vấn đầu tư | Liên hệ với bộ phận khách hàng tổ chức | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối "Liên hệ với bộ phận khách hàng tổ chức" (Tư vấn đầu tư) | R6-06 |
| 171 | C | Tư vấn đầu tư | Đầu tư vào quỹ có thể phát sinh rủi ro. Nhà đầu tư nên đọc k | bỏ câu này | Đã xong | Như #150 (Tư vấn đầu tư) | - |
| 172 | C | Tuyển dụng | Văn hóa của chúng tôi | Chuyển line này xuống dưới Văn hóa PHFM | Đã xong | Gạch vàng của hero Tuyển dụng nằm dưới tiêu đề "Văn hóa PHFM" | - |
| 173 | C | Tuyển dụng | Vị trí đang tuyển | bỏ line | Cần làm | Bỏ đường kẻ ngang 1px (#D8E7EA) (`border-top` của section) trên khối "Vị trí đang tuyển" (Tuyển dụng). Giữ đường kẻ giữa các dòng vị trí, Linh chỉ nói đường trên | R6-06 |
