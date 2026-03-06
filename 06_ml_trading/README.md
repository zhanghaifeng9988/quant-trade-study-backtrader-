# 模块6：机器学习与量化

当传统的线性模型和简单指标不足以挖掘市场中非线性的微弱信号时，机器学习便成为了顶级机构的利器。但金融市场的低信噪比使得 AI 模型极易过拟合。本模块教你如何防御性地使用机器学习。

## 📓 课程目录

| 文件序号 | 内容说明 |
|------|------|
| `01_feature_selection.ipynb` | 多重共线性诊断，利用互信息与 LASSO 正则化进行特征降维与挑选 |
| `02_ml_prediction.ipynb` | 基于树模型（XGBoost/Random Forest）的收益方向预测 |
| `03_deep_learning.ipynb` | 时序深度模型（LSTM/Transformer）在市场预测中的尝试 |
| `04_dangers_of_overfitting.ipynb` | 深入理解过拟合陷阱：不要被训练集的完美曲线欺骗 |
| `05_cross_validation.ipynb` | 带时序保护的 Purged K-Fold 交叉验证技术 |
| `06_advanced_portfolio_optimization.ipynb` | 层次风险平价（HRP）等高级机器学习优化方法 |
| `07_leverage_and_margin.ipynb` | 凯利公式与杠杆风险管理 |

## ⚠️ 机器学习铁律
金融不是图像识别！图像里的一只猫无论如何翻转还是猫（模式固定），但金融市场的规律一旦被广泛发现就会失效。严格的正则化（Regularization）和带“时序保护”的验证机制是模型落地的核心保障。
