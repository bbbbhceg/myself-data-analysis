# 多态，指的是：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态。
# 在程序内，表现的是：
# 同样的行为（函数），传入不同的对象（dog，cat），得到不同的状态（不同的输出结果）。
# 创建 "父类"
class Animal:
    def speak(self):
        pass
#  创建"子类1"
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
#  创建"子类2"
class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):   # 注释形参的类型是Animal类型
    animal.speak()
# 创建类对象
dog = Dog()
cat = Cat()

# 调用函数，并输入Animal的两个子类
make_noise(dog)   # 输出：汪汪汪
make_noise(cat)   # 输出：喵喵喵


#演示抽象类
# 顶层设计/标准设计
class AC:
    def cool_wind(self):
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass
    def swing_l_r(self):
        """左右摆风"""
        pass
# 空调商1
class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")
# 空调商2
class Gree_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()
# 创建类对象
midea_ac = Midea_AC()
gree_ac = Gree_AC()

# 调用函数，参数放入类对象
make_cool(midea_ac)
make_cool(gree_ac)