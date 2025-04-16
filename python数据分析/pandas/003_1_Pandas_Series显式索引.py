import numpy
import pandas

ser_1 = pandas.Series({1:150,"numpy":100,"pandas":120})
# print(ser_1)
"""
1         150
numpy     100
pandas    120
dtype: int64
"""

# 使用显示索引：使用索引名称
"""
# print(ser_1.1)
# 数值型索引没有办法直接点
# 会报错：SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(ser_1[1])  # √  列表式的索引
print(ser_1['numpy']) # √
print(ser_1.pandas) # √  pandas的独特方法，直接点索引
"""


# 接下来是多个索引的使用
# 首先是 点
print(ser_1.numpy,ser_1.pandas)  # 100 120

print((ser_1.numpy,ser_1.pandas))  # (np.int64(100), np.int64(120))  <class 'tuple'>
# 这个就凸显了，pandas这个库是依赖numpy库，所以在输出的时候会显示np这个前缀。
print([ser_1.numpy,ser_1.pandas])  # [np.int64(100), np.int64(120)]  <class 'list'>
print({ser_1.numpy,ser_1.pandas})  # {np.int64(120), np.int64(100)}  <class 'set'>

# 然后测试中括号
print(ser_1[1],ser_1['numpy']) # 150 100
print(ser_1[[1,'numpy']])
""""
1        150
numpy    100
dtype: int64
"""
print(type(ser_1[[1,'numpy']]))  # <class 'pandas.core.series.Series'>


# 另外一种使用显示索引的方法
print("--" * 15)
index_1 = ser_1.loc["numpy"]
index_2 = ser_1.loc[["numpy",'pandas',1]]
index_3 = ser_1.loc[["numpy"]]

print(index_1) # 100
print(index_2)
"""
numpy     100
pandas    120
1         150
dtype: int64
"""
print(index_3)
"""
numpy    100
dtype: int64
"""