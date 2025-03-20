class Student:
    name = None
    age = None
    gender = None
    def __init__(self,name_,age_,gender_,city_):
        self.name = name_
        self.age = age_
        self.gender = gender_
        self.city = city_

students = []  # 用于存储学生对象的列表,相比之前的散装,更便于管理

for i in range(1, 4):  # 假设需要录入3位学生
    print(f"当前录入第{i}位学生信息，总共需要录入3位学生的信息")
    student = Student(
        name_=input("请输入学生姓名："),
        age_=input("请输入学生的年龄："),
        gender_=input("请输入学生的性别："),
        city_=input("请输入学生的来源城市：")
    )
    students.append(student)  # 将学生对象添加到列表中
    print(f"学生{i}信息录入完成，信息为：【学生姓名：{student.name}，年龄：{student.age}, 性别：{student.gender}, 来源城市：{student.city}】")

# 输出所有学生信息
for i in range(len(students)):
    print(f"学生{i+1}信息：【学生姓名：{students[i].name}，年龄：{students[i].age}, 性别：{students[i].gender}, 来源城市：{students[i].city}】")