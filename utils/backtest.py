"""
utils/backtest.py
简单向量化回测引擎
"""
import numpy as np
import pandas as pd


def run_backtest(
    signals: pd.Series,
    prices: pd.Series,
    commission: float = 0.001,
    initial_capital: float = 100_000,
) -> pd.DataFrame:
    """
    向量化回测引擎

    参数
    ----
    signals     : 每日仓位信号 (1=多头, 0=空仓, -1=空头)
    prices      : 对应资产收盘价
    commission  : 每次换手手续费率（单边）
    initial_capital : 初始资金

    返回
    ----
    DataFrame 包含: position, daily_ret, strategy_ret, portfolio_value, drawdown
    """
    df = pd.DataFrame({'price': prices, 'signal': signals}).dropna()

    # 防止 look-ahead bias：信号次日才执行
    df['position'] = df['signal'].shift(1).fillna(0)

    # 日收益率
    df['daily_ret'] = df['price'].pct_change()

    # 策略收益
    df['strategy_ret'] = df['position'] * df['daily_ret']

    # 手续费（仅换手时扣除）
    df['trade'] = df['position'].diff().abs()
    df['strategy_ret'] -= df['trade'] * commission

    # 资产净值
    df = df.dropna()
    df['portfolio_value'] = initial_capital * (1 + df['strategy_ret']).cumprod()

    # 回撤
    rolling_max = df['portfolio_value'].cummax()
    df['drawdown'] = (df['portfolio_value'] - rolling_max) / rolling_max

    return df


def compute_metrics(returns: pd.Series, risk_free: float = 0.04) -> dict:
    """计算标准绩效指标字典"""
    n = len(returns)
    if n == 0:
        return {}

    total_ret = (1 + returns).prod() - 1
    annual_ret = (1 + total_ret) ** (252 / n) - 1
    annual_vol = returns.std() * np.sqrt(252)
    sharpe = (annual_ret - risk_free) / annual_vol if annual_vol > 0 else np.nan

    cum = (1 + returns).cumprod()
    rolling_max = cum.cummax()
    drawdown = (cum - rolling_max) / rolling_max
    mdd = drawdown.min()
    calmar = annual_ret / abs(mdd) if mdd != 0 else np.nan

    downside_vol = returns[returns < 0].std() * np.sqrt(252)
    sortino = (annual_ret - risk_free) / downside_vol if downside_vol > 0 else np.nan

    win_rate = (returns > 0).mean()

    return {
        'total_return': total_ret,
        'annual_return': annual_ret,
        'annual_volatility': annual_vol,
        'sharpe_ratio': sharpe,
        'sortino_ratio': sortino,
        'max_drawdown': mdd,
        'calmar_ratio': calmar,
        'win_rate': win_rate,
    }
