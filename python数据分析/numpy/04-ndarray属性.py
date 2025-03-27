# 五个常用属性
import numpy as np
score =([
  [80,89,86,67,79],
  [78,97,89,67,81],
  [90,94,78,67,74],
  [91,91,90,67,69],
  [76,87,75,67,86],
  [70,79,84,67,84],
  [94,92,93,67,64],
  [86,85,83,67,80]])

score = np.array(score)
# print(type(score))  # 输出检测表明，已经是<class 'numpy.ndarray'>

# numpy.shape 显示目标数组的形状，数据类型为元组
print(score.shape)  # (8, 5)
print(type(score.shape)) # <class 'tuple'>

# numpy.ndim  用来显示目标数组的维度数
print(score.ndim)  # 2

# numpy.size  用来显示数组中的元素数量
print(score.size)  # 40

# numpy.dtype  用来显示数组元素的类型
print(score.dtype)  # int64

# numpy.itemsize 用来显示一个数组
print(score.itemsize)   # 8
"""
在 NumPy 中，itemsize 属性表示数组中每个元素所占的字节数。
对于整数类型 int64，每个元素占用 8 个字节，因此 score.itemsize 的值为 8。
"""