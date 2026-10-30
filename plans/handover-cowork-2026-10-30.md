# Bàn giao cho Cowork · 30/10/2026, 17:55

Claude Code (cloud) dừng ở đây theo yêu cầu của Rin. Cowork làm tiếp khi hạn mức đặt lại.
Đọc trước: `CLAUDE.md`, `specs/brand-rules.md`, `plans/round-6.md` (nhánh `plan/round-6`, PR #42).

## Quyết định của Rin còn hiệu lực

- Trang con: **bố cục, cỡ chữ, khoảng cách như bản gốc** (build commit `3131e7e`), **màu phương án A** (vòng 5, đã merge PR #36). Giữ các sửa lỗi: chữ không bị ép, menu 1 gạch, chữ Hán (giữ màu `#C0962D`), bản 中文 #27, lưới Giá trị cốt lõi mobile #17.
- Trang chủ và footer giữ nguyên.
- Bình luận: chỉ xử lý Option E và C. Đổi chữ áp ngay ở VI, viết EN tương đương, ghi "chờ pháp chế". 中文 không tự dịch (chờ cô Helena).
- File/link chưa có: `[placeholder]`, ghi vào `specs/dev-handoff.md`.
- Claude được tự merge sau khi reviewer **Approve** và CI xanh. Merge bằng **merge commit** (không squash).
- Mỗi việc xong gửi Rin bản xem trước (trang so sánh trước/sau + bản HTML đầy đủ).
- Q1 đường kẻ: giữ nguyên. Q5: "Tỷ suất Lợi nhuận Cổ đông" toàn site (đóng #9 khi merge R6-04). Q6: giữ "Quỹ ETF đầu tiên…", chờ pháp chế. Q7: giữ "Số liệu minh hoạ", chữ nhỏ nghiêng. Q8: Công bố thông tin 8 loại (#116), Tài liệu quỹ 9 loại (#134), biểu mẫu sang trang Biểu mẫu.

## Trạng thái PR

| PR | Nhánh | Nội dung | Trạng thái | Việc tiếp |
|---|---|---|---|---|
| #42 | `plan/round-6` | Plan vòng 6 + tài liệu này | Mở, chỉ tài liệu | Merge sau khi xong vòng 6 (hoặc review nhanh rồi merge) |
| #46 | `r6/r6-01` | Bố cục trang con về bản gốc, màu A. Closes #45 | Mở, **chưa có review** (reviewer bị ngắt do hạn mức) | Review → merge **trước** #44, R6-04 |
| #44 | `r6/r6-03` | Phiếu đăng ký, Bước 03 EN/中文, khối Biểu mẫu | Đã sửa theo review (commit `390cd9c`, vùng chạm 44px), **chờ review lại** | Review lại → merge. Xung đột nhẹ với #46 ở `src/patches.py` (đăng ký PATCHES6 và PATCHES6B) và changelog: giữ cả hai |
| (chưa mở) | `r6/r6-04` | Trang quỹ, Danh sách quỹ, Tỷ suất Lợi nhuận Cổ đông, 9 loại tài liệu, nhãn QUỸ MỞ, ghi chú nghiêng, "Chọn tất cả" (commit `5aacb26`, tách từ `r6/r6-01`) | Đã commit và push, **chưa mở PR**, chưa kiểm hết | Xem lại commit, chạy build + `node qa/qa.js`, kiểm Công bố thông tin dùng 8 loại (#116) — commit hiện chỉ nêu 9 loại cho Tài liệu quỹ; mở PR (ghi phụ thuộc #46, `Closes #9`) → review → merge sau #46 |
| (chưa làm) | `r6/r6-05` | Về chúng tôi: bình luận #64 (ba số đầu lấy đúng chuỗi trang chủ) và việc khác của nhóm R6-05 trong plan | Chưa bắt đầu | Tách từ `r6/r6-04` hoặc main sau khi merge |

Đã merge hôm nay: vòng 4 (#13, #16, #19, #15, #21, #23, #26), sửa #27 (#28), #24 (#29), #18 (#30), #17 (#32), #20 (#33), vòng 5 màu A (#36, đóng #35 #37 #38), R6-02 (#43).

## Việc còn lại theo thứ tự

1. Review #46 → merge.
2. Review lại #44 → gộp main (giữ cả PATCHES6 và PATCHES6B) → merge.
3. R6-04: kiểm, mở PR, review, merge; đóng #9.
4. R6-05: làm, PR, review, merge.
5. Ảnh hero mới (8 ảnh, xem dưới), gắn vào 8 hero trang con, chỉnh `object-position`, xoá khoá ảnh không dùng.
6. QA tổng: 20 trang × VI/EN/中文 × 1440/1024/768/390 (`WIDTHS="1440 1024 768 390" node qa/qa.js`), so trang chủ 0 điểm ảnh khác.
7. Gói bàn giao cho dev back-end: bản HTML cuối, ảnh toàn trang, specs UI/UX (màu, chữ, khoảng cách, thành phần, responsive), specs dữ liệu (`PHFM_DATA`, `PHFM_ASOF`, các trường CMS/API, form, tải tài liệu, tìm kiếm, link giao dịch), danh sách placeholder, chờ pháp chế, chờ cô Helena. Cập nhật `specs/dev-handoff.md`.

## Ảnh hero mới (Higgsfield, chưa tải về repo)

Claude Code cloud không tải được: mạng chặn `d8j0ntlcm91z4.cloudfront.net`. Cowork tải bằng Higgsfield (job id dưới), lưu gốc `assets/source/generated/r6_*.webp`, nén `python3 tools/add_image.py <gốc> <khoá> <rộng>`, ghi `specs/image-sources.json`.
Lưu ý: hệ thống ghi model `nano_banana_2` dù đã chọn `nano_banana_pro` — kiểm lại; nếu không phải Nano Banana Pro thì tạo lại theo brand-rules.

| Khoá đề xuất | Vị trí | Khung | Job id |
|---|---|---|---|
| r6_about_hero | Về chúng tôi | 4:3 | d64ba9d9-5ba3-4f45-b608-e56aa46ca7a6 |
| r6_phvsf_hero | PHVSF | 16:9 | be721a91-173c-4620-8423-f18f5b8d7f1a |
| r6_vns_hero | VNSHINE | 16:9 | e88526cd-7994-440f-82e9-48cb40a431ee |
| r6_member_hero | Quỹ thành viên | 4:5 | 9af8d1df-dd0b-4a43-b71b-93d1912fe4a0 |
| r6_pf_hero | Quản lý danh mục | 4:5 | b079f6d0-494e-4355-badf-ef54cb882ebf |
| r6_adv_hero | Tư vấn đầu tư | 4:5 | e13b79e5-dc82-43d8-a761-3753502e1c6b |
| r6_acad_hero | Học viện | 4:3 | 1ca9b9b4-d19c-462c-9515-3495fe63262b |
| r6_cr_hero | Tuyển dụng | 4:3 | 6d124989-9662-460c-9845-63b869222d6f |

## Issue mở chờ Rin

#9 (đóng khi merge R6-04), #10 (ảnh hero PHVSF mobile), #22 (ảnh PHVSF bị ô giá che — xét lại khi gắn ảnh mới), #31 (hero 中文 hẹp 44px), #34 và #25-loại (chữ 中文 còn tiếng Anh — cô Helena), #39 (ghi chú CMS lộ ở Danh sách quỹ), #40 ("1 documents"), #41 (form 768 tràn).
Câu hỏi phụ chưa trả lời: thêm nút Tải về Phiếu đăng ký cho tab Hồ sơ **tổ chức** ở Hướng dẫn PHVSF? Khối CTA Hướng dẫn PHVSF có đổi sang nền mist để không liền khối trắng Đại lý phân phối?
Rin cần gửi: nội dung PHVSF performance và overview EN từ phfm.vn (Q9, Q10), tên EN bốn giá trị, file Phiếu đăng ký và các biểu mẫu.

## Ghi chú kỹ thuật

- Các tầng vá: `patches.py` → `patches2.py` → `patches4.py` (PATCHES4) → `patches5.py` → `patches6.py` (R6-01) → `patches6b.py` (R6-02/03) → `patches6c.py` (R6-04/05). CSS: `r3.css` → `r4.css` → `r5.css` → `r6.css` → `r6b.css` → `r6c.css`.
- Nhánh xếp chồng: merge theo thứ tự; khi gộp chỉ xung đột ở danh sách PATCHES và changelog — giữ cả hai phía, một danh sách duy nhất.
- Agent `frontend` dùng Sonnet; vài commit ghi trailer Sonnet — không phải lỗi.
- Hạn mức 5 giờ bị chạm 2 lần hôm nay; nên chạy tối đa 2 agent song song.
