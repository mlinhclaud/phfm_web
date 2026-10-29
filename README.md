# phfm_web

Website phfm.vn (Công ty CP Quản lý Quỹ Phú Hưng): bản VI/EN tông Teal Vanguard, build thành một file HTML tự chứa.

```bash
bash scripts/setup.sh
python3 src/build.py      # -> dist/phfm-website.html
node qa/qa.js             # QA 20 trang × VI/EN × 1440/390
```

- Cách làm việc, luật, agent: [`CLAUDE.md`](CLAUDE.md)
- Luật thương hiệu và tuân thủ: [`specs/brand-rules.md`](specs/brand-rules.md)
- Bàn giao cho dev (MIN Solutions): [`specs/dev-handoff.md`](specs/dev-handoff.md)
- Nhật ký thay đổi: [`specs/changelog.md`](specs/changelog.md)
- Plan vòng hiện tại: [`plans/round-4.md`](plans/round-4.md)
- Artifact/canvas và cách đồng bộ với Cowork: [`specs/canvas-links.md`](specs/canvas-links.md)

Ảnh gốc trong `assets/source/` lưu dạng WebP chất lượng 92. Build chỉ cần `assets/img/`.
