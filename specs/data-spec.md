# Specs dữ liệu và tích hợp · website PHFM bản Teal

Bản build hiện là một file HTML tĩnh. Mọi nội dung nằm trong `window.PHFM_DATA` (song ngữ), số liệu quỹ sinh từ chuỗi minh hoạ. Tài liệu này liệt kê dữ liệu nào dev cần chuyển sang CMS/API khi dựng bản thật, kèm hành vi mong muốn.

Quy ước: `text{vi,en}` là một chuỗi hai ngôn ngữ (`b(vi, en)` trong code). Bản 中文 lấy từ bảng `window.PHFM_ZH` (khoá là chữ EN); khoá chưa có thì hiện chữ EN.

## 1. Định tuyến và ngôn ngữ

- URL dạng `#/<lang>/<trang>`, `lang` = `vi | en | zh`. 20 trang: home, about, funds, phvsf, vnshine, member, portfolio, advisory, ir, news, academy, careers, contact, guidePhvsf, guideVnshine, faq, glossary, forms, terms, privacy.
- Chuyển sang URL thật (`/vi/phvsf`): sửa `__phfmRoute` và `__phfmSetHash` ở đầu `<head>`, cấu hình rewrite về trang gốc. `document.title` đổi theo trang (bảng tiêu đề trong `head_route.html`).

## 2. Số liệu quỹ (PHVSF, VNSHINE) · ưu tiên nối API

| Trường | Hiện tại | Cần từ CMS/API |
|---|---|---|
| `PHFM_ASOF` | `'2026-10-14'` cố định | Ngày của dòng NAV mới nhất. **Không dùng ngày người xem mở trang** |
| Chuỗi NAV | `fundCalc()` sinh chuỗi minh hoạ từ `PHFM_ANCHORS` | Mỗi ngày giao dịch: ngày, NAV/CCQ, giá đóng cửa (ETF), iNAV (ETF), chỉ số tham chiếu (VN-Index cho PHVSF, VNSHINE Index cho VNSHINE) |
| Hiệu quả theo kỳ | Tính từ chuỗi (1 ngày, 1/3/6 tháng, YTD, 1/3 năm, từ khi thành lập) | Tính ở client từ chuỗi thật, hoặc API trả sẵn. Kỳ chưa đủ dữ liệu trả `null` (hiện "—") |
| Thông tin quỹ `funds.<mã>.info` | Văn bản cố định | Bảng thuộc tính (ngân hàng giám sát, phí, ngày giao dịch…) quản lý trong CMS |
| Ban điều hành `team2` | Cố định | CMS |
| Dòng "Số liệu minh hoạ, cập nhật đến ngày…" | Hiện ở mọi khối số | **Xoá khi nối số thật** |

Mọi khối (hero, bảng hiệu quả, biểu đồ, Lịch sử NAV, thông tin giao dịch, Danh sách quỹ) lấy từ cùng một chuỗi nên luôn khớp nhau. Code có ghi chú `DEV:` ở `fundCalc()`.

## 3. Tài liệu

