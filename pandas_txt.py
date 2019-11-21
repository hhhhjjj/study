import pandas as pd
data = pd.read_table('1.txt',sep='	')
# print(data)
# print(data.iloc[[0,1,2],[0,1]])
# 这个还算比较好用
data = data.drop(columns=["Time"])
# 去掉时间这一列
new_data = data.loc[:, (data != 0).any(axis=0)]
# 删除全为0的列
# print(new_data)
new_data.to_csv("new_1.csv",index=False)
# 还是保存成csv方便些



