import pandas as pd
try:
        from tickflow import TickFlow
        # 使用免费服务（无需 API key）
        tf = TickFlow.free()
        df = tf.klines.get("600000.SH", period="1d", count=100, as_dataframe=True)
        print(df.tail(20)) #pandas得dataFrame格式
except ImportError:
        print('⚠️  TickFlow 未安装')
except Exception as e:
        print(f'TickFlow  数据获取失败: {e}')
universes = tf.universes.list()
top10_universes = universes[:10] #列表中得前10个值
print(top10_universes) # 这是list类型，里面包含得全是字典类型得数据，接下来我们把他们转换成pandas得dataFrame格式
df1 = pd.DataFrame(top10_universes)
print(f'转成后得数据内容：\n{df1}')
for u in top10_universes:
        print(f"{u['id']}: {u['name']} ({u['symbol_count']} 只)")

# 获取标的池详情（含全部标的代码）
universes2 = tf.universes.get("CN_Equity_A")
print(type(universes2))  # 先看看是什么类型
# clearprint(universes2)        # 打印出来看看内容结构
df_complete = pd.DataFrame({
    'id': [universes2['id']] * len(universes2['symbols']),#创建一个列表，其中包含重复 N 次的 universes2['id'] 值，N 等于股票的数量。
    'name': [universes2['name']] * len(universes2['symbols']),
    'description': [universes2['description']] * len(universes2['symbols']),
    'region': [universes2['region']] * len(universes2['symbols']),
    'category': [universes2['category']] * len(universes2['symbols']),
    'symbol': universes2['symbols']
})
print(f'\n转成后得数据内容-前10行：\n{df_complete.head(10)}')
print(f'\n转成后得数据内容-后10行：\n{df_complete.tail(10)}')
print(f"A 股共 {len(universes2['symbols'])} 只")
etf_universe = tf.universes.get("CN_ETF")
print(type(etf_universe))  # 先看看是什么类型
# print(etf_universe)
etf_complete = pd.DataFrame({
    'id': [etf_universe['id']] * len(etf_universe['symbols']),#创建一个列表，其中包含重复 N 次的 universes2['id'] 值，N 等于股票的数量。
    'name': [etf_universe['name']] * len(etf_universe['symbols']),
    'description': [etf_universe['description']] * len(etf_universe['symbols']),
    'region': [etf_universe['region']] * len(etf_universe['symbols']),
    'category': [etf_universe['category']] * len(etf_universe['symbols']),
    'symbol': etf_universe['symbols']
})
print(f'\n转成后得数据内容-前10行：\n{etf_complete.head(10)}')
print(f'\n转成后得数据内容-后10行：\n{etf_complete.tail(10)}')
print(f"ETF 共 {len(etf_universe['symbols'])} 只")

