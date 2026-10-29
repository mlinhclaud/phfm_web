# Quyết định audit website (vòng 1–2)

Nguồn: artifact "Audit website PHFM C+B" (https://claude.ai/artifact/EWvfAaxUcoCbmthDyv5ExD), collection `decisions` và `picks`. Xuất ngày 30/10/2026.

Nhóm A: lỗi kỹ thuật/giao diện. Nhóm B: nội dung, số liệu, tuân thủ. Nhóm C: đổi tông teal. Nhóm I: ảnh.

## Lỗi và đề xuất

| Mã | Mức | Trang | Thiết bị | Vấn đề | Đề xuất | Quyết định của Rin | Ghi chú của Rin |
|---|---|---|---|---|---|---|---|
| A01 | Cao | Tất cả trang | Desktop + Mobile | Không có đường dẫn riêng cho từng trang | Thêm đường dẫn theo dạng #vi/vnshine, #en/about… Back/F5/chia sẻ link chạy đúng. Không đổi giao diện hay nội dung. | Sửa |  |
| A02 | Cao | Hướng dẫn VNSHINE | Mobile | Khối “Bắt đầu đầu tư” cuối trang bị mất nền | Cho khối này dùng chung kiểu nền với khối tương ứng ở Hướng dẫn PHVSF. | Sửa |  |
| A03 | Cao | Về chúng tôi, VNSHINE, Hướng dẫn VNSHINE | Desktop + Mobile | Logo đối tác đang lấy trực tiếp từ website khác | Lưu file logo vào trong website. Cần Rin gửi bộ logo chính thức của các đối tác (hoặc đồng ý để mình dùng bản từ trang chủ của từng đối tác). | Trao đổi thêm | lấy từ D:\AI\PHFM\Partner |
| A04 | Cao | Footer mọi trang | Desktop + Mobile | Icon mạng xã hội trỏ sai địa chỉ | Gắn link fanpage/kênh chính thức của PHFM. Cần Rin gửi 3 link. | Sửa | https://www.youtube.com/@PhuHungFundManagement https://www.facebook.com/phuhungfm🔸Linkedin: www.linkedin.com/company/phu-hung-fund-management 🔸Instagram: www.instagram.com/phuhungfm/ 🔸Zalo: https://zalo.me/1596901652048517862 |
| A05 | Trung bình | Biểu mẫu, Tài liệu quỹ (PHVSF, VNSHINE), Công bố thông tin | Desktop + Mobile | Nút tải tài liệu chưa có file | Gắn file thật nếu Rin có. Chưa có file thì để nút hiện thông báo “Tài liệu đang được cập nhật” thay vì nhảy trang. | (chưa chọn) | ok theo đề xuất. chưa có tài liệu |
| A06 | Trung bình | Header mọi trang | Desktop + Mobile | Ô tìm kiếm chưa hoạt động | Làm tìm kiếm trong site: tìm theo tên trang, bài viết, thuật ngữ, câu hỏi FAQ, tài liệu. Kết quả hiện trong bảng xổ xuống. | Sửa |  |
| A07 | Trung bình | Liên hệ, Quỹ thành viên, Quản lý danh mục, Tư vấn, Góc nhìn | Desktop + Mobile | Các form chưa gửi dữ liệu đi đâu | Phần này bên dev cần nối hệ thống nhận (email/CRM). Mình chỉ ghi chú lại trong file, không sửa. | Bỏ qua |  |
| A08 | Thấp | Tất cả trang | — | Lỗi ngầm khi tải trang | Dọn để console sạch: ảnh/icon chỉ gắn nguồn sau khi có dữ liệu. | Sửa |  |
| A09 | Trung bình | PHVSF, VNSHINE | Desktop + Mobile | Ô chọn ngày hiển thị kiểu Mỹ | Đổi sang ô ngày định dạng dd/mm/yyyy cho bản VI, giữ mm/dd cho EN nếu Rin muốn. | Sửa |  |
| A10 | Trung bình | Nhiều trang (Giới thiệu, quỹ, hướng dẫn) | Desktop + Mobile, nặng nhất ở EN | Căn đều 2 lề làm chữ bị hở | Giữ căn đều ở đoạn rộng trên desktop, chuyển căn trái cho cột hẹp và toàn bộ mobile. | Sửa |  |
| A11 | Trung bình | Toàn site | — | File nặng 12,9 MB | Nén ảnh (giảm còn khoảng 3–4 MB), bỏ font không dùng. Vẫn giữ 1 file HTML mở trực tiếp được. | Sửa | nén ảnh nhưng không được làm giảm chất lượng hiển thị khi deploy |
| A12 | Thấp | Toàn site | — | Tải font không dùng trên web | Bỏ 2 font này, chỉ giữ Inter (và Noto cho bản 中文 ở giai đoạn 3). | Sửa |  |
| A13 | Thấp | Footer mọi trang | Desktop + Mobile | Gạch phân cách thừa ở footer | Footer sẽ thay theo footer của homepage Teal Vanguard nên lỗi này tự hết. | Sửa |  |
| A14 | Thấp | VNSHINE, Góc nhìn (EN) | Desktop + Mobile | Bản EN còn sót tiếng Việt | Dịch: “Download portfolio composition file (PCF) ↓”, “PHFM Investment Division”. | Sửa |  |
| A15 | Thấp | Tuyển dụng (VI) | Desktop + Mobile | Bản VI còn chữ tiếng Anh | Đổi thành “Khối Vận hành”. | Bỏ qua |  |
| A16 | Trung bình | Danh sách quỹ | Desktop + Mobile | Khung “Ghi chú demo · Mục CMS” đang hiện cho người xem | Ẩn khung này ở bản chính. Ghi chú chuyển vào tài liệu bàn giao cho dev. | Sửa |  |
| A17 | Trung bình | Liên hệ | Desktop + Mobile | Bản đồ là hình vẽ giả | Thay bằng ảnh bản đồ tông teal và nút “Mở Google Maps”. Bên dev nhúng bản đồ thật khi lên web. | Bỏ qua |  |
| A18 | Thấp | Trang 中文 | Desktop + Mobile | Nút 中文 trên trang con chưa đổi ngôn ngữ | Để giai đoạn 3 xử lý cùng bản 中文. | Sửa |  |
| B01 | Cao | PHVSF, VNSHINE, Danh sách quỹ | Desktop + Mobile | Số liệu giả lập nhưng ngày tự cập nhật theo hôm nay | Cố định ngày, gắn nhãn “Số liệu minh họa” và [placeholder] ở các ô số. Bên dev nối nguồn NAV thật khi lên web. | Sửa | số liệu không tự nhảy theo ngày mở trang mà nhảy tự động theo ngày số liệu cập nhật. note chỗ này cho bên dev |
| B02 | Cao | PHVSF, VNSHINE, Danh sách quỹ | Desktop + Mobile | Số liệu mâu thuẫn giữa các khối | Đi chung với B01: đưa về một nguồn số, các khối lấy cùng số. | Sửa |  |
| B03 | Cao | Hướng dẫn PHVSF | Desktop + Mobile | Số tài khoản nhận tiền cần xác nhận | Không sửa. Nhờ Vận hành xác nhận trước khi public. | Bỏ qua |  |
| B04 | Thấp | Học viện Đầu tư | Desktop + Mobile | Ví dụ tính lãi chưa ghi rõ là minh họa | Thêm dòng nhỏ: “Ví dụ minh họa, không phải cam kết lợi nhuận.” (chờ pháp chế duyệt câu chữ). | Sửa |  |
| B05 | Thấp | Hướng dẫn PHVSF | Desktop + Mobile | Hồ sơ còn ghi “CMND” | Để pháp chế quyết, mình không tự sửa nội dung. | Bỏ qua |  |
| B06 | Thấp | Góc nhìn & Tin tức | Desktop + Mobile | Bài MSCI có số liệu cần nguồn | Nhờ Khối Đầu tư xác nhận nguồn. Không sửa. | Bỏ qua |  |
| C01 | Retheme | Hầu hết trang con | Desktop + Mobile | Màu ngoài bộ teal | Nền kem → mist #E3EEF0 viền vàng; lớp phủ kem → trắng/mist; tiêu đề một màu #0A3440; nút thống nhất #E9C46A (hover #F2D27D); đường so sánh trên biểu đồ → teal-grey #86B4BE; màu tăng → #15897D. | Sửa |  |
| C02 | Retheme | Về chúng tôi, PHVSF, VNSHINE, Học viện, Hướng dẫn, Quản lý danh mục, Tư vấn, Tuyển dụng, Góc nhìn | Desktop + Mobile | Ảnh tông be/nâu hoặc có người lớn tuổi | Xem bảng “Ảnh thay thế”. | Sửa |  |

## Ảnh

| Mã | Vị trí | Ảnh cũ | Vấn đề | Đề xuất ban đầu | Quyết định | Ảnh dùng cuối cùng |
|---|---|---|---|---|---|---|
| I01 | Hero · Về chúng tôi | advisor | 2 khách lớn tuổi, bàn gỗ | 214-tu-van-khach-hang.png | Sửa | 214-tu-van-khach-hang.png |
| I02 | Nền Sứ mệnh / Tầm nhìn · Về chúng tôi | coinplant | Đồng xu trên mặt gỗ, tông nâu | 236-tam-nhin-san-thuong.png | Trao đổi thêm | 237-mat-kinh-truu-tuong.png |
| I03 | Hero PHVSF, hero Hướng dẫn PHVSF, thẻ PHVSF ở Học viện, nền CTA Hướng dẫn PHVSF | dc_stones | Đá cuội nền be, ảnh nhỏ bị mờ | 239-tay-nang-mam-cay.png | Trao đổi thêm | 235-cap-doi-xem-app.png |
| I04 | Hero VNSHINE, hero Hướng dẫn VNSHINE, thẻ VNSHINE ở Học viện, nền CTA Hướng dẫn VNSHINE | dc_vntower | Tòa nhà vàng ấm, ảnh nhỏ bị mờ | 244-vnshine-binh-minh-thanh-pho.png | Sửa | 244-vnshine-binh-minh-thanh-pho.png (crop bỏ dải teal trên) |
| I05 | Hero · Quản lý danh mục | docs | Nội thất be, áo be | 221-xem-danh-muc-tablet.png | Trao đổi thêm | hf_..._145703_104ff3c1 |
| I06 | Hero · Tư vấn đầu tư | office | Hoàng hôn cam, ly cà phê nâu | 225-chuyen-vien-phan-tich.png | Trao đổi thêm | 224 (sau đổi sang ảnh riêng ở vòng 3) |
| I07 | Hero · Học viện Đầu tư | planner | Tường be, áo be | 238-workshop-nha-dau-tu.png | Trao đổi thêm | hf_..._160011_d3fb7c09 |
| I08 | Tuyển dụng · thẻ 01 Học hỏi từ thực tiễn | desk | Văn phòng nắng chiều tông cam | 233-van-phong-mo.png | Trao đổi thêm | ảnh mới tạo bằng Higgsfield (hf_20261029_132430_1ee739b2) |
| I09 | Tuyển dụng · thẻ 02 Chủ động & trách nhiệm | handshake | Tông ấm | 224-doi-ngu-hop-phong-kinh.png | Sửa | 224-doi-ngu-hop-phong-kinh.png |
| I10 | Tuyển dụng · thẻ 03 Cùng nhau phát triển | office | Trùng ảnh trang Tư vấn, tông cam | hf_20261021_160012_2f931d30-4796-47c0-bab0-6c89ca9fd914.png | Sửa | hf_20261021_160012_2f931d30 |
| I11 | Tuyển dụng · thẻ 04 Kết nối quốc tế | plant | Cây bonsai nền be | hf_20261021_155213_fd88d3b9-0fb0-48fd-b7b0-c98ea30f277d.png | Trao đổi thêm | hf_..._160011_59a4433a |
| I12 | Góc nhìn · Cập nhật vĩ mô tháng 8 | planner | Áo be, tường be | 202-ca-phe-app-dau-tu.png | Trao đổi thêm | 245-vnshine-ban-lam-viec-chi-so.png |
| I13 | Góc nhìn · Đầu tư định kỳ và bình quân giá vốn | planner | Trùng ảnh bài trên | 231-so-tay-duong-tang.png | Trao đổi thêm | 206-cap-doi-lap-ke-hoach.png |
| I14 | Góc nhìn · Kỷ luật tái cân bằng | docs | Nội thất be | 222-doc-bao-cao-quy.png | Trao đổi thêm | 221-xem-danh-muc-tablet.png |
| I15 | Góc nhìn · Đọc báo cáo tài chính quỹ | docs | Trùng ảnh bài trên | 246-tin-bao-cao-chien-luoc.png | Trao đổi thêm | hf_..._160011_d070e025 |
| I16 | Góc nhìn · Báo cáo thị trường tháng 8 | tower | Thành phố lúc hoàng hôn, tông cam | 228-flycam-khu-tai-chinh.png | Sửa | 228-flycam-khu-tai-chinh.png |
| I17 | Góc nhìn · Triển vọng thị trường nửa cuối năm | g_book | Sổ tay trên mặt đá be | 252-cta-flatlay-da-trang.png | Trao đổi thêm | 241-hero-kinh-vien-vong.png |
| I18 | Góc nhìn · Cổ tức tiền mặt và mua lại cổ phiếu | coinplant | Đồng xu trên mặt gỗ | 216-flatlay-ban-da.png | Trao đổi thêm | 239-tay-nang-mam-cay.png |

## Ngoài danh sách audit (vòng 3, 29/10)

- Hero VNSHINE: ảnh mới tạo bằng Higgsfield (`r3_vns_hero`). Hero Tư vấn đầu tư: ảnh riêng (`r3_adv_hero`).
- Ảnh bìa bài MSCI và Luân chuyển ngành: thay ảnh nền kem (`r3_nw_msci`, `r3_nw_rot`).
- A03 đã xong: đủ 15 logo đối tác từ folder Partner, nhúng vào file.
- A04 đã xong: thêm icon Instagram, Zalo (tạo bằng Higgsfield, đổi màu teal #0B6274).
