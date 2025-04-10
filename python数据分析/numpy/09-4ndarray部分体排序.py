# 2.部分排序np.partition(a,k)
# 有的时候我们不是对全部数据感兴趣，我们可能只对最小或最大的一部分感兴趣。
# ·当k为正时，我们想要得到最小的k个数
# ·当k为负时，我们想要得到最大的k个数
import numpy as  np
data = np.random.permutation(100)
aaa = np.partition(data,4)[:4]
print(aaa)  # [0 1 2 3]
bbb = np.partition(data,-4)[-4:]
print(bbb)  # [96 97 98 99]
"""
但是你如果使用partition这个方法指定的数值小于切片长度，
那么超出长度的部分，正确性是没有保证的
"""