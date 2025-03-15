#导包，导入Line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts
#得到一个空折线图对象，我将其并命名为line_1
line_1 = Line()
#添加x轴数据
line_1.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
line_1.add_yaxis("GDP",[30,20,10])
# 全局配置的标题设置 pos_left="center",pos_bottom="1%"
# 这些都是距离左边，和距离底部多远
line_1.set_global_opts(
    title_opts=TitleOpts(title='GDP展示',pos_left="center",pos_bottom="1%")
)
# 生成图表
line_1.render()




