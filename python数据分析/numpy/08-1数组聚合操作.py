# 求和np.sum
import numpy

arr_1 = numpy.random.randint(0,10,size=10)

# 求累加和
sum_arr_1 = arr_1.sum()
print("求累加和:",sum_arr_1)  # 会直接出现是个数值的累加和
# 求多维数组的累加和，但是axis= 0  or 1
arr_56 = numpy.random.randint(1,11,size = (2,3))
print("多维数组",arr_56)
print("多维数组求和",arr_56.sum())
print("多维数组的累加和，但是axis= 0",arr_56.sum(axis=0))
print("多维数组的累加和，但是axis= 1",arr_56.sum(axis=1))



# 求平均值方法1
mean_arr_1 = arr_1.mean()
print("求平均值:",mean_arr_1)
# 求均值方法2
avera_arr = numpy.average(arr_1)
print("average方法求的平均值：",avera_arr)
"""
这个average方法，之所以一定要在numpy下，是因为它的用法更为复杂。
例如他可以进行权重的赋值
arr = np.array([1, 2, 3, 4, 5])
weights = np.array([1, 1, 1, 1, 1])  # 均匀权重
print(np.average(arr, weights=weights))  # 输出：3.0

weights = np.array([1, 2, 3, 4, 5])  # 不均匀权重
print(np.average(arr, weights=weights))  # 输出：3.6666666666666665
"""

# 求最大值
max_arr_1 = arr_1.max()
print("求最大值:",max_arr_1)

# 求最小值
min_arr_1 = arr_1.min()
print("求最小值:",min_arr_1)

# 求最大值索引
arg_max = arr_1.argmax()
print("求最大值索引:",arg_max)

# 求最小值索引
arg_min = arr_1.argmin()
print("求最小值索引:",arg_min)

# 求标准方差  （方差开根号）
std_arr = arr_1.std()
print("标准方差:",std_arr)

# 求方差(每个数据点距离平均值的平方（平方消除符号）的累加和，然后再除去总数据量，)
var_arr = arr_1.var()   # Variance的缩写
print("方差:",var_arr)

"""
然后就是比较特殊的中位数，因为其需要先排序。
"""
med_arr = numpy.median(arr_1)
print("中位数是：",med_arr)

# 其余测操作
# 求四分位数，和median一样是需要调用numpy.对应关键字（）然后括号内传入数据，列表内可以定制
data = numpy.arange(1,11,step = 1)
percet_data = numpy.percentile(data,[0.25,0.5,0.75])
print("数据的四分位数值",percet_data)


# 数组的次方。结果是将每一个元素进行次方运算
aaaaaa = numpy.power(arr_1,3)  # 三次方
#  或者这样也可以 arr_1 **3
print(aaaaaa)
