# 设计类
happy = "you"
class Student:
    name = None   # 记录学生姓名
    age = None    # 记录学生年龄
    gender = None # 记录学生性别
    def say_hi(self):
        print(f"你好呀{self.name}{happy}")

    def  say_hi2(self,infor):
        print(f"你好呀{self.name},{happy},{infor}")
# 创建对象
stu_1 = Student()
stu_2 = Student()
stu_3 = Student()

# 对象属性赋值
stu_1.name = "tom"
stu_1.age = 12
stu_1.gender = "man"
stu_1.say_hi2("真不错")   # 输出：你好呀tom,you,真不错

stu_2.name = "jack"
stu_2.age = 15
stu_2.gender = "man"

stu_3.name = "luna"
stu_3.age = 18
stu_3.gender = "woman"
stu_3.say_hi()   # 会打印出：你好呀luna

