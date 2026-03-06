# 模块4：策略回测框架

“如果历史重演，我的想法能赚到钱吗？”回测是量化体系中最重要也最容易自欺欺人的一环。本模块带你手写回测引擎深刻理解背后机制，然后引入工业级的 Backtrader 框架。

## 📓 课程目录

| 文件序号 | 内容说明 |
|------|------|
| `00_strategy_thinking.ipynb` | 策略灵感来源：行为认知偏差与风险溢价补偿 |
| `01_simple_backtest.ipynb` | 从零手写向量化回测，彻底搞懂未来函数（Look-ahead Bias）与手续费累积 |
| `02_backtrader_intro.ipynb` | Backtrader 框架入门：四大组件协作与专业绩效汇报（夏普、回撤） |
| `03_performance_metrics.ipynb` | 策略评估指标准确计算与常见陷阱分析 |
| `04_classic_strategies.ipynb` | 跨市场经典选股与择时量化策略复现 |
| `05_beta_hedging.ipynb` | Beta 对冲与市场中性策略构建 |
| `06_pairs_trading_strategy.ipynb` | 实盘级统计套利与配对交易 |
| `07_kalman_filter_applications.ipynb` | 高级滤波器在动态对冲比例中的应用 |
| `08_market_impact_slippage.ipynb` | 模拟真实交易深度与冲击成本 |
| `09_long_short_equity.ipynb` | 多空股票对冲基金策略底层逻辑 |

## 🛡️ 防御性研究
永远对极高的回测收益保持怀疑。回测不是用来证明策略有多好，而是用来尝试证明策略是“错误”的。如果它一直没被证伪，那才值得真金白银投入。
