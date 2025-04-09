# 广播机制
# 【重要】ndarray广播机制的两条规则、
# ·规则一：为缺失的维度补1
# ·规则二：假定缺失元素用已有值填充
# 例1 : m= np.ones((2,3))                a = np.arange(3)求+a
# 例2: a = np.arange(3).reshape((3,1))   b = np.arange(3)求a+b
# 习题a = np.ones((4,1)) b = np.arange(4)求a+b
import numpy