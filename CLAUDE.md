# PHFM website (phfm_web)

Website phfm.vn của Công ty CP Quản lý Quỹ Phú Hưng (PHFM): bản VI/EN tông Teal Vanguard, build thành **một file HTML tự chứa** (`dist/phfm-website.html`). Bên MIN Solutions deploy. Claude không deploy lên phfm.vn.

Người duyệt: Rin (marketing PHFM). Trả lời Rin bằng tiếng Việt, câu ngắn, rõ, viết như người viết.

## Chạy

```bash
bash scripts/setup.sh          # cài Python/Pillow, Playwright chromium (bỏ qua nếu đã có)
python3 src/build.py           # -> dist/phfm-website.html (~9 MB)
node qa/qa.js                  # 20 trang × VI/EN × 1440/390 -> qa/out/ ; trả mã 1 nếu tràn ngang hoặc lỗi JS
PAGES="about vnshine" LANGS=vi WIDTHS=390 node qa/qa.js   # chạy một phần
node qa/insp.js /vi/phvsf 1440 "document.title"            # đọc DOM nhanh
node qa/shot.js /vi/vnshine 1440 ".pd-cell" qa/out/x.png   # chụp một khối
```

Mở trang: `dist/phfm-website.html#/vi/<trang>` (trang: home about funds phvsf vnshine member portfolio advisory ir news academy careers contact guidePhvsf guideVnshine faq glossary forms terms privacy).

## Cấu trúc

- `src/src_o8.html`: tài liệu gốc (dc-runtime: template + class `Component` + dữ liệu `window.PHFM_DATA`). **Không sửa trực tiếp.**
- `src/patches.py`, `src/patches2.py`: mọi thay đổi là một hàm vá; `rep(s, old, new)` kiểm tra số lần khớp, khớp sai là build dừng. Thêm vòng mới bằng file `src/patches<N>.py` hoặc thêm hàm vào `patches2.py`, đăng ký trong `PATCHES`.
- `src/parts/`: HTML/CSS/JS chèn vào (trang chủ, footer, theme.css, r3.css, site.js, tools.html…). CSS vòng mới viết vào file riêng (vd `r4.css`), nạp sau cùng.
- `src/images.py`: mỗi file `assets/img/<khoá>.<ext>` là một ảnh; template dùng `{{ img.<khoá> }}`, JS dùng `window.__I.<khoá>`.
- `src/edits.json`: chữ Rin sửa ở bảng Nội dung, áp lên `PHFM_DATA` lúc tải trang.
- `assets/source/`: ảnh gốc (WebP chất lượng 92, đủ để nén lại cho web). Ảnh mới: `python3 tools/add_image.py <gốc> <khoá> <rộng>`.
- `vendor/`: React 18.3.1 UMD, font Inter. Build không gọi mạng.
- `tools/canvas_gen.py`: sinh artboard cho canvas Trang con (Cowork đăng).
- `specs/`: quyết định, luật thương hiệu, bàn giao dev, nhật ký thay đổi. `plans/`: plan từng vòng.

Lưu ý runtime: `{{ }}` chỉ là đường dẫn tra cứu, không viết biểu thức; tính sẵn trong `renderVals()`. Chữ nội suy được bọc trong `span.sc-interp`. Có các script cũ chỉnh DOM sau render (mobile `fix/tight/nm`, căn chữ `okBlock`, gạch tiêu đề `hl-*`, hiệu ứng `.cr`); trang chủ (`[data-hm]`), footer (`.ft`) và `[data-keepgrid]` được loại trừ khỏi chúng.

## Luật bắt buộc

Đọc `specs/brand-rules.md` trước khi đụng vào giao diện hay chữ. Tóm tắt:
- Màu theo đúng bảng Teal Vanguard. Không nền đen/than chì. Không be, kem, nâu trong giao diện và ảnh. Ảnh dùng người trẻ.
- Inter cho web. Không tự vẽ logo.
- Không hứa hẹn lợi nhuận. Số liệu chưa xác minh dùng `[placeholder]`. Giữ cảnh báo rủi ro và dòng "Số liệu minh hoạ".
- Lỗi mới phát hiện ngoài plan: ghi vào issue và **hỏi Rin trước khi sửa**.
- Bản 中文 chỉ làm khi Rin duyệt.

## Skill thiết kế: design-taste-frontend (taste-skill v2)

Cài ở `.claude/skills/design-taste-frontend/` (Leonxlnx/taste-skill, commit `12af471`, MIT).
- **Dùng:** `references/critique.md`, `references/tells.md`, `layout.md`, `type.md` để phê bình; `scripts/inspect.mjs` để chụp và đo ở 1440/768/390; `scripts/lint.mjs` để quét. Coi kết quả lint là gợi ý.
- **Không dùng:** `draw.mjs` (direction, palette, font của skill), `assets.mjs` (ảnh từ kho mở), ảnh Lorem Picsum. Website đã có hệ nhận diện riêng.
- Luật của skill xung đột với PHFM (eyebrow label, số thứ tự 01/02/03 cho bước thật, đường kẻ mảnh, chân trang có đường kẻ…): **brand-rules thắng**. Chỉ bỏ những thứ thật sự là trang trí thừa.

## Agent và quy trình

| Vai trò | Agent | Model |
|---|---|---|
| Lập plan | `planner` | Opus 5.5, effort high |
| Triển khai front-end | `frontend` | Sonnet 5.5, effort high |
| Review | `reviewer` | Opus 5.5, effort high |

1. `planner` viết/cập nhật `plans/round-N.md` và tạo GitHub issue cho từng mục (nhãn `round-N`). Rin duyệt plan.
2. `frontend` làm từng mục trên nhánh `rN/<mã-việc>`, chạy build + QA, mở PR (mẫu `.github/pull_request_template.md`) kèm ảnh trước/sau 1440 và 390.
3. `reviewer` review PR, ghi Approve hoặc Request changes. Không tự merge.
4. Rin merge. `frontend` nối dòng vào `specs/changelog.md` trong chính PR đó.

## Làm song song Cowork và Claude Code cloud

- Cowork (claude.ai) làm việc cần kết nối riêng: tạo ảnh Higgsfield (model Nano Banana Pro), đọc/ghi artifact (bảng Nội dung, canvas), file trên máy Rin. Nhánh `cowork/*`, `sync/*`.
- Claude Code cloud làm code: nhánh `rN/*`. Không sửa `assets/source/` trừ khi issue yêu cầu.
- Trước khi bắt đầu một issue: gán bản thân (comment "đang làm") để bên kia không làm trùng. Mỗi PR nhỏ, một việc.
- Không push thẳng vào `main`.
- Không commit token, mật khẩu, file cá nhân.
