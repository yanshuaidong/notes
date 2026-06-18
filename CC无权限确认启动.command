#!/bin/bash
cd "$(dirname "$0")" || exit 1

# 临时切换到 Node 22（仅当前终端会话生效）
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm use 22

echo "Node 版本: $(node -v)"
echo "工作目录: $(pwd)"
echo "启动 Claude..."
echo

claude --dangerously-skip-permissions
