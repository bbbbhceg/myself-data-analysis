# 求和np.sum
import numpy

arr_1 = numpy.random.randint(0,10,size=10)

# 求累加和
sum_arr_1 = arr_1.sum()
print("求累加和:",sum_arr_1)  # 会直接出现是个数值的累加和

# 求平均值
mean_arr_1 = arr_1.mean()
print("求平均值:",mean_arr_1)

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

