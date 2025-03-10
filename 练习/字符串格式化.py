"""多个变量%拼接
class_num = 21
avg_salary = 12000
print("他们是第%s期，平均的工资是%s元" % (class_num,avg_salary))
name1 = "张三"
message = "李四和%s经常出现" % name1
print(message)
# 接下来试试数字的拼接，输出，张三今年22，李四和张三经常出现
age1 = 22
message2 = "张三今年%s，%s" % (age1,message)
print(message2)
# 如果用+进行拼接，则需要将age1的22进行格式转换成字符串。
message3 = "李四今年" + str(age1)
print(message3)
# 如果直接是+ age1 则会报错.右上角会有黄色警告，因为用+进行字符串拼接时，不能拼接数字
message4 = "李四今年%d" % age1
print(message4)
"""
# 接下来要实验%s %d %f.%f会自动转换成小数点后6位的精度，
name1 = "长伞"
age = 20
weight = 75.5
print("有一个人名字叫%s，年龄是%d，今天的体重是%f" % (name1,age,weight))
# 接下来要进行精度控制的练习。
num1 = 15
num2 = 12.636
print("当数字15限制整体宽度为5时，输出：%5d" % num1)
print("当数字12.236整体宽度为7，小数部分为2时：%7.2f" % num2)
print("当数字12.236整体宽度为7，小数部分为2时：%7.2d" % num2)
