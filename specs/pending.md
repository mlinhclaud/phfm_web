# Việc còn chờ trước go-live · website PHFM bản Teal

Cập nhật 31/10/2026, sau vòng 6 (đã gồm sửa #47: đậm màu số % trong thẻ giá). Danh sách này gom mọi chỗ còn thiếu file, thiếu số thật, hoặc chờ người duyệt. Chi tiết kỹ thuật ở `specs/dev-handoff.md`, `specs/data-spec.md`.

## 1. Placeholder: thiếu file, link hoặc số thật

| Chỗ | Trang | Hiện tại | Cần |
|---|---|---|---|
| Chuỗi NAV, giá, chỉ số tham chiếu | PHVSF, VNSHINE, Danh sách quỹ, trang chủ | Chuỗi minh hoạ từ `fundCalc()`, ngày `PHFM_ASOF = 2026-10-14` | API/CMS số thật. Xoá dòng "Số liệu minh hoạ…" khi nối |
| Tài liệu quỹ (từng file) | PHVSF, VNSHINE | Nút tải hiện "Tài liệu đang được cập nhật" | `url` từng file. API nén ZIP cho "Tải tài liệu đã chọn" |
| Loại tài liệu chưa có file | PHVSF, VNSHINE | Một dòng tạm "Tài liệu đang được cập nhật" | Factsheets, Thông tin quỹ, Giấy phép (cả hai quỹ); Khác (PHVSF); Báo cáo tài chính (VNSHINE) |
| Công bố thông tin | IR | Danh sách mẫu, chưa có file | `url` từng tài liệu; loại Điều lệ quỹ, Biểu mẫu, Factsheet chưa có mục nào |
| Biểu mẫu | Biểu mẫu, Hướng dẫn PHVSF | Nút "Tải về" hiện thông báo | File PDF các biểu mẫu, Phiếu đăng ký mở tài khoản (Rin gửi) |
| Form liên hệ, form dịch vụ, nhận báo cáo | Liên hệ, Quỹ thành viên, Quản lý danh mục, Tư vấn, Tin tức | Chỉ báo thành công ở trình duyệt | API hoặc email nhận form, chống spam, lưu đồng ý xử lý dữ liệu |
| Ứng tuyển | Tuyển dụng | `mailto:cskh@phfm.vn` | Xác nhận email nhận CV hoặc form upload |
| Bản đồ | Liên hệ | Hình vẽ | Google Maps embed (nếu muốn) |
| Số tài khoản nhận tiền | Hướng dẫn PHVSF | Số đang có trong bản gốc | Vận hành/pháp chế xác nhận |
| Nội dung PHVSF từ phfm.vn | PHVSF (EN) | Giữ như hiện tại | Rin gửi trang performance và overview EN (Q9, Q10) |
| Tên EN bốn giá trị Tân · Tốc · Thực · Giản | Về chúng tôi | Chờ | Rin gửi (Q4) |
| Link giao dịch, app, mạng xã hội | Toàn site | Xem `specs/data-spec.md` mục 6 | Dev kiểm lại với PHFM |

## 2. Chờ pháp chế

Chữ mới áp ở VI, EN viết tương đương. Pháp chế cần duyệt trước go-live:

- "Tỷ suất Lợi nhuận Cổ đông" thay "Lợi suất Cổ đông" toàn site (Q5). EN giữ "Shareholder Yield".
- "Quỹ ETF đầu tiên tại Việt Nam được xây dựng theo Chiến lược Tỷ suất Lợi nhuận Cổ đông" (hero, thẻ VNSHINE). Chữ "đầu tiên" cần xác nhận; không xác nhận được thì đổi "một trong những quỹ ETF tiên phong" (Q6).
- Nhãn hero PHVSF "QUỸ MỞ" / "OPEN-ENDED FUND".
- "Tài liệu đang được cập nhật." / "This document is being updated."
- Khối Biểu mẫu ở Hướng dẫn PHVSF: "Xem tất cả biểu mẫu" / "View all forms".
- Về chúng tôi, nhãn số liệu EN: "18+ years of operation", "2,000+ bn VND AUM", "4 fund products".
- Điều khoản đồng ý xử lý dữ liệu cá nhân ở các form.
- Hồ sơ còn ghi "CMND" (B05). Bài MSCI cần ghi nguồn số liệu (B06).
- Toàn bộ chữ EN của các trang con.

## 3. Chờ cô Helena (中文)

Claude không tự dịch bản 中文. Những chỗ đang hiện chữ EN hoặc cần duyệt:

- Nhãn hero PHVSF "OPEN-ENDED FUND".
- Dòng "Tài liệu đang được cập nhật", 9 tên loại tài liệu quỹ.
- Ba nhãn số liệu Về chúng tôi (trước đây có "營運年數", "總管理資產"; nay hiện EN giống trang chủ).
- Khối Biểu mẫu ở Hướng dẫn PHVSF: tiêu đề và nút đều là "表單", lead còn tiếng Anh.
- Các chữ 中文 còn tiếng Anh ở issue #34.
- "Tỷ suất Lợi nhuận Cổ đông" bản 中文 đang là "股東收益率" (không đổi).

## 4. Issue mở chờ Rin quyết

| Issue | Nội dung |
|---|---|
| #10 | Hero PHVSF trên mobile: ảnh gần như bị lớp teal phủ |
| #22 | Ảnh PHVSF bị ô giá che (ảnh mới không có người, xét lại) |
| #31 | Hero 中文 hẹp 44px |
| #34 | Chữ 中文 còn tiếng Anh |
| #39 | Ghi chú CMS lộ ở Danh sách quỹ |
| #40 | "1 documents" |
| #41 | Form ở 768 bị tràn |
| #49 | Ô tick từng tài liệu chưa dùng được bằng bàn phím |
| #50 | EN "Thông báo quỹ" đang là "Fund Information", trùng "Thông tin quỹ" |
| #55 | Bản EN còn viết số kiểu Việt (dấu phẩy thập phân, dấu chấm hàng nghìn) |
| #8 | Đăng lại canvas Trang con theo bản build cuối (việc của Cowork) |
| #56 | PHVSF 390px: nút Công cụ nổi đè cột "Từ khi thành lập" của thẻ giá |
| #7 | R4-06 QA tổng vòng 4: đã thay bằng QA tổng vòng 6 (240 lượt xanh), Rin đồng ý thì đóng |

Câu hỏi phụ:
- Có thêm nút Tải về Phiếu đăng ký cho tab Hồ sơ tổ chức ở Hướng dẫn PHVSF không?
- Khối CTA Hướng dẫn PHVSF có đổi sang nền mist không?
- Ở 768px, nút Tải về cao 40px, link "Xem tất cả biểu mẫu" cao 19px. Có nâng lên 44px cho máy tính bảng không?
- Hàng số liệu Về chúng tôi có cả "tỷ VND" và "tỷ VNĐ". Có đồng bộ không?
- Ảnh hero Học viện có mặt bàn gỗ sáng. Có giữ không?
