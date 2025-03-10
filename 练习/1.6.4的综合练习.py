# 有一个列表，内容是:[21, 25,21,23,22,20]，记录的是一批学生的年龄
# 请通过列表的功能（方法)，对其进行
# 1．定义这个列表，并用变量接收它
# 2．追加一个数字31，到列表的尾部
# 3．追加一个新列表[29,33,30]，到列表的尾部
# 4．取出第一个元素（应是:21)
# 5.取出最后一个元素（应是:30)
# 6.查找元素31，在列表中的下标位置
students_age = [21, 25,21,23,22,20]   # 1．定义这个列表，并用变量接收它
students_age.append(31)  # 2．追加一个数字31，到列表的尾部
print(students_age)   # 确认追加成功，位置正确。
new_list = [29,33,30]
students_age.append(new_list)    # 3．追加一个新列表[29,33,30]，整体追加到列表的尾部
students_age.extend(new_list)     # 3.1 追加一个新列表但是将内容取出追加
pop_num = students_age.pop(0)  # 4．取出第一个元素（应是:21)
print(pop_num)
print(students_age)
num2 = students_age[-4][-1]  # 5.取出最后一个元素（应是:30)
print(num2)
index31 = students_age.index(31) # 6.查找元素31，在列表中的下标位置
print(index31)
students_age.count(21)  # 这个关键字是自带输出的
print(len(students_age))


