#!/usr/bin/env bash
# Chuẩn bị môi trường build + QA cho phfm_web. Chạy lại nhiều lần không sao.
# Dùng ở: Claude Code cloud (SessionStart hook), workspace Cowork, máy dev, GitHub Actions.
set -u
cd "$(dirname "$0")/.."
ok(){ printf '  ✓ %s\n' "$1"; }; warn(){ printf '  ! %s\n' "$1"; }
echo "phfm_web setup"

# 1. Python + Pillow (nén ảnh)
if python3 -c "import PIL" 2>/dev/null; then ok "Pillow $(python3 -c 'import PIL;print(PIL.__version__)')"
else pip install --quiet --break-system-packages pillow 2>/dev/null || pip install --quiet pillow || warn "không cài được Pillow"; fi

# 2. Node + Playwright (QA). Ưu tiên Playwright có sẵn trong máy (cloud có sẵn Chromium).
if node -e "require('playwright')" 2>/dev/null; then ok "Playwright có sẵn"
else
  npm install --no-audit --no-fund --silent >/dev/null 2>&1 && ok "npm install" || warn "npm install lỗi"
  node -e "require('playwright').chromium.executablePath()" >/dev/null 2>&1 || npx --yes playwright install --with-deps chromium >/dev/null 2>&1 || warn "chưa cài được Chromium"
fi


# 3. Thử build
if python3 src/build.py >/tmp/phfm_build.log 2>&1; then ok "build: $(tail -1 /tmp/phfm_build.log)"; else warn "build lỗi, xem /tmp/phfm_build.log"; fi
exit 0
