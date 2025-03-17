"""
山东疫情地图绘制
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据
f= open("D:\Program Files\黑马第十章练习数据\地图数据\疫情.txt","r",encoding="utf-8")
china_data = f.read()
f.close()

# 将读取的json格式数据，转换成Python格式数据
china_data = json.loads(china_data)

# 取出山东各个城市的总体数据
sd_cities_data_list = china_data["areaTree"][0]["children"][11]["children"]
# print(sd_cities_data_list)   # 进行输出检测

# 使用for循环将城市名称进行补全
# 先循环，取各个城市整体的数据
# 第一层共循环15次，剔除0元素的总体数据
data_list = []
for city_data in sd_cities_data_list[1:]:
    # 再在城市字典数据中匹配name变量
    city_name = city_data["name"] + "市"
# print(sd_city_data_list)  输出检测
    city_confirm = city_data["total"]["confirm"]
    # 向目标列表填入元组数据，数据是城市名称和确诊数据
    data_list.append((city_name,city_confirm))
# print(data_list)  输出检测

"""
手动添加莱芜和东营两个城市的数据
"""
# 这顺便复习了一下，列表的append方法，一次只能追加一个数据
data_list.append(("莱芜市",38))
data_list.append(("东营市",30))

# 建立地图对象,括号非常容易忘
map =Map()
# 添加数据
map.add("山东省疫情分布",data_list,"山东")
# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="山东省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 499, "label": "100-499人", "color": "#FFFF99"},
            {"min": 500, "max": 999, "label": "500-999人", "color": "#FF9966"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF6666"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#CC3333"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+", "color": "#990033"},
        ]
    )
)
# 但是数据缺少莱芜和东营的数据，莱芜是已经并到济南了。东营是真没有数据
# 但是为了地图的美观，直接自己根据周围地市假设数据，并添加于构建地图之前

#绘图
map.render("山东省疫情地图.html")







