@echo off
setlocal enabledelayedexpansion

echo ==========================================
echo   📈 量化交易教程 - 自动化部署工具
echo ==========================================

:: 1. 同步 README 到 index.md
echo [1/3] 正在同步文档首页...
copy /Y README.md docs\index.md >nul
if %errorlevel% neq 0 (
    echo [错误] 无法同步 README.md，请检查文件是否存在。
    pause
    exit /b
)

:: 2. Git 提交

git push
if %errorlevel% neq 0 (
    echo [错误] 推送失败，请检查网络或 Git 配置。
    pause
    exit /b
)

echo.
echo [3/3] ✅ 部署指令已发送！
echo 网页将在几分钟内自动更新：https://Si-Xiaoming.github.io/quant-trade-tutorial/
echo.

set /p preview="是否启动本地预览 (y/n)? "
if /i "%preview%"=="y" (
    echo 启动 MkDocs 本地服务器...
    mkdocs serve
)

pause
