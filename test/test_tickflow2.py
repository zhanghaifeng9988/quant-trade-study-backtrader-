from dotenv import load_dotenv
import os
# 加载 .env 文件
load_dotenv()
# 读取环境变量
API_KEY = os.getenv('API_KEY')
import pandas as pd
import numpy as np
import datetime
from tickflow import TickFlow
from pathlib import Path #处理文件路径和文件系统操作
try:
    tf = TickFlow(api_key=API_KEY)
    start = int(datetime.datetime(2022, 1, 1).timestamp() * 1000)
    end = int(datetime.datetime(2026, 5, 22).timestamp() * 1000)
    df = tf.klines.get("600519.SH", period="1d", start_time=start, end_time=end,adjust="forward", as_dataframe=True)
    print(f"2022-2026年5月22日 共 {len(df)} 个交易日")
    print(df.tail())
    # # 2. 获取单只股票行情（以贵州茅台为例）
    # # k_type: 1.日；2.周；3.月
    # # adjust: 0.不复权；1.前复权；2.后复权
    # # mt_df = adata.stock.market.get_market(stock_code='600519', start_date='2022-01-01', k_type=1, adjust=1)
    # mt_df = adata.stock.market.get_market(stock_code='600519', k_type=1, start_date='2022-01-01')
    
#     print(f'adata 茅台数据样例:\n{mt_df}')
#     mt_df['list_date'] = pd.to_datetime(mt_df['list_date']) #将日期列转换为标准日期格式
#     mt_df.set_index('list_date', inplace=True) #将日期列设置为表格的行索引
    
#     # 保存
#     mt_df[['open', 'high', 'low', 'close', 'volume']].to_csv(DATA_DIR / 'adata_mt.csv')
#     mt_df[['open', 'high', 'low', 'close', 'volume']].to_parquet(DATA_DIR / 'adata_mt.parquet')
#     print(f'已保存 {len(mt_df)} 条数据至 adata_mt.csv')
#     mt_df.head()

except ImportError:#导入错误捕获
    print('⚠️   未安装，请运行: pip install ')
except Exception as e: #e 是错误对象的变量名，可以把它当作一个包含错误信息的"容器"
    print(f'获取数据出错: {e}')
