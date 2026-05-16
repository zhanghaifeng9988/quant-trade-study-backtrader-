"""
utils/plot_utils.py
可视化工具函数
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_price_with_signals(prices: pd.Series, buy_dates=None, sell_dates=None,
                             title: str = '价格走势', figsize=(13, 5)):
    """绘制价格曲线 + 买卖信号标记"""
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(prices.index, prices.values, linewidth=1.2, color='steelblue', label='价格')
    if buy_dates is not None and len(buy_dates) > 0:
        ax.scatter(buy_dates, prices.loc[buy_dates],
                    marker='^', color='green', s=100, zorder=5, label='买入')
    if sell_dates is not None and len(sell_dates) > 0:
        ax.scatter(sell_dates, prices.loc[sell_dates],
                    marker='v', color='red', s=100, zorder=5, label='卖出')
    ax.set_title(title, fontsize=13)
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    return fig, ax


def plot_cumulative_returns(*return_series, labels=None, figsize=(12, 5),
                             title='累积收益对比'):
    """对比多条收益曲线"""
    fig, ax = plt.subplots(figsize=figsize)
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    if labels is None:
        labels = [f'策略{i+1}' for i in range(len(return_series))]

    for i, (rets, label) in enumerate(zip(return_series, labels)):
        cum = (1 + rets).cumprod()
        ax.plot(cum.index, cum.values, label=label,
                 linewidth=1.8, color=colors[i % len(colors)])

    ax.axhline(1, color='gray', linestyle='--', alpha=0.5)
    ax.set_title(title, fontsize=13)
    ax.set_ylabel('累积净值')
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    return fig, ax


def plot_drawdown(returns: pd.Series, title: str = '回撤曲线', figsize=(12, 4)):
    """绘制回撤曲线"""
    cum = (1 + returns).cumprod()
    rolling_max = cum.cummax()
    drawdown = (cum - rolling_max) / rolling_max

    fig, ax = plt.subplots(figsize=figsize)
    ax.fill_between(drawdown.index, drawdown.values, 0, color='red', alpha=0.4)
    ax.plot(drawdown.index, drawdown.values, color='darkred', linewidth=0.8)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
    ax.set_title(f'{title}  |  最大回撤: {drawdown.min():.2%}', fontsize=12)
    ax.set_ylabel('回撤')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    return fig, ax


def plot_monthly_heatmap(returns: pd.Series, title: str = '月度收益热力图'):
    """蜡烛图 + 月度收益热力图"""
    try:
        import seaborn as sns
    except ImportError:
        print('需要安装 seaborn: pip install seaborn')
        return

    monthly = returns.resample('ME').apply(lambda x: (1 + x).prod() - 1)
    df = monthly.to_frame('ret')
    df['year'] = df.index.year
    df['month'] = df.index.month_name().str[:3]

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
    pivot = df.pivot_table(index='year', columns='month', values='ret', observed=False)

    fig, ax = plt.subplots(figsize=(14, max(4, len(pivot) * 0.5 + 2)))
    sns.heatmap(pivot, annot=True, fmt='.1%', cmap='RdYlGn',
                center=0, linewidths=0.5, ax=ax, annot_kws={'size': 9})
    ax.set_title(title, fontsize=13)
    plt.tight_layout()
    return fig, ax
