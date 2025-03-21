"""
设计一个手机类，内部包含:
私有成员变量:__is_5g_enable，类型bool，True表示开启5g,False表示关闭5g
私有成员方法:__check_5g()，会判断私有成员_is_5g_enable的值
    ·若为True，打印输出:5g开启
    ·若为False，打印输出:5g关闭，使用4g网络
公开成员方法: call_by_5g()，调用它会执行
    ·调用私有成员方法:__check_5g0，判断5g网络状态
    ·打印输出:正在通话中
运行结果要求显示:5g关闭，使用4g网络正在通话中
(提示：Ctrl键+10可缩略大段独立注释)
"""
class Phone:
    __is_5g_enable = False

    # 私有成员方法
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    # 私有成员方法
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

# 创建类对象,一定记得括号
phone1 = Phone()
phone1.call_by_5g()


# 反思，这个就是想要实现，在用户调用手机的打电话功能时，进行通话状态/信号检查