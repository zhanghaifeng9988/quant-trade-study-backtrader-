# 📈 量化交易从零到一教程

> 面向零基础同学的量化交易完整学习路径，涵盖金融概念、算法原理、Python 实现与策略回测。

---

## 🗺️ 学习路线图

```
模块0：环境配置
    ↓
模块1：金融基础概念（价格、收益、风险）
    ↓
模块2：数据获取与处理（yfinance / AKShare / Tushare）
    ↓
模块3：技术指标与信号（MA, RSI, MACD, Bollinger Bands）
    ↓
模块4：策略回测框架（手写 + backtrader）
    ↓
模块5：投资组合优化（Markowitz, 风险平价）
    ↓
模块6：机器学习与量化（XGBoost, LSTM）
```

---

## 📁 项目结构

```
trade_tutorial/
├── README.md
├── requirements.txt          # pip 依赖
├── environment.yml           # conda 环境配置
├── 00_setup/                 # 模块0：环境配置
├── 01_financial_concepts/    # 模块1：金融基础
├── 02_data/                  # 模块2：数据获取与处理
├── 03_indicators/            # 模块3：技术指标
├── 04_backtesting/           # 模块4：策略回测
├── 05_portfolio/             # 模块5：投资组合优化
├── 06_ml_trading/            # 模块6：机器学习量化
├── datasets/                 # 示例数据集
└── utils/                    # 共享工具函数
```

---

## ⚡ 快速开始

### 方式一：conda（推荐）

```bash
conda env create -f environment.yml
conda activate quant-tutorial
jupyter lab
```

### 方式二：pip + venv

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
jupyter lab
```

### 验证环境

```bash
python 00_setup/check_env.py
```

---

## 📚 各模块内容概览

| 模块 | 主题 | 核心内容 |
|------|------|----------|
| 00 | 环境配置 | Python 安装、包管理、Jupyter 使用 |
| 01 | 金融基础 | 收益率、波动率、夏普比率、市场结构 |
| 02 | 数据处理 | 数据下载、清洗、特征工程 |
| 03 | 技术指标 | 趋势、动量、波动率指标 |
| 04 | 策略回测 | 回测框架、绩效评估、常见陷阱 |
| 05 | 组合优化 | 均值方差、有效前沿、风险平价 |
| 06 | 机器学习 | 因子选择、监督学习、深度学习 |

---

## 🛠️ 主要依赖

- `pandas` / `numpy` — 数据处理
- `matplotlib` / `seaborn` / `plotly` — 数据可视化
- `yfinance` / `akshare` — 数据获取
- `scipy` / `scikit-learn` — 数学工具 / 机器学习
- `backtrader` — 策略回测框架
- `xgboost` / `lightgbm` — 梯度提升
- `torch` — 深度学习（LSTM）

---

## 📝 学习建议

1. **按顺序学习** — 模块之间有依赖关系
2. **动手运行代码** — 每个 notebook 都有可交互的示例
3. **修改参数** — 改变参数观察结果变化，加深理解
4. **做笔记** — 在 notebook 中记录自己的思考

---

## 📖 参考资源

- [Quantopian Lectures](https://github.com/quantopian/research_public)
- [Quant-RA](https://github.com/dafuzhuu/Quant-RA)
- [Backtrader 文档](https://www.backtrader.com/docu/)
- [awesome-quant (中文)](https://github.com/thuquant/awesome-quant)
