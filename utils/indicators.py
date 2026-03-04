"""
utils/indicators.py
常用技术指标计算函数库
"""
import numpy as np
import pandas as pd


def sma(series: pd.Series, period: int) -> pd.Series:
    """简单移动均线"""
    return series.rolling(period).mean()


def ema(series: pd.Series, span: int) -> pd.Series:
    """指数移动均线"""
    return series.ewm(span=span, adjust=False).mean()


def macd(series: pd.Series, fast=12, slow=26, signal=9):
    """
    MACD 指标
    返回: (macd_line, signal_line, histogram)
    """
    ema_fast = ema(series, fast)
    ema_slow = ema(series, slow)
    macd_line = ema_fast - ema_slow
    signal_line = ema(macd_line, signal)
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """相对强弱指数 RSI"""
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
    avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def bollinger_bands(series: pd.Series, window: int = 20, n_std: float = 2.0):
    """
    布林带
    返回: (upper, middle, lower, bandwidth)
    """
    middle = sma(series, window)
    std = series.rolling(window).std()
    upper = middle + n_std * std
    lower = middle - n_std * std
    bandwidth = (upper - lower) / middle
    return upper, middle, lower, bandwidth


def atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    """真实波动幅度均值 ATR"""
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs()
    ], axis=1).max(axis=1)
    return tr.ewm(com=period - 1, min_periods=period).mean()


def stochastic(high: pd.Series, low: pd.Series, close: pd.Series,
               k_period: int = 14, d_period: int = 3):
    """
    随机指标 KDJ
    返回: (K, D, J)
    """
    lowest_low = low.rolling(k_period).min()
    highest_high = high.rolling(k_period).max()
    rsv = (close - lowest_low) / (highest_high - lowest_low) * 100
    K = rsv.ewm(com=d_period - 1, adjust=False).mean()
    D = K.ewm(com=d_period - 1, adjust=False).mean()
    J = 3 * K - 2 * D
    return K, D, J


def momentum(series: pd.Series, period: int = 20) -> pd.Series:
    """动量指标（n日价格变化率）"""
    return series.pct_change(period)
