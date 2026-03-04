# 示例数据集

本目录包含用于演示和练习的示例数据集。

## 文件说明

| 文件 | 说明 | 来源 |
|------|------|------|
| `sp500_sample.csv` | 美股代表性股票（AAPL/MSFT/GOOGL/AMZN/SPY）日线收盘价 | yfinance，2020-2024 |
| `stock_daily.csv` | A股示例日线数据（默认：贵州茅台 600519） | AKShare，2022-2024 |

## 如何更新数据

```python
from utils.data_loader import load_yfinance, save_csv

# 重新下载美股数据
prices = load_yfinance(['AAPL','MSFT','GOOGL','AMZN','SPY'],
                        start='2020-01-01', end='2024-12-31')
save_csv(prices, 'sp500_sample.csv')
```

## 数据格式

所有 CSV 文件均遵循以下格式：
- 第一列为日期索引（YYYY-MM-DD）
- 价格列为复权后收盘价
- 编码：UTF-8
