"""
需求分析：
    要求设计一个类，记录10位学生的姓名，年龄，地址
实现技术要求：
    通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘录入
    输入完成后，使用print语句，完成信息的输出
"""
class Student:
    name = None
    age = None
    gender = None
    def __init__(self,name_,age_,gender_,city_):
        self.name = name_
        self.age = age_
        self.gender = gender_
        self.city = city_
i = 1
for x in range(3):
    print(f"当先录入第{i}位学生信息，总共需要录入3位学生的信息")
    x = Student(name_=input("请输出学生姓名："),
                age_=input("请输入学生的年龄："),
                gender_=input("请输入学生的性别："),
                city_=input("请输入学生的来源城市：")
                )
    print(f"学生{i}信息录入完成，信息为：【学生姓名：{x.name}，年龄：{x.age},性别：{x.gender},来源城市：{x.city},】")
    i += 1
