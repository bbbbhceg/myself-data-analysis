# 这个文件内，主要是演示数据准备

import json
from  pyecharts.charts import Line
from  pyecharts.options import TitleOpts,LabelOpts
# 打开数据赋予变量文件_美国
f_us = open("D:\Program Files\黑马第十章练习数据\折线图数据\美国.txt",'r',encoding='utf-8')
us_data = f_us.read()   # 读取全部内容，赋值给us_data，类型为str

# 打开数据赋予变量文件_日本
f_jp = open("D:\Program Files\黑马第十章练习数据\折线图数据\日本.txt",'r',encoding='utf-8')
jp_data = f_jp.read()   # 读取全部内容，赋值给jp_data，类型为str

# 打开数据赋予变量文件_印度
f_in = open("D:\Program Files\黑马第十章练习数据\折线图数据\印度.txt",'r',encoding='utf-8')
in_data = f_in.read()   # 读取全部内容，赋值给in_data，类型为str


# 将文本内的内容，修正成标准json格式
# 用字符串的replace方法，将开头进行替换操作，达到删除的目的
us_data = us_data.replace('jsonp_1629344292311_69436(','')
jp_data = jp_data.replace('jsonp_1629350871167_29498(','')
in_data = in_data.replace('jsonp_1629350745930_63180(','')

#  用切片操作，将末尾进行修正
# 这里不使用replace，是因为replace会进行整体的匹配
# 开头那个非常地独特，内容内没有重复，但是结尾的）;可就不一样了。
# 所以，以求谨慎，就选用切片操作。
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# 使用json将完全符合json格式的数据，更改成python的字典格式
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# print(type(us_dict))   # 检测格式是否是字典

# 然后，我需要将已经转成python字典格式的，文件对象内容中的trend整体取出,赋值给trend_data
# 这个trend字典中一共俩键值对，一个是名为updateDate的列表数据，一个是名为list的列表数据
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 将日期数据设置为x轴数据，从而备用
# 并只取第一年的数据,通过json视图发现，第一年的末尾的12.31日的下标是313
# 所以进行切片操作，将前314个元素切出
us_x_data =us_trend_data['updateDate'][:314]
jp_x_data =jp_trend_data['updateDate'][:314]
in_x_data =in_trend_data['updateDate'][:314]
# print(x_data)  输出检测是没问题的

# 将list数据设置为y轴数据，从而备用
# 因为x轴数据只有到下标313，所以，y轴的数据也需要进行切片
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]
# print(y_data)  输出检测是没问题的

# 生成图表,这个括号是必不可少的
line = Line()
# 获取x轴数据
# 又因为x轴日期是公用的，所以添加一份就可以
line.add_xaxis(us_x_data)

# y轴，添加三个国家的数据
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))
# ,label_opts=LabelOpts(is_show=False)这个的作用是控制折线上的是否显示数字

# 设置全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2022年美日印三国确诊人数对比折线图",pos_left="center",pos_bottom="1%")
)

# 调用render方法，生成图表
line.render()

# 因为最开始调用了文件读取，所以闲杂要关闭文件对象
# 刚才也突然忘记这个事情了，这也反应了with open() as f:的好用之处
f_us.close()
f_jp.close()
f_in.close()
