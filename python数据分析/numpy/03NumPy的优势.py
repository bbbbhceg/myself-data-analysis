# 因为这一节的的1亿随机数占用太高，就暂时全部注释掉
# # 使用time模块，比较Python列表和numpy计算大数据的时间，以对比出优势
# import time
# import numpy,random
#
# # 首先生成一个超级大数组
# python_list = []
#
# for i in range("这里应该放100000000，也就是1亿"):  # 范围是1亿
#     # 每次循环都会向python_list中追加一个随机数，一共追加1亿次
#     python_list.append(random.random())
# # 将同一段数据赋予numpy的数组变量
# ndarray_list = numpy.array(python_list)
#
# """将同一段大数据，分别进行计算，并用计时，以比较运算效率，得出优劣"""
# # 原生python_list求和
# t1 = time.time()
# a = sum(python_list)
# t2 = time.time()
# d1 = t2-t1
#
# # ndarray求和
# t3 = time.time()
# b = numpy.sum(ndarray_list)
# t4 = time.time()
# d2 = t4-t3
#
# print(d1)  # list用时：3.606496810913086
# print(d2)  # adarray用时：0.2368757724761963
# # 两者之间的是15.22526670082101倍
# # 也就是在这个情况下，python的只有numpy的6.568%的效率
# """足以说明，进行大数据的的处理时，numpy效率远高于原生python"""
#
#
#
#
