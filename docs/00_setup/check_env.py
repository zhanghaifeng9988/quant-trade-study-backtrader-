"""
check_env.py — 环境检测脚本
运行: python check_env.py
"""

import sys

REQUIRED_PACKAGES = {
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "plotly": "plotly",
    "scipy": "scipy",
    "sklearn": "scikit-learn",
    "yfinance": "yfinance",
    "ta": "ta",
    "backtrader": "backtrader",
    "xgboost": "xgboost",
    "lightgbm": "lightgbm",
    "cvxpy": "cvxpy",
    "tqdm": "tqdm",
}

OPTIONAL_PACKAGES = {
    "akshare": "akshare",
    "torch": "torch",
    "pypfopt": "PyPortfolioOpt",
}


def check_package(import_name, display_name):
    try:
        mod = __import__(import_name)
        version = getattr(mod, "__version__", "unknown")
        print(f"  ✅ {display_name:<22} v{version}")
        return True
    except ImportError:
        print(f"  ❌ {display_name:<22} 未安装 → pip install {display_name}")
        return False


def main():
    print("=" * 50)
    print("  量化交易教程 — 环境检测")
    print("=" * 50)
    print(f"\nPython 版本: {sys.version}")

    if sys.version_info < (3, 9):
        print("⚠️  建议使用 Python 3.9 及以上版本\n")

    print("\n📦 必要依赖：")
    required_ok = all(
        check_package(imp, disp) for imp, disp in REQUIRED_PACKAGES.items()
    )

    print("\n📦 可选依赖：")
    for imp, disp in OPTIONAL_PACKAGES.items():
        check_package(imp, disp)

    print("\n" + "=" * 50)
    if required_ok:
        print("🎉 所有必要依赖已安装，可以开始学习！")
    else:
        print("⚠️  请安装缺少的依赖后重新运行此脚本")
        print("   提示: pip install -r requirements.txt")
    print("=" * 50)


if __name__ == "__main__":
    main()
