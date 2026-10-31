# Gói bàn giao vòng 6 (cập nhật 31/10/2026, sau PR #53)

- `phfm-website-r6.html`: bản build cuối của vòng 6, giống `dist/phfm-website.html` khi build từ commit này. Mở bằng trình duyệt, thêm `#/vi/phvsf`, `#/en/about`, `#/zh/home`… vào cuối đường dẫn.
- `screens/`: ảnh toàn trang của 20 trang × VI/EN/中文. Có hai bộ: `-1440.jpg` (thu còn 1080px rộng) và `-390.jpg` (cỡ điện thoại).
- Đọc tiếp:
  - `specs/dev-handoff.md`: ghi chú kỹ thuật;
  - `specs/ui-spec.md`: giao diện;
  - `specs/data-spec.md`: dữ liệu và tích hợp;
  - `specs/pending.md`: việc còn chờ.

QA lúc đóng gói:
- 240 lượt (20 trang × VI/EN/中文 × 1440/1024/768/390): không tràn ngang, không lỗi JS.
- Trang chủ so với đầu vòng 6: 0 điểm ảnh khác ở cả 12 tổ hợp (4 cỡ màn hình × 3 ngôn ngữ).
