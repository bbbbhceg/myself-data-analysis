# 创建数组的训练
import numpy
"""
list_a = [1,22,333,4444]
list_b = [1,2,3,4,5]
list_c = [1,2,3,4,5,"aaaaaa"]

arr_1 = numpy.array(list_a)
arr_2 = numpy.array(list_b)
arr_3 = numpy.array(list_c)

print(arr_1)       # [   1   22  333 4444]
print(arr_2)       # [1 2 3 4 5]
print(arr_3)       # ['1' '2' '3' '4' '5' 'aaaaaa']
# 经过观察,列表转数组，会丢弃掉
print(type(arr_1)) # <class 'numpy.ndarray'>
print(len(arr_1))  # 4

"""
# 1.生成0和1的数组进行占位
# 我将生成一个(3,4)形状的二维数组
array_1 = numpy.zeros(shape=(3,4))
print(array_1)
print(array_1.dtype)


ar1 = numpy.ones(shape = (3,3),dtype = numpy.int8)
"""
np.ones(shape, dtype=None, order='℃')  float64类型

shape = (m, n) # m行n列二维数组
shape = (m)    # m个元素的一维数组  [1,2,3]
shape = (m,)   # m个元素的维数组

shape = (m,1)  # m行1列 二维数组   [[1],[2],[:3]]
shapc = (1, n) # 1行m列二维数组    [[1,2,3]]
"""

"""
[
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]
 ]
float64
"""
array_2 = numpy.ones(shape = (4,5))
print("array_2:\n",array_2)
print(array_1.dtype)
"""
array_2:
 [[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
float64
"""

# full方法
ar111 = numpy.full(shape=(3,3),fill_value= 6)
print(ar111)
"""
[[6 6 6]
 [6 6 6]
 [6 6 6]]
"""


# 生成单位矩阵数组
ar123 = numpy.eye(N = 5)
print(ar123)
"""
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
"""