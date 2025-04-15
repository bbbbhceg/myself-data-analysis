# 记得测试完删除。
import pandas
import numpy as np
d = {
    'a':11,
    'b':22,
    'c':33,
    'd':44,
    'e':55
}
s_3 = pandas.Series(d)
print(s_3)

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


