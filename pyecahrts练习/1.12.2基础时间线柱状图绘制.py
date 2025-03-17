from pyecharts.charts import  Bar,Timeline
from pyecharts.options import  *
from pyecharts.globals import ThemeType
# 构建柱状图对象
bar1 = Bar()

# 添加x，y轴数据,并进行反转
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[40,30,20],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[50,38,25],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 创建时间线对象,以及别忘记括号
timeline = Timeline(
    {"theme":ThemeType.ROMA}
)
# 在时间线内添加柱状图对象
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")
# 绘图是用时间线对象进行绘图，而不是单纯的bar对象

# 但是，截止到现在，如果直接render绘图，出现的图表是静态的，不是自动播放的。
# 如果需要自动播放，就需要调用timeline.add_schema()
timeline.add_schema(
    play_interval=1000,     # 自动播放的时间间隔，单位是毫秒1000毫秒=1秒
    is_timeline_show=True,  # 是否在自动播放的时候，显示时间线。    默认是True
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True,      # 是否循环自动播放   ， 默认是True
)

timeline.render("基础时间线柱状图.html")







