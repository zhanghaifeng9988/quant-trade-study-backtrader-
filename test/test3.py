import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import yfinance as yf
import time

tickers = ['AAPL', 'MSFT', 'GOOGL']

# 下载数据，加重试
for i in range(3):  # 最多试3次
    try:
        data = yf.download(tickers, start='2023-01-01', end='2024-01-01', progress=False)['Close']
        if not data.empty:
            break
    except Exception as e:
        print(f"第{i+1}次下载失败: {e}")
        time.sleep(5)  # 等5秒再试

# 检查数据是否下载成功
if data.empty:
    print("数据下载失败，请稍后再试")
else:
    rets = data.pct_change().dropna()
    pca = PCA(n_components=1)
    rets_pca = pca.fit_transform(rets)

    print("原始数据 data.shape:", data.shape)
    print("收益率 rets.shape:", rets.shape)
    print("PCA降维后 rets_pca.shape:", rets_pca.shape)
