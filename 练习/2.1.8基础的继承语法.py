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
    IMEI = None
    producer = "bmw"

    def cal_by_4g(self):
        print("正在进行4g通话")

class Phone2025(Phone):
    face_id = "1001"   # 增加面部识别ID

    def cal_by_5g():
        print('2025年新功能，5g通话启动')
# 创建一个子类的类对象
phone_1 = Phone2025()
print(phone_1.producer)  # 展示子类可以调用父类方法
phone_1.cal_by_4g()   # 展示子类可以调用父类方法
phone_1.cal_by_5g()


