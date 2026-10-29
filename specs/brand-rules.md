# Quy tắc thương hiệu và tuân thủ cho website PHFM

Áp dụng cho mọi thay đổi trên website. Khi skill thiết kế, design system hay gợi ý nào khác mâu thuẫn với file này, file này thắng.

## Màu (bảng Teal Vanguard của trang chủ)

| Vai trò | Mã |
|---|---|
| Teal chính, link, nút phụ | `#0B6274` |
| Teal đậm: hero trang con, thanh mục con, khối nhấn | `#0A3440` |
| Mist: nền phụ, nền khối thông tin | `#E3EEF0` |
| Viền, đường kẻ | `#D8E7EA` |
| Vàng nút (nút chính) | `#E9C46A` (hover `#F2D27D`) |
| Vàng logo: chữ nhấn, chữ Hán Tân Tốc Thực Giản | `#C0962D` |
| Màu tăng (số dương) | `#15897D` |
| Chữ chính / chữ phụ | `#16262B` / `#4D6066` |

- Không thêm tông màu mới ngoài bảng trên.
- Không dùng nền đen, nền than chì (charcoal).
- Không dùng màu be, kem, nâu trong giao diện và trong ảnh.
- Màu đỏ/xanh lá chỉ dùng cho số liệu tăng giảm.

## Chữ

- Web: Inter (đã nhúng sẵn latin + vietnamese, 300–700).
- Chữ Hán (bản 中文, chữ 新 速 實 簡): Noto Serif TC/SC, nhúng bản subset.
- Playfair chỉ dùng cho social, không dùng trên web.

## Ảnh

- Người trong ảnh là người trẻ (khoảng 25–40 tuổi), trang phục trắng, xanh nhạt, teal.
- Bối cảnh sáng, văn phòng hiện đại, thành phố HCMC. Không tông be/nâu/cam hoàng hôn.
- Được dùng ảnh AI nếu ảnh nhìn thật, không có cảm giác AI. Tạo ảnh bằng Higgsfield, model **Nano Banana Pro** (`nano_banana_pro`, độ phân giải 2k trở lên). Không dùng các model GPT Image.
- Mỗi vị trí dùng một ảnh riêng, không trùng giữa các trang.
- Không tự vẽ logo PHFM hay logo đối tác. Chỉ dùng file chính thức (assets/source/partner).
- Nén WebP bằng `tools/add_image.py`: hero/dải ngang 1920px, thẻ/ảnh bài 960px, chất lượng 84. Không làm giảm độ nét khi hiển thị.

## Nội dung và tuân thủ (ngành quản lý quỹ)

- Không hứa hẹn hay ngụ ý cam kết lợi nhuận.
- Số liệu chưa xác minh để `[placeholder]`, không tự bịa.
- Giữ dòng "Số liệu minh hoạ, cập nhật đến ngày …" cho tới khi có số thật từ CMS.
- Giữ câu cảnh báo "Hiệu suất trong quá khứ không đảm bảo kết quả trong tương lai" và dòng rủi ro ở chân trang.
- Nội dung mới phải qua pháp chế duyệt trước khi go-live.
- Ngày số liệu quỹ lấy theo ngày cập nhật dữ liệu (`PHFM_ASOF`), không theo ngày người xem mở trang.
- "Shareholder Yield" tiếng Việt đã chốt: "Tỷ suất Lợi nhuận Cổ đông".
- PHFM là quỹ tiên phong dùng chỉ số VNSHINE, không có quyền độc quyền: không viết như thể độc quyền.
- Khi quỹ đi sau chỉ số: nói trung thực nhưng khéo, không né số liệu.
- Tiếng Trung (tên gọi, thuật ngữ) lấy theo phfm.vn/zh. Cô Helena duyệt bản tiếng Trung.

## Văn phong

- Chữ trên web và trong tài liệu phải đọc như người viết: câu ngắn, rõ, không sáo rỗng.
- Tránh các dấu hiệu văn AI: từ đệm phóng đại ("vượt trội", "hàng đầu", "toàn diện"), cấu trúc "không chỉ… mà còn…", liệt kê ba cho đủ nhịp, gạch ngang chèn ý, câu kết tóm tắt thừa.
- Tiếng Việt và tiếng Anh tương đương về nghĩa, không cần dịch từng chữ.
