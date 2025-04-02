import numpy
from pyecharts.charts import  Bar
from pyecharts.options import *

data1 = numpy.random.normal(loc=1.75,scale=0.2,size=1000)
data1 = list(data1)
data1 = sorted(data1)
data_x = []
for x in range(0,1000):
    data_x.append(x)

bar = Bar()
bar.add_xaxis(data1)
bar.add_yaxis("正态分布",data1,label_opts=LabelOpts(is_show=False))


bar.render("正态分布直方图.html")