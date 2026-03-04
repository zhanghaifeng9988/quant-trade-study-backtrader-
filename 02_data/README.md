# 模块2：数据获取与处理

量化交易的核心之一是**高质量的数据**。本模块介绍主流数据源的使用方法，以及数据清洗的关键技巧。

## 内容

| 文件 | 说明 |
|------|------|
| `01_data_sources.ipynb` | yfinance（美股）、AKShare（A股）数据获取 |
| `02_data_cleaning.ipynb` | 缺失值处理、异常值检测、复权处理 |
| `03_feature_engineering.ipynb` | 从 OHLCV 构建有效特征：滞后项、滚动统计量 |

## 常用数据源

| 数据源 | 覆盖市场 | 是否免费 | 说明 |
|--------|----------|----------|------|
| [yfinance](https://pypi.org/project/yfinance/) | 美股、全球 | ✅ 免费 | Yahoo Finance API |
| [AKShare](https://akshare.akfun.cn/) | A股、港股 | ✅ 免费 | 聚合多源数据 |
| [Tushare](https://tushare.pro/) | A股 | 部分免费 | 需注册获取 Token |
| [Quandl/Nasdaq Data Link](https://data.nasdaq.com/) | 全球 | 部分免费 | 高质量基本面数据 |
