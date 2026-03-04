# 模块6：机器学习与量化交易

机器学习为量化交易提供了更强大的信号挖掘能力，但也带来了更高的过拟合风险。

## 内容

| 文件 | 说明 |
|------|------|
| `01_feature_selection.ipynb` | 因子重要性、相关性筛选、信息比率 |
| `02_ml_prediction.ipynb` | XGBoost/LightGBM 预测涨跌方向 |
| `03_deep_learning.ipynb` | LSTM 时序预测简介 |

## ML 量化的核心挑战

1. **金融数据的低信息密度** — 信噪比极低
2. **非平稳性** — 统计规律随时间变化
3. **过拟合** — 样本内好，样本外差（"炼金术"陷阱）
4. **执行风险** — 模型预测与实际交易有差距

> 💡 推荐阅读：Marcos López de Prado《Advances in Financial Machine Learning》
