# 级联的学习
import numpy as np

array1 = np.random.randint(0,10,size=(6,3))
array2 = np.random.randint(10,20,size=(3,3))
# print(array1)
"""
形状如此
[[0 7 3]
 [9 1 7]
 [9 4 0]]
"""
# print(array2)
"""
形状如此
[[19 11 16]
 [16 11 10]
 [10 11 19]]
"""
con = np.concatenate((array1,array2))    # 参数格式是元组
# con = np.concatenate([array1,array2])  # 参数格式是列表
print(con)



"""
# 级联方式2
stack2 = np.vstack((array1,array2))  # 数组展开形式的垂直纵向级联  也就是等同于方式1的 axis是0(默认值)的情况
stack1 = np.hstack((array1,array2))  # 数组展开形式的水平横向级联  也就是等同于方式1的 axis是1的情况
"""

