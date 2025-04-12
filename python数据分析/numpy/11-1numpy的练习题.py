# 1、创建一个长度为10的一维全为int0的ndarray对象，然后让第5个元素等于1
# 2、创建一个元素为从10到49的ndarray对象
# 3、将第2题的所有元素位置反转
# 4、使用np.random.random创建一个10*10的ndarray对象，并打印出最大最小元素
# 5、创建一个10*10的ndarray对象，且矩阵边界全为1，里面全为0
# 6、创建一个每一行都是从0到4的5*5的矩阵
# 7、创建一个范围在(0,1)之间的长度为12的等差数列
# 8、创建一个长度为10的随机数组并排序
# 9、创建一个长度为10的随机数组并将最大值替换为0

import numpy

# 1、创建一个长度为10的一维全为int0的ndarray对象，然后让第5个元素等于1
"""
arr_1 = numpy.zeros(shape=(10,),dtype=int)
arr_1[4] = 1
# print(arr_1) # 输出检测
"""

# 2、创建一个元素为从10到49的ndarray对象
"""
arr_2 = numpy.arange(10,50)
# print(arr_2) # 输出检测
"""

# 3、将第2题的所有元素位置反转
"""
arr_3 = arr_2.copy()
arr_3 = arr_3[::-1]
# print(arr_3) # 输出检测
"""


# 4、使用np.random.random创建一个10*10的ndarray对象，并打印出最大最小元素
"""
arr_4 = numpy.random.randint(1,10,size = (10,10))
print(arr_4.max())
print(arr_4.argmax())
print(arr_4.min())
print(arr_4.argmin())
"""

# 5、创建一个10*10的ndarray对象，且矩阵边界全为1，里面全为0
"""
arr_5 = numpy.zeros(shape=((10,10)))
arr_5[[0,-1]] = 1
arr_5[:,[0,-1]] = 1
print(arr_5)
# 或者使用切片索引控制中间
"""

# 6、创建一个每一行都是从0到4的5*5的矩阵
""""
arr_6_0 = numpy.ones([5,5])
arr_6_1 = numpy.arange(0,5,dtype=int)
arr_6 = arr_6_1 * arr_6_0
print(arr_6)
# 或者1：a =  arr_6_1 * 5
# 或者2：l = [0,1,2,3,4]
#  n= np.array(I*5).reshape(([5.5))
"""

# 7、创建一个范围在(0,1)之间的长度为12的等差数列
"""
arr_7 = numpy.linspace(0,1,12)
print(arr_7)
print(len((arr_7)))
"""

# 8、创建一个长度为10的随机数组并排序
"""
arr_8 = numpy.random.randint(1,5,size=(10,))
arr_8.sort()
print(arr_8)
print(len(arr_8))

"""

# 9、创建一个长度为10的随机数组并将最大值替换为0
arr_9 = numpy.random.randint(1,5,size=(10,))
print(arr_9)
print(len(arr_9))
arr_9[arr_9.argmax()] = 0
print(arr_9)