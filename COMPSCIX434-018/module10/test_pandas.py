import pandas as pd

s = pd.Series([1, 3, 5, 6, 8])
print(s)
print(s.sum())
print(s.mean())
print(s.std())
print(s.loc[0])

# 从字典创建，字典的 key 会成为索引
s_dict = pd.Series({'a': 10, 'b': 20, 'c': 30})
print(s_dict)


# 从字典创建 (最常用)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'LA', 'TX']
}
df = pd.DataFrame(data)
print(df)
print(df.loc[0:1, 'Name':'Age'])
print("======head========")
print(df.head(3))
print("======tail========")
print(df.tail(2))
print("======groupby========")
print(df.groupby('City')
      ['Age'].mean())
#
# # 从列表的列表创建，并指定列名
# data_list = [[1, 'A'], [2, 'B'], [3, 'C']]
# df_list = pd.DataFrame(data_list, columns=['Number', 'Letter'])
# print(df_list)