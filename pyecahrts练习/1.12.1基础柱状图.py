"""
基础柱状图
"""
from pyecharts.charts import  Bar
from pyecharts.options import  *

# 构建柱状图对象
bar = Bar()

# 修改x轴数据
bar.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))

# 反转对象
bar.reversal_axis()

# 绘制图表
bar.render("基础柱状图.html")


