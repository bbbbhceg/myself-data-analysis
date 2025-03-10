# def say_hi():
#     print("hi...")
# result = say_hi() # 此变量存储的是函数的返回值，而非其他。
# print(f"当函数没有使用return关键字的时候，实际的返回值是：{result}")
# print(f"返回值的类型是：{type(result)}")
# # 以下是主动返回None的结果
# def say_hi2():
#     print("hi...")
#     return None
# result2 = say_hi2()
# print(f"当函数使用return关键字但返回的是None的时候，实际的返回值是：{result2}")
# print(f"返回值的类型是：{type(result2)}")
"""
以下是关于None关键字，用于if判断的例子
"""
def check_num(x):
    """
    这是一个检测输入数字是否大于三的函数。
    如果大于三返回一个print，否则返回None
    :param x:用于函数内部if的判断
    :return:大于三则返回True，否则是False
    """
    if x>3:
        print("干饭很积极！")
        return True
    else:
        return None
result = check_num(4)
if result == None:
    print("干饭不积极，脑袋有问题")
