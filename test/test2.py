import numpy as np
import matplotlib.pyplot as plt

# 生成10000个符合正态分布的随机数
np.random.seed(42)
data = np.random.normal(0.001, 0.02, 10000)

# 画直方图
plt.figure(figsize=(10, 5))
plt.hist(data, bins=50, edgecolor='black', alpha=0.7, density=True)

# 标注均值
plt.axvline(0.001, color='red', linestyle='--', linewidth=2, label='均值=0.001')

# 标注 ±1个标准差
plt.axvline(0.001 + 0.02, color='orange', linestyle='--', linewidth=1.5, label='+1个标准差 (0.021)')
plt.axvline(0.001 - 0.02, color='orange', linestyle='--', linewidth=1.5, label='-1个标准差 (-0.019)')

# 标注 ±2个标准差
plt.axvline(0.001 + 0.04, color='green', linestyle=':', linewidth=1.5, label='±2个标准差')
plt.axvline(0.001 - 0.04, color='green', linestyle=':', linewidth=1.5)

plt.title('正态分布：均值=0.001, 标准差=0.02')
plt.xlabel('收益率')
plt.ylabel('概率密度')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
