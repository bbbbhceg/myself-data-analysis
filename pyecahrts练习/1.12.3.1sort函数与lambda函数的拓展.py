"""
这个文件内，我将进行sort函数和lambda函数拓展部分实战
"""
# 准备列表
my_list = [["a",33],["b",55],["d",11]]

"""
# 定义拥有函数名称的方法，以便sort方法的调用
def choose_sort_key(element):
    return element[1]
my_list.sort(key=choose_sort_key,reverse=True)
print(my_list)   # 进行输出检测：[['b', 55], ['a', 33], ['d', 11]]
"""

# 使用lambda方法，以便sort方法的调用
# 这个sort函数的内参数key，就是执行排序的关键点，被赋值的值就是用于排序的数值
# 之所以写出这样，又需要函数，是因为，这些用于排序的数值，大概率没有标识符
# 只能用函数将其一个个挑出来
my_list.sort(key=lambda element : element[1],reverse=True)
"""
用自己的大白话解释这一段就是：
对my_list这个列表进行排序，排序的的依据\关键点key是lambda函数的返回值

"""