#!/usr/bin/env bash
# Dán vào "Setup script" của môi trường cloud tại claude.ai/code (Environment → Edit).
# Chạy một lần khi tạo máy, trước khi Claude Code khởi động. Phần còn lại do .claude/hooks/session-start.sh lo.
apt-get update -qq || true
apt-get install -y -qq python3-pil >/dev/null 2>&1 || true
exit 0
