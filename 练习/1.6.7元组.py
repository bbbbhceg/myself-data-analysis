# 定义元组的字面量
("元素1","元素2","元素...")
# ↑这里会弹出警告，表示这个没有任何作用，但是不耽误程序运行
# 元组的英文名称是tuple
tuple1 = ("元素1",123,12.3,True,(2,3,"元素"))
print(tuple1)
# 定义空元组,与列表的定义非常相似
tuple2 = ()    # 方式1
tuple3 = tuple()  # 方式2
tuple4 = ("hellow",666)
tuple5 = ("hellow") # 这里会提示括号冗余，因为这样定义会被视为字符串
list1 = ["你好"]

# 检测类型
print(type(tuple5))
print(type(tuple4))
print(type(tuple3))
print(type(tuple2))
print(type(tuple1))

# 我将测试元组的功能
# tuple1 = ("元素1",123,12.3,True,(2,3,"元素"))
num = tuple1[4][2]

##############################
tuple1 = ("元素1",123,12.3,True,(3,2,"元素"),(3,),[3])
# index()的用法,查找某一个数据，找到则返回下标，否则报错。
print(tuple1.index("元素1")) # 返回的下标是0

"""
count()的用法,查找指定元素的数量
一个位置只能匹配一次，且如果是嵌套则默认不是
但是，注意元组的单个元素的嵌套，如果是（）而非（，）就会默认括号多余进行匹配
否则，就是默认不是
"""

print(tuple1.count(3))   # 实际打印是0
# 进行len(元组)，统计元组内的元素个数
print(len(tuple1))  # 打印是7

# 我将依次输入元组内的元素，while循环。
index = 0
while index < len(tuple1):
    print(f"此元组组的元素有：{tuple1[index]}")
    index += 1


