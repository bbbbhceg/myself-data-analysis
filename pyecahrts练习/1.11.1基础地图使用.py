"""
地图可视化的基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import  VisualMapOpts

# 准备地图对象
map = Map()
# 准备数据
data = [
    ("北京市",99),
    ("上海市",199),
    ("湖南省",299),
    ("台湾省",399),
    ("广东省",499),
    ("山东省",4199),
    ("辽宁",4199)
]
# 添加数据
map.add("测试地图",data,"china")
# 通过全局配置，将地图的颜色加入
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9人","color":"#CCFFFF"},
            {"min":10,"max":99,"label":"10-99人","color":"#FFFF99"},
            {"min":100,"max":499,"label":"100-499人","color":"#FF9966"},
            {"min":500,"max":999,"label":"500-999人","color":"#FF6666"},
            {"min":1000,"max":4999,"label":"1000-4999人","color":"#CC3333"},
            {"min":5000,"label":"1000以上","color":"#990033"}
        ]
    )
)
# 绘图
map.render()


