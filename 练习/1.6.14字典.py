# 我将进行字典定义的练习，分别是。有元素字典，以及两种空字典的练习。
dict1 = {"元素1":100,"元素2":90,"元素3":80,"元素4":70,"元素5":60}
dict2 = {}
dict3 = dict()
print(f"字典1得内容是{dict1}，数据类型是{type(dict1)}")
print(f"字典2得内容是{dict3}，数据类型是{type(dict2)}")
print(f"字典3得内容是{dict3}，数据类型是{type(dict3)}")

# 尝试用字典类型，进行三位学生的三科成绩的查询
grade = {
            "小明":{"语文":77,"数学":66,"英语":33},
            "小红":{"语文":88,"数学":86,"英语":55},
            "李华":{"语文":99,"数学":96,"英语":66}
        }
keys = grade.keys()
keys2 = grade["小明"].keys()
print(f"字典的全部keys：{keys}")
print(f"字典内，其中一个嵌套的字典的全部keys：{keys2}")

del grade["小明"]["英语"]
print(grade)

# grade_check = grade["小明"]["语文"]
# print("小明的语文成绩是：%d" % grade_check)
# print(f"小明的成绩是：{grade['小明']}")
# # word = grade.pop("小明")