# 我将使用while循环和for循环进行列表的遍历循环
my_list = [1,"m",2,"5133"]
def list_while_func(x):
    """
    调用此函数时，需要传入一个列表
    然后会将列表内的元素逐个输出
    :param x: 列表名称
    :return:
    """
    index = 0
    while index < len(x):
        element = x[index]
        print(f"取出的元素是：{element}")
        index += 1
list_while_func(my_list)

def list_for_func(x):
    """
    调用此函数时，需要传入一个列表
    然后会将列表内的元素逐个输出
    :param x: 列表名称
    :return:
    """
    index = 0
    for element in x:
        print(f"222取出的元素是：{element}")
        index += 1
list_for_func(my_list)

# 我要定义一个列表，内容是1到10
# 要求1是遍历列表，并且取出列表内的偶数，并存入一个新地列表对象中
# 要求2，使用while循环和for循环各一次
list1 = [1,2,3,4,5,6,7,8,9,10]
def while_list(x):
    index = 0
    list2 = []
    while index < len(x):     # 这里是不能取等号的，如果取等号了你是对下标的理解不到位。
        element = x[index]  # 取出下标为index的元素赋予element
        if (element % 2) == 0:
            list2.append(element)  # 列表的增加操作，只有三种，insert需要指定位置，extend会改变格式，所以append关键字才是最好的选择。
        index += 1
    print(list2)


# while_list(list1)

def for_list(x):
    index = 0 # 这里取的指数是下标的意思
    list2 = []
    for element in x:
        if (element % 2) == 0:
            list2.append(element)  # 列表的增加操作，只有三种，insert需要指定位置，extend会改变格式，所以append关键字才是最好的选择。
        index += 1
    print(list2)

for_list(list1)