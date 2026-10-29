#!/usr/bin/env bash
# Mỗi phiên Claude Code (cloud hoặc máy) tự chuẩn bị môi trường.
bash "${CLAUDE_PROJECT_DIR:-.}/scripts/setup.sh" 2>&1 | tail -8
exit 0
