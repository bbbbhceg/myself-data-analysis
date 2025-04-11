# np.sort():不改变原数组
# ndarray.sort() :改变原数组,不多占内存空间
import numpy as np

a = np.random.randint(1,10,size=(2,3))
print(a)
"""
[[3 3 8]
 [1 3 5]]
"""
# print(np.sort(a))
"""
[[3 3 8]
 [1 3 5]]
"""
print(a.sort())  # None
print(a)
"""
[[3 3 8]
 [1 3 5]]
"""