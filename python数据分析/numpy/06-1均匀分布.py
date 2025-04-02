# 实际上是创建数组的05-4生成随机数组，但是因为可以指定分布状态所以产生了这一文件名称
# 这个文件主要用于练习均匀分布

import numpy
from pyecharts.charts import  Bar
from pyecharts.options import *


data1 = numpy.random.uniform(low=0.0,high=10.0,size=100)
# print(type(data1))
data1 = list(data1)
data1 = sorted(data1)
# print(type(data1))
data_x = []
for x in range(0,100):
    data_x.append(x)

# print(len(data_x))

bar = Bar()
bar.add_xaxis(data1)
bar.add_yaxis("随机数",data1,label_opts=LabelOpts(is_show=False))


bar.render("随机数直方图.html")