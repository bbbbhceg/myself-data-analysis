"""
全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据
f = open("D:\Program Files\黑马第十章练习数据\地图数据\疫情.txt","r",encoding="utf-8")
data = f.read()   # 读取全部数据，json是特殊格式的str
# 数据读取完毕，直接关闭文件占用
f.close()
# 读取各省数据
# 将特殊字符格式json格式，转换成python的字典格式
data_dict = json.loads(data)
# 从字典格式data_dict取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]
# 将省份的数据，更改成字典格式
data_list = []     # 绘图需要的数据列表
for province_data in province_data_list:
    province_name = province_data["name"]     # 省份名称
    province_confirm = province_data["total"]["confirm"]   # 确诊人数
    data_list.append((province_name,province_confirm))

# print(data_list) #可以输出检测一下
# 创建地图对象
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list,"china")
#  设置全局配置，定制分段的图例（视觉映射）
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99人","color":"#CCFFFF"},
            {"min":100,"max":499,"label":"100-499人","color":"#FFFF99"},
            {"min":500,"max":999,"label":"500-999人","color":"#FF9966"},
            {"min":1000,"max":4999,"label":"1000-4999人","color":"#FF6666"},
            {"min":5000,"max":9999,"label":"5000-9999人","color":"#CC3333"},
            {"min":10000,"max":99999,"label":"10000-99999人","color":"#CC3333"},
            {"min":100000,"label":"100000+","color":"#990033"}
        ]
    )
)
# 绘图
map.render("全国疫情地图1.html")


"""
反思：老师的教学版本，pyecharts的map还可以不识别是否加省和市以及自治区，但是现在时间的这个第三方包，就需要加上。
这个就导致，只是和教学一样的代码是没有办法实现同样效果的，就需要克服，如何进行省，市和自治区的匹配问题
我思考了一阵，还是尽量使用了代码的方式进行匹配，而不是使用手动改。
因为，这样会多有一种解决问题的思路。
详见1.11.2全国疫情地图构建_改进版，以及全国疫情地图2的展示效果。
"""