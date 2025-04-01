# 常见的生成固定范围数组的方法一共有两种

# 1.linespace()
import numpy as np
data_1 = np.linspace(0,15,3)
print(data_1)
"""
[ 0.   7.5 15. ]
"""

# 2.arange()
data_2 = np.arange(0,15,2)
print(data_2)
"""
[ 0  2  4  6  8 10 12 14]
"""