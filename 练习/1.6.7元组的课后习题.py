# 要求：定义一个元组，内容是:('周杰轮',11, ['football' , 'music'])
# 记录的是一个学生的信息（姓名、年龄、爱好)
# 请通过元组的功能（方法)，对其进行
# 1．查询其年龄所在的下标位置
# 2．查询学生的姓名
# 3．删除学生爱好中的football
# 4．增加爱好: coding到爱好list内
tuple1 = ('周杰轮',11, ['football','music'] )
# 1．查询其年龄所在的下标位置
print(tuple1.index(11))
# 2．查询学生的姓名
print(tuple1[0])
# 3．删除学生爱好中的football,4．增加爱好: coding到爱好list内
tuple1[2][1] = 'coding'

# 检测成功与否
print(tuple1)