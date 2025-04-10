# 广播机制
# 主要是为了解决之前提到的，为什么高维数组可以和一个零维的数进行数学运算。
# 【重要】ndarray广播机制的两条规则、
# ·规则一：为缺失的维度补1
# ·规则二：假定缺失元素用已有值填充
# 例1 : m= np.ones((2,3))                a = np.arange(3)求m+a
# 例2: a = np.arange(3).reshape((3,1))   b = np.arange(3)求a+b
# 习题a = np.ones((4,1)) b = np.arange(4)求a+b

#  例子1
import numpy as np
m= np.ones((2,3))
a = np.arange(3) # 012
sum1 = m + a
# 此处就是一维数组和二维数组的计算，运用广播机制，
print(sum1) # 输出检测，证明OK。
"""
[[1. 2. 3.]
 [1. 2. 3.]]
"""

# 例子2
aa = np.arange(3).reshape((3,1))
bb = np.arange(3)
print("aa + bb:",(aa + bb))
"""
最后这个形状是因为两个数组都进行广播机制的补全
[[0 1 2]
 [1 2 3]
 [2 3 4]]
"""

# 练习题
aaa = np.ones((4,1))
bbb = np.arange(4)
print("aaa + bbb:",aaa + bbb)
"""
[[1. 2. 3. 4.]
 [1. 2. 3. 4.]
 [1. 2. 3. 4.]
 [1. 2. 3. 4.]]
"""

# 不能广播的例子。虽然numpy不能解决这个问题，但是pandas是可以进行解决的。
x =np. ones(shape=(3,3))
y =np.array ([[1,2],[3,1]])
# print(x + y)  # ValueError: operands could not be broadcast together with shapes (3,3) (2,2)


