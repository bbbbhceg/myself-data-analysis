# 我要在这个这个文件中进行序列的切片操作
# 需要注意的是，切片操作是左闭右开（在结束下标填的情况下）
# 三种序列类型，列表，元组，字符串
# 列表的切片操作
list1 = [1,2,3,"list",True,55555555,["嵌套列表元素1","2222"],(256,"元组的嵌套"),5-2]
new_list = list1[2:-1:1]
print(new_list)
print("列表的切片类型是：",type(new_list))
# 输出：[3, 'list', True, 55555555, ['嵌套列表元素1', '2222'], (256, '元组的嵌套')]

# 接下来测试的是：元组的切片操作
tuple1 = (1,2,3,"list",True,55555555,["嵌套列表元素1","2222"],(256,"元组的嵌套"),5-2)
new_tuple = tuple1[3:-2:2]
print(new_tuple)
print("元组的切片类型是：",type(new_tuple))

# 字符串
str1 = '1,2,3,"list",True,55555555,["嵌套列表元素1","2222"],(256,"元组的嵌套"),5-2'
index1 = str1.index("-")
print(index1)
new_str = str1[-2:1+2:-1]
print("字符串的切片类型是：",type(new_str))
print(new_str)
# -5,)"套嵌的组元",652(,]"2222","1素元表列套嵌"[,55555555,eurT,"tsil",3
# -5,)"套嵌的组元",652(,]"2222","1素元表列套嵌"[,55555555,eurT,"tsil",3



"""
str1 = '1,2,3,"list",True,55555555,["嵌套列表元素1","2222"],(256,"元组的嵌套"),5-2'
index1 = str1.index("222")
print(type(index1))   # 确认index关键字返回值的类型为int
print(index1)    # 确定返回值是多少
print("字符串的长度为",len(str1))  # 确定字符串内容的整体长度
new_str2 = str1[int(input(f"输入起始位置数字，需要小于{len(str1)}，但是大于{index1}")):str1.index("222"):-1]
print("字符串的切片类型是：",type(new_str2))
print(new_str2)

"""

# 链式编程进行黑马程序员的输出
my_str = "万过薪月，员序程马黑来，nohtyP学"
# split分隔"，"replace替换"来"为空，倒序字符串，分步进行书写版本。
# split这个字符串独属的关键字，在使用后会生成一个新的列表，列表的每一个元素都是字符串。
new_list1 = my_str.split("，")
print(new_list1)   # 确认new_list的样子
new_list2 = new_list[1].replace("来","")   # 删掉“来”



"""

str = "0123456789"
#  即使结束下标超过索引页不会报错，甚至连警告页没有.list tuple  str都是如此
aaa =str[3:12]
print(aaa)   # 3456789

# 结束下标是78的起始下标是7，所以等同于此处是7
bbb = str[str.index("234"):str.index("78")]
print(bbb)  # 23456

# 234的起始下标是2，所以此处等同于2
ccc = str[str.index("78"):str.index("234"):-1]
print(ccc)  # 76543

"""





