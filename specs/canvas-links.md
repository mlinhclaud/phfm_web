# Artifact, canvas và cách đồng bộ

Các artifact dưới đây chỉ đọc/ghi được từ Cowork (claude.ai), không vào được từ Claude Code cloud. Mọi dữ liệu cần cho build đều được Cowork export vào repo.

| Tên | Link | Dùng để | Dữ liệu trong repo |
|---|---|---|---|
| Website PHFM - Teal Vanguard (trang chủ) | https://claude.ai/artifact/H5PmzQhszv1547fQn8aabv | Thiết kế trang chủ VI/EN, desktop/mobile | `src/parts/home.html`, `home.css`, `th.js`, ảnh `hm_*` |
| Website PHFM - Teal Vanguard · Trang con | https://claude.ai/artifact/B6qoNVM6TuiXgi7R8vZhc5 | 19 trang con (VI, desktop) để Rin chỉnh bố cục, màu, ảnh | `specs/canvas/published/` (bản đã đăng gần nhất) |
| Nội dung website PHFM | https://claude.ai/artifact/4xo1FeZWDZZV3Uy7CErh1f | Rin sửa chữ VI/EN; ghi yêu cầu khác | `specs/content-edits.json` → `src/edits.json` |
| Audit website PHFM C+B | https://claude.ai/artifact/EWvfAaxUcoCbmthDyv5ExD | Quyết định vòng 1–2 | `specs/audit-decisions.md` |
| PHFM Teal Editorial (design system) | https://claude.ai/artifact/PekYinK6dcUwREhm7xVVZ9 | Token màu, chữ cho canvas | `specs/brand-rules.md` |

## Quy trình đồng bộ (Cowork làm)

**Chữ Rin sửa ở bảng Nội dung**
1. Cowork đọc collection `edits` của bảng Nội dung, ghi vào `specs/content-edits.json` và `src/edits.json` (mảng `{p, vi, en}`).
2. Đọc collection `requests`, chuyển mỗi yêu cầu chưa làm thành một GitHub issue nhãn `request`.
3. Mở PR `sync/content-YYYYMMDD`.

**Bố cục Rin sửa trên canvas Trang con**
1. Cowork đọc các artboard đã đổi, so với `specs/canvas/published/<file>`.
2. Ghi phần khác nhau vào `plans/canvas-diff-YYYYMMDD.md` (artboard, vùng, thay đổi CSS/markup).
3. Agent frontend chuyển các thay đổi đó vào `src/` (patches, parts). Không chép nguyên artboard đè lên code.
4. Sau khi merge, Cowork chạy `python3 tools/canvas_gen.py` và đăng lại canvas, cập nhật `specs/canvas/published/`.

**Ảnh mới**
- Higgsfield chỉ dùng được từ Cowork. Cowork tạo ảnh, lưu gốc vào `assets/source/generated/`, nén bằng `tools/add_image.py`, mở PR.
- Ảnh mới cần hiện trên canvas: upload làm asset của canvas rồi thêm dòng `tên-file id` vào `specs/canvas/blobs.txt` và khoá vào `specs/canvas/manifest.json`.
