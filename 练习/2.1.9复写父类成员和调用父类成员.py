class Phone:
    # 父类
    IMEI = None
    producer = "bmw"

    def cal_by_5g(self):
        print('2025年新功能，5g通话启动')

class Phone2025(Phone):
    producer = "abc"   # 复写父类的成员属性,但是对父类无影响

    def cal_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        print("使用5g网络进行通话")
        print("关闭CPU单核模式，确保性腊")

phone = Phone2025()
phone.cal_by_5g()
print(phone.producer)

aaa = Phone
print(aaa.producer)