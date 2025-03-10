# 语法1：del 列表[下标]    # 注意这里是中括号
# 语法2：列表.pop(下标)	# 注意这里是小括号
"""
my_list = ["你好","待删除元素1","待删除元素2"]
del my_list[1]
print(my_list)
my_list.insert(2,"二次装填元素") # 因为是插入元素，所以要提前指定位置
my_list.append(666) # append这个单词，动词是附加的意思。都附加了，所以默认是在指定列表的尾部，就不用特意指定位置。
print(my_list)
pop = my_list.pop()  # 列表删除的第二种方法，因为要删除，知道没有才会删除，就不用再附加内容，只用附加下标即可。
print(pop)
print(my_list)
my_list.insert(2,"增加的元素")
print(my_list)
del my_list[0:2]
print(my_list)
"""
list22 = [5,6,3]
my_list2 = [5,"元素位置1",1,"元素位置2","元素位置3","元素位置4","元素位置5","元素位置6"]
num = my_list2.remove("元素位置5")  # 尝试接收remove关键字的返回值
print(num)  # 打印返回值
print(my_list2) # 打印经历remove之后的列表
len1 = len(my_list2)
print(len1)   # 打印经历remove之后的列表长度
my_list2.insert(4,list22)  # 插入一个元素数量为三的列表
print(my_list2)  # 打印一下确认插入了
len2 = len(my_list2)  # 打印len计算结果
print(f"在插入了一个元素数量是3的列表之后，len识别的原7元素数量的列表是8还是其他数字？答案是：{len2}")

