# ↓这个叫函数，调用时直接用函数名字就行
def add1(a,b):
    """
    输入两个整数实参，返回相加的和
    :param a: 整数形参1
    :param b: 整数形参2
    :return:  整数类型的相加和
    """
    return  a + b
# ↓调用函数
num1 = add1(1,15)

# ↓这个叫方法，调用时需要先声明是那个类
# 之后才能调用声明类的成员方法
"""
class Student:
    def add2(self,a, b):
        return a + b
student = Student()
num2 = student.add2(1,77)
"""
# ok,现在我要进行列表元素查询方法的尝试
# 先定义一个列表
test = "你好，我正在进行查询操作的测试"
mylist1 = [6,"abb",1,"我爱干饭",test]
# 接着我要查询某一个元素的下标，并将查询得到的下标赋予一个变量
index_1 = mylist1.index(test)
print(f"你查询的元素，在列表的下标是{index_1}")

# 现在我要进行列表修改方法的测试
"""
my_list2 = [1,2,3]
my_list2[2] = 666
print(my_list2)
"""
# 输出的结果：[1, 2, 666]

# 列表插入功能（方法）
"""
my_list5 = [123,456,789]
my_list5.insert(1,"阿巴阿巴")
print(my_list5)
"""

# 列表追加单个元素的方法
"""
my_list6 = [1,22,333]
my_list6.append(4444)
my_list6.append(66*2)
my_list6.append(6 > 2)
print(my_list6)
"""
# 输出的结果是：[1, 22, 333, 4444, 132, True]

# 列表追加多个元素的方法
my_list = [1,2,3]
my_list.extend([4,5,6])
print(my_list)  # 结果:[1，2，3，4，5，6]

list000 = [0,1,2,3,4,5,6]
list002 = ["a","b","c","d","e"]
list000[-1] = 999
print(list000)   # [0,1,2,3,4,5,999]
list000.extend(list002[:3])   # 列表的extend方法可以操作指定数据容器的指定部分。
print(list000)   # [0,1,2,3,4,5,999,'a', 'b', 'c']
print(list002) # ['a', 'b', 'c', 'd', 'e']




