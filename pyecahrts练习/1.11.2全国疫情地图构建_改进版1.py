import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据
f = open("D:\Program Files\黑马第十章练习数据\地图数据\疫情.txt", "r", encoding="utf-8")
data = f.read()
f.close()

# 将JSON字符串转换为Python字典
data_dict = json.loads(data)

# 清洗，修补数据
# 定义直辖市列表municipalities(直辖市)
municipalities = ["北京", "上海", "天津", "重庆"]

# 定义自治区列表regions(行政区)
regions = ["广西壮族", "西藏", "宁夏回族", "新疆维吾尔", "内蒙古"]

# 遍历并修改名字
for province_data in data_dict["areaTree"][0]["children"]:   # 控制循环次数
    province_name = province_data["name"]    # 匹配字典的key并进行赋值

    # 如果是直辖市，直接在名字后加上"市"
    if province_name in municipalities:
        province_data["name"] = province_name + "市"
    # 如果是自治区，直接在名字后加上"自治区"
    elif province_name in regions:
        province_data["name"] = province_name + "自治区"
    # 如果是省，检查是否有"children"键
    elif "children" in province_data:
        province_data["name"] += "省"  # 在省名后加上"省"
        # 遍历省下的市
        for city_data in province_data["children"]:
            city_data["name"] += "市"  # 在市名后加上"市"


# 准备数据列表
data_list = []
for province_data in data_dict["areaTree"][0]["children"]:
    # 如果是省、自治区或直辖市，取对应的名字和确诊人数
    if "children" in province_data:
        province_name = province_data["name"]
        province_confirm = province_data["total"]["confirm"]
        data_list.append((province_name, province_confirm))
    else:
        # 如果是市，取市名和确诊人数
        city_name = province_data["name"]
        city_confirm = province_data["total"]["confirm"]
        data_list.append((city_name, city_confirm))

# 打印修改后的data_list，以验证是否正确
print(data_list)

# 创建地图对象并添加数据
map = Map()
map.add("各省份确诊人数", data_list, "china")

# 设置全局配置
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
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

# 渲染地图
map.render("全国疫情地图2.html")