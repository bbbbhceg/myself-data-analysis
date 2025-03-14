# 在这个文件内，我需要实现两个功能，以期调用该文件时，可以处理字符串
# 函数: str_reverse(s)，接受传入字符串，将字符串反转返回
# 函数:substr (s, x, y)，按照下标x和y，对字符串进行切片
def str_reverse(s):
    """
    接受传入字符串，将字符串反转返回
    :param s: 需要时str类型
    :return: 将返回，反转的字符串
    # """
    # rev_str = sorted(s,reverse=True)
    # return rev_str
    return s[::-1]
# 用到了，数据容器通用的sorted排序功能
# 反思，其实我这里混淆了，数据容器通用的排序功能sorted和翻转字符串功能。我将注释掉sorted，更正为正确的

def substr (s, x, y):
    """
    功能是输入的字符串按照制定的下标进行切片，然后返回切片部分
    :param s: 需要处理的字符串
    :param x: 起始下标
    :param y: 结束下标
    :return: 回切片部分
    """
    sub_str = s[x:y]
    return sub_str
# 这个是运用了序列类型数据容器的通用操作，容器[起始下标:结束下标:步长]

"""
最后写完的反思，我没有进行功能的测试，可以使用main将测试功能包含进去，
如果我测试的话，就不会出现刚才，sorted和反转字符串混合使用的情况了
"""
if __name__ == '__main__':
    """
    这是测试该文件的模块
    """
    str1 = "123456789abcd"
    print(str_reverse(str1))
    print(substr(str1,5,9))