| Nơi | Cấu trúc một dòng | Loại (bộ lọc) |
|---|---|---|
| Tài liệu quỹ `funds.<mã>.docs` | `{c: mã loại, t: tên, d: mô tả, date: 'dd.mm.yyyy', size}` + cần thêm `url` | 9 loại (bình luận #134 trên bảng góp ý): Báo cáo ngày, tuần / Báo cáo tài chính / Báo cáo hoạt động tháng / Factsheets / Bản cáo bạch / Điều lệ quỹ / Thông tin quỹ / Giấy phép / Khác |
| Công bố thông tin `ir.items` | `{e: đơn vị, ty: loại, t: tên, date, y: năm}` + `url` | 8 loại (bình luận #116 trên bảng góp ý): Thông báo quỹ / Điều lệ quỹ / Bản cáo bạch / Báo cáo tài chính / Báo cáo hoạt động tháng / Báo cáo NAV ngày, tuần / Biểu mẫu / Factsheet. Đơn vị: PHFM, PHVSF, VNSHINE ETF, HTDF, VPDF |
| Biểu mẫu `forms.groups[].items` | `{t, d}` + `url` | Nhóm theo quỹ/dịch vụ |

- Hiện chưa có file: bấm tải hiện thông báo "Tài liệu đang được cập nhật" (`site.js`, regex `DL`). Có file thì gắn `href` và bỏ khớp regex cho nút đó.
- "Tải tài liệu đã chọn (n)": nên gọi API nén ZIP ở server.
- Loại chưa có tài liệu vẫn hiện trong bộ lọc, chọn vào thì hiện một dòng "Tài liệu đang được cập nhật".

## 4. Form (chưa gửi dữ liệu đi đâu)

| Form | Trang | Trường | Ghi chú |
|---|---|---|---|
| Liên hệ | contact | Họ và tên*, Email*, Số điện thoại*, Tỉnh/thành, Bạn là (5 lựa chọn), Bạn cần hỗ trợ về (chủ đề), Nội dung, đồng ý xử lý dữ liệu | Hiện báo gửi thành công ở client |
| Liên hệ dịch vụ tổ chức | member, portfolio, advisory | Họ và tên, Tổ chức, Email, Số điện thoại, Nội dung, ô đồng ý xử lý dữ liệu cá nhân | |
| Nhận báo cáo thị trường | news | Email | Có thông báo thành công/lỗi (`nlOk`, `nlErr`) |
| Ứng tuyển | careers | Gửi email `cskh@phfm.vn` (mailto) | Có thể đổi sang form upload CV |

Dev cần: API nhận form (hoặc email), chống spam (captcha/hidden field), lưu đồng ý xử lý dữ liệu cá nhân kèm thời điểm, email xác nhận. Điều khoản xử lý dữ liệu cần pháp chế duyệt.

## 5. Tìm kiếm

- Chạy ở client trên `PHFM_DATA`: tên trang, bài viết, FAQ, thuật ngữ, biểu mẫu, công bố thông tin, việc làm. Gõ không dấu vẫn ra.
- Khi nội dung lên CMS: giữ cách này nếu dữ liệu tải về client, hoặc thay bằng API tìm kiếm có cùng nhóm kết quả.

## 6. Link giao dịch và ứng dụng

| Link | Đích hiện tại |
|---|---|
| Nút "PHFM Trading" ở header (mọi trang) | `https://fund.phfm.vn/home` |
| Nút "Đầu tư ngay" ở hero PHVSF | `https://fund.phfm.vn` |
| Link giao dịch ở Hướng dẫn PHVSF | `https://fund.phfm.vn/home` |
| Hero VNSHINE | Không có link giao dịch (ETF mua bán qua công ty chứng khoán) |
| App Store | `https://apps.apple.com/us/app/phfm-mobile/id6451093704` |
| Google Play | `https://play.google.com/store/apps/details?id=com.fplatform.PhuHung&pcampaignid=web_share&pli=1` (dev có thể bỏ hai tham số chia sẻ `pcampaignid`, `pli`). Nút "Tải app để đầu tư ngay" ở PHVSF chỉ dẫn tới Google Play |
| Hotline / email | `tel:02854137991`, `mailto:phfm@phfm.vn`, `mailto:cskh@phfm.vn` |
| Mạng xã hội | LinkedIn, Facebook, YouTube, Instagram, Zalo OA (footer) |

Dev kiểm lại các link này với PHFM trước go-live.

## 7. Nội dung khác trong `PHFM_DATA`

| Khoá | Nội dung | Gợi ý CMS |
|---|---|---|
| `ui` | Menu, nút, chân trang, Danh sách quỹ | Bảng chuỗi giao diện |
| `about` | Giới thiệu, 4 số liệu, Lịch sử hình thành (`phases`), Sứ mệnh/Tầm nhìn, Giá trị cốt lõi (`values`: chữ Hán + tên), Ban lãnh đạo (`leaders`: tên, chức vụ, tiểu sử, `eduZh`) | Trang + danh sách nhân sự |
| `services` | Quỹ thành viên, Quản lý danh mục, Tư vấn | Trang dịch vụ |
| `news` | `insights` và `news`: `{img, cat, date, t, s, a}` + nội dung bài | Bài viết (ảnh bìa, chuyên mục, ngày, tiêu đề, tóm tắt, tác giả, nội dung, file PDF) |
| `academy` | Hướng dẫn, so sánh, thuật ngữ (`glossFull`), FAQ (`faqFull`) | Thuật ngữ, FAQ |
| `careers` | Văn hoá, việc làm (`jobs`, `jds`) | Tin tuyển dụng |
| `contact` | Địa chỉ, giờ làm việc, lựa chọn form | Cài đặt chung |
| `legal` | Điều khoản, Chính sách bảo mật | Trang tĩnh, pháp chế duyệt |

Chữ Rin sửa ở bảng "Nội dung website PHFM" được áp lên `PHFM_DATA` lúc tải trang (`src/edits.json`). Khi có CMS thì nhập thẳng vào CMS.

## 8. Ảnh

- Ảnh nhúng base64 trong `window.__I` (mỗi ảnh một lần). Khi deploy nên tách ra file riêng để trình duyệt cache. Chất lượng: WebP q84, hero 1920px, thẻ 960px. Danh sách và nguồn: `specs/image-sources.json`, ảnh gốc `assets/source/`.
