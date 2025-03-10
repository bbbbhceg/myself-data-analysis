"""
# 我将先定义五个类型的数据容器，但是都是纯数字，字母和中文进行max和min的测试
list =[1,2,3,4,5]
tuple =(1,2,3,4,5)
str = "1,2,3,4,5"
set = {1,2,3,4,5}
dict = {1:1,2:2,3:3,4:4,5:5}  # 我连key也定义成数字
# 接下来进行max的测试
print("列表类型：",max(list))
print("元组类型：",max(tuple))
print("字符串类型：",max(str))
print("集合类型：",max(set))
print("字典类型：",max(dict))
# 不出意外的都输出5，那么min也不用测试了
"""
"""
# 我将把上一个测试全注释，进行如果全是字母的max的测试
list =["a","b","c","d","e"]
tuple =("a","b","c","d","e")
str = "abcde"
set = {"a","b","c","d","e"}
dict = {"a":"a","b":"b","c":"c","d":"d","e":"e"}
# 接下来进行max的测试
print("列表类型：",max(list))
print("元组类型：",max(tuple))
print("字符串类型：",max(str))
print("集合类型：",max(set))
print("字典类型：",max(dict))
# 不出意外的，全部输出e，那么min也不用测试了
"""

# 接下来我将测试，前三位3是数字，后两位是字母
# 这样的话，在测试max的时候，如果是字母直接视为对应26字母的位置，将直接显现出来
list =[1,2,3,"d","e"]
tuple =(1,2,3,"d","e")
str = '1,2,3,"d","e"'
set = {1,2,3,"d","e"}
# dict = {"a":1,"b":2,"c":3,"d":"d","e":"e"}
# 接下来进行max的测试
print("列表类型：",max(list))
print("元组类型：",max(tuple))
print("字符串类型：",max(str))
print("集合类型：",max(set))
# print("字典类型：",max(dict))