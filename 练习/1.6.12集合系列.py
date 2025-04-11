# 我将定义一个含有重复元素的集合
# 定义一个空集合
# 通过for循环遍历列表
# 在for循环中将列表的元素添加至集合
# 最终得到元素去重后的集合对象，并打印输出

my_list= ['黑马程序员','传智播客','黑马程序员','传智播客', 'itheima', 'itcast', 'itheima', 'itcast','best']
set1 = set()
for i in my_list:
    # 在for循环中将列表的元素添加至集合
    set1.add(i)

print(set1)


# 集合的增删改查操作。
set_0 = {True,1,2,"2",3,False}
print("原始集合：",set_0)
# 输出结果：{False, 1, 2, 3, '2'}
# 结果分析：一个集合内，0和False，1和True都是相等的。且集合会保留位于前方的形式。

# 增
set_0.add("666666")
print("add操作后的集合：",set_0)
# 输出结果： {False, True, 2, 3, '2', '666666'}

# 删
set_0.pop()
print("pop操作之后的集合：",set_0)
# pop操作之后的集合： {True, 2, 3, '2', '666666'}

set_0.remove(1)
print("remove（1）操作之后的集合：",set_0)
# remove（1）操作之后的集合： {2, 3, '2', '666666'}

# set_0.clear()


# 独有操作
set_111 = {1111,222,1,"2",3}

set_dif = set_0.difference(set_111)
print("set_0.difference(set_111)的结果：",set_dif)
# set_0.difference(set_111)的结果： {'666666', 2}

set_0.difference_update(set_111)  # 直接会修改原数据，所以，不用再赋值
print("set_0.difference_update(set_111)的结果：",set_0)
# set_0.difference_update(set_111)的结果： {2, '666666'}

set_union = set_0.union(set_111)
print("set_0.union(set_111)的结果：",set_union)
# set_0.union(set_111)的结果： {1, 2, 3, '2', 1111, '666666', 222}

# 查操作
print("len操作：",len(set_0))
# len操作： 2

"""
这个集合有一个copy方法，和numpy的数组的“从现有数组中生成新数组”章节学习的copy方法的存在是一样的道理，
如果你只是单纯的创立集合1，然后中途对将集合1赋值给另外一个集合2，那么这两个集合会共享内存。
这样造成的结果就是，对其中任意几个集合进行操作，都会对另一个集合产生连带作用。
即使你将集合2再赋值给集合3…..n，都是共享一个内存地址，对任意一个操作都会进行联动。
所以集合才有一个copy。将集合复制一份，赋予另一个集合，以确保两个集合之间的操作不会联动。

python5种数据容器，允许原始数据修改的，list，set，dict都是这个逻辑，也都有对应的copy方法
"""