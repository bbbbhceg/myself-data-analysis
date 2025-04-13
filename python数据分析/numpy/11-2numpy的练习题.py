# 1、给定一个4维矩阵，如何得到最后两维的和?
# 2、给定数组[1,2，3,4,5]，如何得到在这个数组的每个元素之间插入3个0后的新数组?
# 3、给定一个二维矩阵，如何交换其中两行的元素?
# 4、创建一个100000长度的随机数组，使用两种方法对其求三次方，并比较所用时间
# 5、创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积
# 6、矩阵的每一行的元素都减去该行的平均值
# 7、打印出以下矩阵(要求使用np.zeros创建8*8的矩阵):
# 8、正则化一个5*5随机矩阵
# 正则的概念:假设a是矩阵中的一个元素,max/min分别是矩阵元素的最大最小值，则正则化后a= (a - min)/(max - min)

import numpy
# 1、给定一个4维矩阵，如何得到最后两维度的和?
"""
arr_1 = numpy.random.randint(1,10,size=(2,3,4,5))
sum_1 = arr_1.sum(axis=(2,3))
print(sum_1)
# 第1个维度是axis=0
# 第2个维度是axis=1
# 第3个维度是axis=2
# 第4个维度是axis=3
"""


# 2、给定数组[1,2,3,4,5]，如何得到在这个数组的每个元素之间插入3个0后的新数组?
"""
arr_2 = numpy.array([1,2,3,4,5])
# 这个事情我本来想列表化之后，再通过循环完成。但是教学有更简单的方法。
arr_2_0 = numpy.zeros(20,dtype=int)
arr_2_0[::4] = arr_2
print(arr_2_0)
"""

# 3、给定一个二维矩阵，如何交换其中两行的元素?例如1,3行
"""
arr_3 = numpy.random.randint(1,6,size=(5,4))
print(arr_3)
arr_3_1 = numpy.copy(arr_3[0])
arr_3_3 = numpy.copy(arr_3[2])
arr_3[0] = arr_3_3
arr_3[2] = arr_3_1
print(arr_3)
# 更为简单的方法是利用索引直接交换.而不是费劲巴啦的覆盖。
# arr_3 = arr_3[[2,1,0,3,4]]
"""


# 4、创建一个100000长度的随机数组，使用两种方法对其求三次方，并比较所用时间
# 因为计算时间的关键字好像有点问题就在此，只是展示三次方的方案。
"""
arr_4 = numpy.random.randint(1,11,size=100)
numpy.power(arr_4,3)

arr_4 ** 3
"""

# 5、创建一个5*3随机矩阵和一个3*2随机矩阵，求矩阵积
"""
n1 = numpy.random.randint(0,100,size=(5,3))
n2 = numpy.random.randint(0,100, size=(3,2))
aaaa = numpy.dot(n1, n2)
print(aaaa)
"""

# 6、矩阵的每一行的元素都减去该行的平均值
"""
arr_6_0 = numpy.random.randint(0,10, size=(3,4))
arr_6_1 = numpy.mean(axis= 1).reshape(3,1)
print(arr_6_0 - arr_6_1)
"""


# 7、打印出以下矩阵(要求使用np.zeros创建8*8的矩阵):
"""
[[0 1 0 1 0 1 0 1]
 [0 0 1 0 0 0 0 0]
 [0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0]
 [0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0]
 [0 1 0 1 0 1 0 1]
 [0 0 0 0 0 0 0 0]]
"""
"""
arr_7= numpy.zeros((8,8), dtype=int)
arr_7[::2,1::2]=1
arr_7[1:2,2]=1
print(arr_7)
"""

# 8、正则化一个5*5随机矩阵
arr_8 = numpy.random.randint(0,100,size=(5, 5))
min1 = arr_8.min()
max1 = arr_8.max()
bbbb = (arr_8 - min1)/ (max1 - min1)
print(bbbb)
