# 在这文件内，我将测试，几种比较常见的魔术方法
# 例如：
# __str__,字符串方法
# __It__,小于、大于符号比较
# __Ie__,小于等于、大于等于符号比较
# __eq__,==符号比较=
class Student_1:
    def __init__(self, name_, age_):
        self.name = name_
        self.age = age_
        # __str__魔术方法
    def __str__(self):
        return f"Student类对象：name：{self.name},a{self.age}"

# str魔术方法的使用
stu0 = Student_1(name_="tom",age_=12)
print(stu0)         # Student类对象：name：tom,a12
print(str(stu0))    # Student类对象：name：tom,a12
print(type(stu0))   # <class '__main__.Student'>

# __It__魔术方法的使用
class Student_2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
     #定义 __It__魔术方法，用于类对象的比较
    def __lt__(self, other):
        return self.age < other.age

stu1 = Student_2("周杰轮",11)
stu2 = Student_2("林军杰",13)
print(stu1 < stu2)     # True
# 在我们没有定义魔术方法：__It__时
# 如果是这样直接比较大于或小于，会报错，因为类中没有支持比较的方法，程序不知道比较哪一个点
# 当我们需要进行比较，并已经定义__It__魔术方法时
# 就可以按照__It__魔术方法所定义的点，进行比较，返回True或False
print(stu1 > stu2)     # False
# 但是需要注意的是，__It__只能包括，大于或者小于的比较，如果你加上=符号,或者单纯的等于号判断
# 则会报错：TypeError: '<=' not supported between instances of 'Student_2' and 'Student_2'
# 例如↓
# print(stu1 <= stu2)

# __le__魔术方法
class Student_3:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # __le__魔术方法
    def __le__(self, other):
        return  self.age <= other.age

stu3 = Student_3("周杰轮",11)
stu4 = Student_3("林军杰",13)
print(stu3 <= stu4)  # True
print(stu3 >= stu4)  # False

print(stu3 == stu4)
# False,虽然结果是对的，但是，实际上，即使是age相同，它也会报错
# 因为 == 符合实际对比的是连个类对象的内存地址
# 判断两个类对象的比较点，是否相等
# 用的魔术方法确实是__le__，但是是在进行判断>=,<=时进行的。
# 而不是在 == 符号这里进行的。

# __eq__魔术方法
class Student_4:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # __eq__魔术方法
    def __eq__(self, other):
        return  self.age == other.age

stu5 = Student_4("周杰轮",11)
stu6 = Student_4("林军杰",13)
stu7 = Student_4("aaa",13)
print(stu5 == stu6)  # False
print(stu6 == stu7)  # True