from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
f = open("D:\Program Files\黑马第十章练习数据\动态柱状图数据\\1960-2019全球GDP数据.csv","r",encoding="ansi")
# 这里的encoding应该写ansi，因为这个目标文件夹的编码格式是：ANSI。
# (记事本打开文件对象，并另存为，在临时对话框的下边就会显示编码格式)
data_lines =f.readlines()
# 这里使用readlines方法时因为，它会以行为单位生成列表，便于之后的pop操作
# 但是要警惕\n
f.close()

# 清洗数据
# 删除第一条不符合规格的数据
data_lines.pop(0)
# print(data_lines)  输出检测

# 将数据转换成为字典存储，格式为：
# {年份：[[国家，gdp],[国家，gdp]，......],年份：[[国家，gdp],[国家，gdp]，......],......}

# 定义一个字典对象
data_dict = {}
for line in data_lines:
    """
    data_lines的是使用readlines方法读取的成为的列表类型
    每一个元素是一行数据
    元素格式都为字符串，内容格式是：1960,澳大利亚,18577668271\n
    """
    year = int(line.split(",")[0])  # 年份
    country = line.split(",")[1]    # 国家
    gdp = float(line.split(",")[2]) # gdp数据,也可以转换科学计数法，且float之后会忽略\n
    # 如何判断字典里有没有指定的key呢？
    # 尝试将取出的三个元素添加进入提前定义好的字典对象中
    # 这个try的意识是key时year，value是一个列表，列表内容是[country,gdp]
    # 因为识别字典的元素，只能识别到key
    # 并且当key不存在于指定字典时，就视为增加元素的操作
    # 但是，经过测试，我发现：
    # 如果key不存在，且你只是写“list【key】”而不是写“list【key】=12”
    # 系统就不会将其识别为列表的增加操作，而是进行报错，报错的类型是：KeyError。
    # 在这个文件内就表现为被except捕获，然后对指定列表使用增加操作
    # 创建一个key，value是空列表。
    # 并顺手就将内容通过链式操作追加到value列表中，以符合绘图格式。
    # 紧接着依靠循环完成剩下的重复操作，就不过是，每次到新的年份，都会重复捕获操作。
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year]=[]
        data_dict[year].append([country,gdp])

# print(data_dict)  #输出检测

# 创建时间线对象，这里可以进行颜色的控制（记得导包）
timeline = Timeline({"theme":ThemeType.DARK})

# 排序年份，keys方法获得是列表格式，
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)  进行输出检测，确保年份数据的顺序是从小到大不是乱序的
# 进行for循环，每次获取一个年份
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element:element[1],reverse=True)    # 意思是对指定的年份的value进行sort排序
    # 取出本年份前15名的国家
    year_data = data_dict[year][0:15]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])    # x轴添加国家
        y_data.append(country_gdp[1]/100000000)    # y轴添加gdp数据,并除以1亿

    # 构建柱状图
    bar = Bar()
    x_data.reverse()   # x,y轴的数据本身进行同步顺序的反转
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP（亿）",y_data,label_opts=LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()

    # 设置每一年的图表标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前15GDP数据")
    )
    timeline.add(bar,str(year))

# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

# 绘图
timeline.render("1960-2019全球GDP前15国家.html")


"""
可以整体上分为两大步骤
39行之前是准备数据
39行之后是构建时间线对象
"""