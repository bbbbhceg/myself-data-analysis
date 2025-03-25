"""
继承的应用场景多是更新迭代，
不想直接粘贴代码然后添加，而是直接使用继承语法
这样的选择有更高的自由度
继承的基础语法：
就是在新的类（即，子类）名称后加个括号，然后将需要继承的父类名称添加进去
继承还可以分为多继承和单继承
(提示：Ctrl键+10可缩略大段独立注释)
"""
class Phone:
    # 父类1
    IMEI = None
    producer = "bmw"

    def cal_by_4g(self):
        print("正在进行4g通话")

class Phone2025(Phone): # 继承父类Phone
    face_id = "1001"   # 增加面部识别ID

    def cal_by_5g(self):
        print('2025年新功能，5g通话启动')
"""
# 创建一个子类的类对象
phone_1 = Phone2025()
print(phone_1.producer)  # 展示子类可以调用父类方法
phone_1.cal_by_4g()   # 展示子类可以调用父类方法
phone_1.cal_by_5g()

"""

"""
class 类名(父类名)∶
    类内容体
"""
# 多继承示例，咱们继续先写俩父类，分别是NFCreader，RemoteControl
class NFCreader:
    # 父类2
    nfc_type = "第五代"
    producer = "bmw"

    def read_card(self):
        print("成功读取NFC卡")

    def write_nfc(self):
        print("成功写入NFC卡")

class RemoteControl:
    # 父类3
    r_type = "红外遥控"

    def control(self):
        print("红外遥控器开启")

class MyPhone(Phone,NFCreader,RemoteControl):
    # 当你，单纯只是想继承多个父类，而不想新写东西则可以单纯写个pass关键字
    pass

phone_2 = MyPhone()
phone_2.cal_by_4g()      # 父类1的方法,正在进行4g通话
phone_2.read_card()      # 父类2的方法,成功读取NFC卡
phone_2.control()        # 父类3的方法,红外遥控器开启

# 需要注意的点：
# 当继承的多个父类中重合的成员变量名称或者方法
# 子类会自动根据父类在括号内的顺序进行调用，靠左的父类优先调用