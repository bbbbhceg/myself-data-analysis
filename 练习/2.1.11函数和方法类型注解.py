# 1.函数的方法的类型注解语法
# 2.函数返回值的类型注解
"""
def 函数/方法名(形参名:类型，形参名:类型，......) :
    pass
"""
# 示例如下：
def add(x:int,y:int):  # 添加了形参类型注解
    return x+y
# 调用这个函数，在括号内Ctrl键+p就可以显示参数的需要的数值类型
add(1,2)

# 展示一下，如何对返回值进行类型注解
def func(data:list)->int:
    list_1 = data
    num = len(list_1)
    return num
func([1,2,3])

