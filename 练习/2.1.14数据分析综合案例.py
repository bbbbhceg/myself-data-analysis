# 有2份数据文件，现需要对其进行分析处理，计算每日的销售额并以柱状图表的形式进行展示
# 第一,先将二月份的数据进行数据清洗
import json

from  pyecharts.charts import Bar
from  pyecharts.options import LabelOpts, AxisOpts, InitOpts, TitleOpts
from  pyecharts.globals import *


# 打开文件对象
f = open(r"D:\Program Files\黑马练习数据\2011年2月销售数据JSON.txt","r",encoding="utf-8")
# 读取文件对象的内容
data = f.readlines()
f.close()
# print(data) # 输出检测为列表格式的数据，元素为带有\n的字符串格式，共978条
# 我将循环读取，然后进行sorted
data_list = []
for x in data:
    x = x.strip()
    data_list.append(x)
# print(data_list)  # 输出检测表明，每个元素中的\n已经删除
# 接下来，需要将列表中的字符串格式，还原为字典格式
"""
经过观察发现，虽然data_list整体不符合json格式，但是其中的每一个元素都是符合json格式的字符串
所以决定使用for循环的方法将其中的元素一一还原成为字典格式
"""
# 首先遍历 data_list 列表中的每个元素
data_list_dict = []
for item in data_list:
    # 使用 json.loads() 将遍历进来的， JSON 格式的字符串item解析为python字典,并赋予变量 dict_item
    dict_item = json.loads(item)
    # 将解析后的字典添加到 dict_list 列表中
    data_list_dict.append(dict_item)

# print(data_list_dict) # 输出检测，是达到预期结果的
# [{'date': '2011-02-01', 'order_id': 'caf99222-53d6-427b-925d-3187fc71a86a', 'money': 1805, 'province': '江西省'}, {'date': '2011-02-01', 'order_id': '3dea6f83-a9b2-4197-ba9f-2b25704c530b', 'money': 2547, 'province': '广东省'}]
# aaa = json.dumps(data_list_dict)  # 转化为json格式，然后再网站中查看是正确格式
# print(aaa)

# 然后就是数据准备
# x轴要求是列表格式，元素为字符串的日期，y轴要求是列表格式，元素是数值。
x_data = []
y_data = []
# 第一层循环取到字典元素
for a in data_list_dict:
    # 第二层循环取到字典的元素
    b=a["date"]
    x_data.append(b)
# print(x_data.count('2011-02-11'))  # 经过测试，每日每个地方贡献销售额的数量不一致，可能存在一个省多次贡献
x_data = set(x_data)
x_data = sorted(list(x_data))
# print(x_data) # 输出检测，已经没有重复，且从左到右，从小到大的排列了 日期是2.1到2.28,长度是28

# y轴要求的数据是列表格式，元素是整数型，数据是该公司每日的销售总额
date_money = {}

for i in data_list_dict:
    date = i["date"]
    money = i["money"]
    # 如果日期存在于字典之中，就进行金额累加，否则，就视为新的日期，进行初始化金额
    if date in date_money:
        date_money[date] += money
    else:
        date_money[date] = money
# print(date_money)   # 结果：{'2011-02-01': 50241, '2011-02-02': 94426, '2011-02-03': 102784, '2011-02-04': 53034, '2011-02-05': 61597, '2011-02-06': 52711, '2011-02-07': 42777, '2011-02-08': 49396, '2011-02-09': 46977, '2011-02-10': 46224, '2011-02-11': 50699, '2011-02-12': 51962, '2011-02-13': 52717, '2011-02-14': 49266, '2011-02-15': 44201, '2011-02-16': 53097, '2011-02-17': 60878, '2011-02-18': 51653, '2011-02-19': 47383, '2011-02-20': 46295, '2011-02-21': 54194, '2011-02-22': 41492, '2011-02-23': 52743, '2011-02-24': 55043, '2011-02-25': 49319, '2011-02-26': 53441, '2011-02-27': 51796, '2011-02-28': 48385}
y_data = list(date_money.values()) # 将每日的销售额数据赋予x_data
# print(y_data) # 输出检测，是符合预期的

"""
第一大阶段准备完毕，开始进行，创建图标对象，添加数据，全局or系列配置
"""
# 创建柱状图表对象
bar = Bar(init_opts=InitOpts(theme=ThemeType.DARK))
# 添加两轴数据
bar.add_xaxis(x_data)
bar.add_yaxis("销售额",y_data,label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额"), # 标题设置
xaxis_opts=AxisOpts(axislabel_opts=LabelOpts(rotate=-45))  # 设置x轴坐标旋转
)

# 绘制图表
bar.render("每日销售额.html")