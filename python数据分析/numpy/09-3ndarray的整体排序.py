#  1.快速排序
# np.sort()与ndarray.sort()都可以:
# 但有区别︰
# - np.sort()不改变输入
# - ndarray.sort()本地处理，不占用空间，但改变输入
import  numpy as np
data = np.random.permutation(10)
print("data原数据：",data)
# data原数据： [5 9 8 3 0 4 2 1 6 7]


bbb = np.sort(data)
print("np.sort()后的数据:",bbb)
print("np.sort()后的原数据:",data)
# np.sort()后的数据: [0 1 2 3 4 5 6 7 8 9]
# np.sort()后的原数据: [5 9 8 3 0 4 2 1 6 7]

aaa = data.sort()
print("数组.sort（）后的数据:",aaa)
print("数组.sort（）后的原数据:",data)
# 数组.sort（）后的数据: None。因为改变发生在原数据处
# 数组.sort（）后的原数据: [0 1 2 3 4 5 6 7 8 9]
