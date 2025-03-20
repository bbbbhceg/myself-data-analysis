# 创建一个类
class Student:
    # 因为构造方法内有对应成员变量的存在，
    # 所以重复的成员变量可以省略
    name = None   # 记录学生姓名
    age =  None    # 记录学生年龄
    gender = None # 记录学生性别
    def say_hi(self):
        print(f"你好呀{self.name}")

    def __init__(self,name_,age_,gender_):
        # 加一个下划线_，用以区分构造方法的参数，和所述类的成员变量
        self.name = name_
        self.age = age_
        self.gender = gender_
# 创建对象
stu_1 = Student("1",15,"man")
stu_1.name = "2"
print(stu_1.name)
print(stu_1)    # 结果是这个对象的内存地址<__main__.Student object at 0x000001F2519B7C70>
print(str(stu_1))   # 和上边的结果一样.
"""
演示，参数传入不够
stu2 = Student("1")
print(stu2.name)
报错：TypeError: Student.__init__() missing 2 required positional arguments: 'age_' and 'gender_'
"""

"""
# 演示，创建类对象的时候，可以进行位置传参
stu_2 = Student("tom",gender_="woman",age_=15)
print(stu_2.name,stu_2.gender,stu_2.age)  # 完美运行
"""







