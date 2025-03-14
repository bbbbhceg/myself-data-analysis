# 导入json模块
import json

# 准备符合符合json格式要求的python数据
data = [{'name':'张三','age':18},{'name':'李四','age':55}]

# 通过 json.dumps(data) 方法把Python数据格式转化为了json数据格式
data = json.dumps(data)
print(type(data))  # <class 'str'>
print(data)
# [{"name": "\u5f20\u4e09", "age": 18}, {"name": "\u674e\u56db", "age": 55}]
# 这里中文会因为编码的问题，不会显示原文
# 如果你想正确展示中文，可以vdata = json.dumps(data,ensure_ascii=False)

#  通过json.dumps(data) 方法
#  把json数据转化为了python数据,也就是字典，或者嵌套字典的列表格式
data = json.loads(data)
print(type(data))     #<class 'list'>



