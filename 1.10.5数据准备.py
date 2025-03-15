# 这个文件内，主要是演示数据准备

import json
# 打开数据赋予变量文件_美国
f_us = open("D:\Program Files\黑马第十章练习数据\折线图数据\美国.txt",'r',encoding='utf-8')
# 读取全部内容，赋值给us_data，类型为str
us_data = f_us.read()

# 将文本内的内容，修正成标准json格式
# 用字符串的replace方法，将开头进行替换操作，达到删除的目的
us_data = us_data.replace('jsonp_1629344292311_69436(','')

#  用切片操作，将末尾进行修正
# 这里不使用replace，是因为replace会进行整体的匹配
# 开头那个非常地独特，内容内没有重复，但是结尾的）;可就不一样了。
# 所以，以求谨慎，就选用切片操作。
us_data = us_data[:-2]

# 使用json将完全符合json格式的数据，更改成python的字典格式
us_dict = json.loads(us_data)
print(type(us_dict))   # 检测格式是否是字典

# 然后，我需要将已经转成python字典格式的，文件对象内容中的trend整体取出
trend_data = us_dict['data'][0]['trend']
# print(type(trend_data))
print('python字典格式\n',trend_data)
a = json.dumps(trend_data)
print('json格式\n',a)
# 将26行输出的数据替换到bejson的网站中，这样可以简化层级
