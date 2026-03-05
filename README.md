# 📈 量化交易从零到一教程

> 面向零基础同学的量化交易完整学习路径，涵盖金融概念、算法原理、Python 实现与策略回测。

---

## 🗺️ 学习路线图

```
模块0：环境配置
    ↓
模块1：金融基础概念（数学基础、价格与收益、风险、市场、概率与模拟、GARCH、统计、时序）
    ↓
模块2：数据获取与处理（yfinance / 数据清洗 / 特征工程）
    ↓
模块3：技术指标与信号（趋势、动量、波动率、标的筛选、协整与相关性）
    ↓
模块4：策略回测框架（策略思维、手写回测、backtrader、绩效、经典策略、对冲、配对交易、卡尔曼、冲击成本、多空）
    ↓
模块5：投资组合优化（Markowitz、风险平价、CAPM/APT、因子分析、风险模型、VaR/CVaR、协方差估计）
    ↓
模块6：机器学习与量化（因子选择、预测、深度学习、过拟合、交叉验证、高级组合优化、杠杆与保证金）
```

---

## 📁 项目结构

```
quant-trade-tutorial/
├── README.md
├── environment.yml               # conda 环境配置（推荐）
├── start.bat                     # 一键启动 Jupyter（Windows）
├── 00_setup/                     # 模块0：环境配置
│   ├── 00_env_setup.ipynb
│   └── check_env.py
├── 01_financial_concepts/        # 模块1：金融基础
│   ├── 00_math_foundations.ipynb
│   ├── 01_price_and_return.ipynb
│   ├── 02_risk_and_volatility.ipynb
│   ├── 03_market_basics.ipynb
│   ├── 04_probability_and_simulation.ipynb
│   ├── 05_garch_volatility.ipynb
│   ├── 06_statistics_fundamentals.ipynb
│   └── 07_time_series_analysis.ipynb
├── 02_data/                      # 模块2：数据获取与处理
│   ├── 01_data_sources.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_feature_engineering.ipynb
├── 03_indicators/                # 模块3：技术指标
│   ├── 01_trend_indicators.ipynb
│   ├── 02_momentum_indicators.ipynb
│   ├── 03_volatility_indicators.ipynb
│   ├── 04_universe_selection.ipynb
│   └── 05_cointegration_correlation.ipynb
├── 04_backtesting/               # 模块4：策略回测
│   ├── 00_strategy_thinking.ipynb
│   ├── 01_simple_backtest.ipynb
│   ├── 02_backtrader_intro.ipynb
│   ├── 03_performance_metrics.ipynb
│   ├── 04_classic_strategies.ipynb
│   ├── 05_beta_hedging.ipynb
│   ├── 06_pairs_trading_strategy.ipynb
│   ├── 07_kalman_filter_applications.ipynb
│   ├── 08_market_impact_slippage.ipynb
│   └── 09_long_short_equity.ipynb
├── 05_portfolio/                 # 模块5：投资组合优化
│   ├── 01_markowitz.ipynb
│   ├── 02_risk_parity.ipynb
│   ├── 03_capm_apt.ipynb
│   ├── 04_factor_analysis.ipynb
│   ├── 05_risk_models.ipynb
│   ├── 06_var_cvar.ipynb
│   └── 07_covariance_estimation.ipynb
├── 06_ml_trading/                # 模块6：机器学习量化
│   ├── 01_feature_selection.ipynb
│   ├── 02_ml_prediction.ipynb
│   ├── 03_deep_learning.ipynb
│   ├── 04_dangers_of_overfitting.ipynb
│   ├── 05_cross_validation.ipynb
│   ├── 06_advanced_portfolio_optimization.ipynb
│   └── 07_leverage_and_margin.ipynb
├── datasets/                     # 示例数据集
└── utils/                        # 共享工具函数
    ├── backtest.py
    ├── data_loader.py
    ├── indicators.py
    └── plot_utils.py
```

---

## ⚡ 快速开始

### conda（推荐）

```bash
conda env create -f environment.yml
conda activate quant
jupyter notebook
```

或直接双击 `start.bat`（Windows）。

### 验证环境

```bash
python 00_setup/check_env.py
```

---

## 📚 各模块内容概览

| 模块 | 主题 | 核心内容 |
|------|------|----------|
| 00 | 环境配置 | Conda 安装、包管理、Jupyter 使用 |
| 01 | 金融基础 | 数学基础、收益率、波动率、GARCH、时序分析 |
| 02 | 数据处理 | yfinance 数据下载、清洗、特征工程 |
| 03 | 技术指标 | 趋势/动量/波动率指标、标的筛选、协整 |
| 04 | 策略回测 | 手写回测、backtrader、绩效评估、配对交易、卡尔曼滤波 |
| 05 | 组合优化 | Markowitz、风险平价、CAPM/APT、VaR/CVaR |
| 06 | 机器学习 | 因子选择、XGBoost、LSTM、过拟合与交叉验证 |

---

## 🛠️ 主要依赖

| 类别 | 包 |
|------|----|
| 数据处理 | `numpy`, `pandas` |
| 可视化 | `matplotlib`, `seaborn` |
| 科学计算 | `scipy` |
| 机器学习 | `scikit-learn`, `xgboost` |
| 深度学习 | `pytorch` (CUDA 12.1), `torchvision`, `torchaudio` |
| 时序/统计 | `statsmodels`, `arch-py` (GARCH) |
| 卡尔曼滤波 | `pykalman` |
| 数据获取 | `yfinance` |
| 回测框架 | `backtrader` |
| 开发工具 | `jupyter`, `notebook`, `ipykernel` |

---

## 📝 学习建议

1. **按顺序学习** — 模块之间有依赖关系
2. **动手运行代码** — 每个 notebook 都有可交互的示例
3. **修改参数** — 改变参数观察结果变化，加深理解
4. **做笔记** — 在 notebook 中记录自己的思考

---

## 📖 参考资源

- [Quantopian Lectures](https://github.com/quantopian/research_public)
- [Backtrader 文档](https://www.backtrader.com/docu/)
- [awesome-quant (中文)](https://github.com/thuquant/awesome-quant)
