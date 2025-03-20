# 创建一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        print("执行响铃操作")
# 创建2个闹钟对象
clock1 = Clock()
clock1.id = "123"
clock1.price = 12.34
clock1.ring()
print(f"id:{clock1.id},price:{clock1.price}")

clock2 = Clock()
clock2.id = "156"
clock2.price = 15.62
clock2.ring()
print(f"id:{clock2.id},price:{clock2.price}")