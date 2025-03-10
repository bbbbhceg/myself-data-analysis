# 给定一个字符串: "itheima itcast boxuegu"
# 统计字符串内有多少个"it"字符
# 将字符串内的空格，全部替换为"|"字符
# 并按照"|"进行字符串分割，得到列表
str1 = "itheima itcast boxuegu"
print(str1.count("it"))
str2 = str1.replace(" ","|")
print(str2)
list1 = str2.split("|")
print(list1)