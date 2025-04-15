import numpy as np
import pandas

# 1.创建series的方法
# 由列表创建
list_1 = [1,22,333,4444]
s_1 = pandas.Series(list_1)  # 注意格式，注意大小写
print(s_1)
"""
0       1
1      22
2     333
3    4444
dtype: int64
"""

# 由数组创建
arr_1 = np.array(list_1)
s_2 = pandas.Series(arr_1)
print(s_2)

"""
0       1
1      22
2     333
3    4444
dtype: int64
"""

# 分别查看series的索引（series）和值（values）
print(s_1.index)   # RangeIndex(start=0, stop=4, step=1)
# 如果觉得上边这个，输出索引的方式不直观，还可以如下一样
print(list(s_1.index))  # [0, 1, 2, 3]

print(s_1.values)  # [   1   22  333 4444]


# 修改索引index
s_1.index = ['b','c','d','e']
s_2.index = list('BCDE')
print(s_1)
"""
b       1
c      22
d     333
e    4444
dtype: int64
"""
print(s_2)
"""
B       1
C      22
D     333
E    4444
dtype: int64
"""

# 索引的使用方法---直接  点   大小写敏感
# 通过索引获取值
a = s_1.d
b = s_1.c,s_1.d     #  第一次见这样的方式。
c = s_1['e']     # 数字索引也是可以的
print(a) # 333
print(b) # (np.int64(22), np.int64(333))
print(c) # 4444

# 通过索引修改值
s_1.e = 213
print(s_1)


# -----------------------------
# 由列表创建series

d = {
    'a':11,
    'b':22,
    'c':33,
    'd':44,
    'e':55
}
s_3 = pandas.Series(d)
print(s_3)
"""
a    11
b    22
c    33
d    44
e    55
dtype: int64
"""
f = {
    'aa':np.random.randint(0,10, size = (2, 3)),
    'bb':np.random.randint(0,10, size = (2, 3)),
    'cc':np.random.randint(0,10, size = (2, 3)),
    'dd':np.random.randint(0,10, size = (2, 3))
}
s_4 = pandas.Series(f)
print(s_4)
"""
aa    [[4, 0, 6], [0, 3, 5]]
bb    [[8, 4, 1], [1, 5, 3]]
cc    [[7, 6, 2], [8, 0, 4]]
dd    [[8, 2, 1], [7, 4, 9]]
dtype: object
"""

s_5 = pandas.Series([1,2,3], index=["鲁班","李白",'杜甫'],name="历史人物")
print(s_5)
"""
鲁班    1
李白    2
杜甫    3
Name: 历史人物, dtype: int64
"""