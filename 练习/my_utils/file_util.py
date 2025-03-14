# 在这个文件内，我需要实现两个功能，以期调用该文件时，可以处理文件
# file_util.py (文件处理相关工具，内含:)
# 函数: print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
# 函数: append_to_file(file_name,data)，接收文件路径以及传入数据，将数据追加写入到文件中
def print_file_info(file_name):
    """
    接收传入文件的路径，打印文件的全部内容
    如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
    :param file_name: 文件名称
    :return: 无返回值
    """
    f = None
    try:
        f =open(file_name,'r',encoding='utf-8')
    except:
        print('您提供的文件路径有问题，请进行检查')
    else:
        print(f.read())
    finally:
        # 如果try成功了，则f有内容，就为True，
        # 否则，就一直未None,也就是false，就不会执行f.close
        # close的操作对象是文件
        # 如果是空则会报错AttributeError: 'NoneType' object has no attribute 'close'
        if f:
            f.close()
# 反思，其实，我对finally的理解还是不到位，如果上边的try出现异常被except捕捉
# 然后finally还是要执行，那不报错了吗？会找不到变量f，报错NameError


def append_to_file(file_name,data):
    """
    接收文件路径以及传入数据，将数据追加写入到文件中
    此功能使用'a'模式，所以不会进行文件路径的判断
    :param file_name: 文件路径
    :param data: 传入数据
    :return:
    """
    with open(file_name,'a',encoding='utf-8') as f:
        f.write(data)