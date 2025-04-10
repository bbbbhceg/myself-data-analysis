import  numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[1,1],[2,2]])
c = a * b
print(c)
"""
这样的数组运算是对应位置的计算，而不是矩阵的那种运算
[[1 2]
 [6 8]]
"""

# 矩阵运算
# 需要借助一个特定关键词
d = np.dot(a,b)
print(d)
"""
[[ 5  5]
 [11 11]]
"""