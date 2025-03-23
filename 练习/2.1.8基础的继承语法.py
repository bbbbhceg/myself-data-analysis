"""
设计一个手机类，内部包含:

(提示：Ctrl键+10可缩略大段独立注释)
"""
class Phone:
    __is_5g_enable = False

    # 私有成员方法
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    # 私有成员方法
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

# 创建类对象,一定记得括号
phone1 = Phone()
phone1.call_by_5g()
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



# 反思，这个就是想要实现，在用户调用手机的打电话功能时，进行通话状态/信号检查