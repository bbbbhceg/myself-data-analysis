# 主要进行隐式索引的测试
# 所谓隐式索引，就是使用数字下标
# 使用整数作为索引值
# 使用iloc[](推荐)
import numpy
import pandas

list_1 = [0,1,2,3,4]
ser_1 = pandas.Series(list_1)
ser_2 = pandas.Series({'aa':150,"numpy":100,"pandas":120})
# print(ser_2[2])
"""
正常输出了结果120，但是报错了
报错：D:\Program Files\PyCharm Community Edition 2024.3.3\pythonlianxicunfangchu\python数据分析\pandas\001-pandas的综合测试处.py:8: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
  print(ser_2[2])

为什么会出现警告？
警告是 FutureWarning，表示你使用的代码行为在未来版本的 pandas 中可能会被修改或弃用。
警告的核心是：pandas.Series.__getitem__ 的行为将从“同时支持标签和位置索引”改为“仅支持标签索引”。
在未来的版本中，ser_2[2] 将不再被解释为位置索引，而是严格按照标签索引来处理。如果标签 2 不存在，代码将直接报错。
"""
# 所以为了避免这个报错和输出结果同时出现的情况，才使用iloc【num】.(index location)

print(ser_2.iloc[2])  # 这样就不会报错，又能正常输出结果了
print(ser_2.iloc[[2,0]])  # 输出结果如下
"""
pandas    120
aa        150
dtype: int64
"""
print(ser_2[['pandas','aa']])  # 输出结果如上
