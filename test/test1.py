import numpy as np
import pandas as pd
np.random.seed(42)
return_matrix = np.random.normal(0.001, 0.02, (5, 3))
print("收益率矩阵 (5天 x 3只股票):")
print(return_matrix)
