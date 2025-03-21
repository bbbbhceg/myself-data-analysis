class Phone:
    weight = None
    banknote = None   # 直接不用money

    __current_voltage = 1.5  # 私有变量，电压

    def call_by_5g(self):    # 尝试在非私有方法内，调用私有变量和方法
       if self.__current_voltage >= 1:
            print("5g通话已开启")
       else:
           self.__keep_single_core()
           print("电量不足，无法使用5g通话，并已设置为单核运行进行省电。")

    def __keep_single_core(self):   # 私有方法
        print("切换cup单核运行，设置成功。")

# 创建类对象
phone1 =Phone()
#尝试调用私有变量和非私有变量
phone1.__current_voltage = 22   # 不报错，但无用
phone1.weight = 223
# phone1.__keep_single_core()   # 强制调用会直接报错：AttributeError.表示类中没有找到该参数
phone1.call_by_5g()
