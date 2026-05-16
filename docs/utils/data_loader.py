"""
utils/data_loader.py
数据加载工具函数
"""
from __future__ import annotations
import pandas as pd
from pathlib import Path

DATASETS_DIR = Path(__file__).parent.parent / 'datasets'


def load_yfinance(tickers, start: str, end: str, field: str = 'Close') -> pd.DataFrame:
    """
    从 yfinance 下载数据（带缓存）

    参数
    ----
    tickers : str 或 list[str]
    start, end : 'YYYY-MM-DD'
    field : OHLCV 字段名

    返回
    ----
    pd.DataFrame，index 为日期，columns 为 ticker
    """
    import yfinance as yf
    data = yf.download(tickers, start=start, end=end, progress=False, auto_adjust=True)
    if isinstance(tickers, str):
        return data[field].to_frame(tickers)
    return data[field]


def load_csv(filename: str, **kwargs) -> pd.DataFrame:
    """
    从 datasets/ 目录加载 CSV 文件

    参数
    ----
    filename : 文件名（相对于 datasets/）
    **kwargs : 传递给 pd.read_csv

    示例
    ----
    df = load_csv('sp500_sample.csv', index_col=0, parse_dates=True)
    """
    path = DATASETS_DIR / filename
    if not path.exists():
        raise FileNotFoundError(
            f"找不到文件: {path}\n"
            f"可用文件: {list(DATASETS_DIR.glob('*.csv'))}"
        )
    defaults = {'index_col': 0, 'parse_dates': True}
    defaults.update(kwargs)
    return pd.read_csv(path, **defaults)


def save_csv(df: pd.DataFrame, filename: str):
    """将 DataFrame 保存至 datasets/ 目录"""
    path = DATASETS_DIR / filename
    df.to_csv(path)
    print(f'已保存: {path}')
