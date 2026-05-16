# 📈 量化交易从零到一教程

> 面向零基础同学的量化交易完整学习路径，涵盖金融概念、算法原理、Python 实现与策略回测。本系列教程采用统一的标准化结构，所有 Notebook 均包含“这一节讲什么”、“学习目标”、“正文内容”和“🎯 练习”。

---

## 🗺️ 学习路线图

```
模块0：环境配置
    ↓
模块1：金融基础概念（数学基础、价格收益、风险、市场、概率模拟、GARCH、统计、时序分析、现值、AR过程）
    ↓
模块2：数据获取与处理（数据源、数据清洗、特征工程）
    ↓
模块3：技术指标与信号（趋势、动量、波动率、股票池选股、协整与相关性）
    ↓
模块4：策略回测框架（策略思维、简单回测、backtrader、绩效评估）
    ↓
模块5：投资组合优化（Markowitz、风险平价）
    ↓
模块6：机器学习与量化（特征筛选、预测建模）
    ↓
后续进阶模块：基本面量化(07)、期货与大宗商品(08)、高频交易(09)、数学方法(10)
```

---

## 📁 项目结构

```
quant-trade-tutorial/
├── README.md                     # 本文件
├── environment.yml               # conda 环境配置（推荐）
├── start.bat                     # 一键启动 Jupyter（Windows）
├── 00_setup/                     # 模块0：环境配置
├── 01_financial_concepts/        # 模块1：金融基础
├── 02_data/                      # 模块2：数据获取与处理
├── 03_indicators/                # 模块3：技术指标
├── 04_backtesting/               # 模块4：策略回测
├── 05_portfolio/                 # 模块5：投资组合优化
├── 06_ml_trading/                # 模块6：机器学习量化
├── 07_fundamental/               # 模块7：基本面量化因子
├── 08_futures/                   # 模块8：期货与商品策略
├── 09_hft/                       # 模块9：高频交易与微观结构
├── 10_math_methods/              # 模块10：量化数学方法
├── datasets/                     # 示例数据集
└── utils/                        # 共享工具函数
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
| 01 | 金融基础 | 收益率、波动率、GARCH、概率模拟、统计基础、时序分析、现值估值 |
| 02 | 数据处理 | 常见数据源下载、数据清洗清洗、收益率特征工程 |
| 03 | 技术指标 | 趋势/动量/波动率指标、Universe 选股过滤、协整配对检验 |
| 04 | 策略回测 | 策略思维来源、手写回测框架、backtrader 框架应用 |
| 05 | 组合优化 | Markowitz 均值方差优化 |
| 06 | 机器学习 | 因子库特征选择与降维 |
| 07 | 基本面量化 | 财务报表、价值因子、质量因子挖掘 |
| 08 | 期货策略 | 期货基础、商品动量、期限结构 |
| 09 | 高频交易 | 订单簿底层逻辑、做市商模型基础 |
| 10 | 数学方法 | 蒙特卡洛、线性规划、马尔可夫链 |

---

## 🛠️ 主要依赖

| 类别 | 包 |
|------|----|
| 数据处理 | `numpy`, `pandas` |
| 可视化 | `matplotlib`, `seaborn` |
| 科学计算 | `scipy` |
| 机器学习 | `scikit-learn`, `xgboost` |
| 深度学习 | `pytorch` (CUDA 12.1) |
| 时序/统计 | `statsmodels`, `arch` (GARCH) |
| 数据获取 | `yfinance`, `akshare`, `adata` |
| 回测框架 | `backtrader` |
| 开发工具 | `jupyter`, `notebook` |

---

## 📝 学习建议

1. **按顺序学习** — 模块之间有强依赖关系，每一个 notebook 的文末都指明了下一步。
2. **动手运行代码** — 每个 notebook 都有可交互的示例与 `🎯 练习`。
3. **修改参数** — 改变参数观察结果变化，加深理解。
4. **做笔记** — 在 notebook 中记录自己的思考。

---

## 📖 参考资源

- [QuantEcon](https://quantecon.org/)
- [Backtrader 文档](https://www.backtrader.com/docu/)
