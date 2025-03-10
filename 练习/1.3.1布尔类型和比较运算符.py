"""
bool_1 = True
bool_2 = False
print(f"bool_1变量内容是：{bool_1}，类型是：{type(bool_1)}")
print(f"bool_1变量内容是：{bool_2}，类型是：{type(bool_2)}")
# 以下是比较运算符号的运用
num1 = 10
num2 = 10
num3 = 12
print(f"10 == 10 的结果是：{num1 == num2}") # 10 == 10 的结果是：True
print(f"10 != 10 的结果是：{num1 != num2}") # 10 != 10 的结果是：False
print(f"10 != 12 的结果是：{num1 != num3}") # 10 != 12 的结果是：True
print(f"10 <= 12 的结果是：{num1 <= num3}") # 10 <= 12 的结果是：True
print(f"10 > 12 的结果是：{num1 > num3}") # 10 > 12 的结果是：False
"""
# 接下来试试字符串的比较
name1 = "abcd"
name2 = "Abcd"
print(f"abcd == Abcd 的结果是：{name1 == name2}")

print(f"5 == Abcd 的结果是：{5 == name2}")
print(f"5 == 2 的结果是：{5 == 2}")
# print(f"abcd == Abcd的结果是：{"abcd" == "Abcd"}")
print(type(str((name1 == name2))))
print("222abcd == Abcd 的结果是：%s" % (name1 == name2))