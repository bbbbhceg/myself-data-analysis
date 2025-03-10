# 快速格式化，不会关心类型，和精度控制的，避免了数值失真。
name = "zhang三"
name2 = "li4肆"
age = 15
weight = 12.345
print(f"她的名字叫{name}，年龄是{age}岁，体重是{weight}")
# 输出结果→她的名字叫zhang三，年龄是15岁，体重是12.345
print("这个人叫做"+name+"；另一个人的名字是"+name2)
print("第一个人的名字是%s，第二个人的名字是%6s，年龄都是%3d，体重都是%6.2f" % (name,name2,age,weight))
