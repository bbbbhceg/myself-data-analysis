# 需要一个钱的变量，一个冰激凌变量，一个汽水变量，钱包初始金额为50，并输出给用户显示钱包余额
money = 50
icecream = 10
water = 5
print("钱包的余额是：",money,"元,冰激凌的价格是：",icecream,"元")
#下一个动作是，用钱包里的钱，花费十元买了冰激凌，并显示冰激凌的花费
money = money-icecream
print("购买了一个冰激凌，花费：",icecream,"元")
print("汽水的价格是：",water,"元")
water = water*2
print("你购买了两瓶汽水，所以购买汽水的花费为：",water,"元")
money = money-water
print("购物完毕，你现在钱包的余额是：",money,"元")
# 接下来都是数据类型的测试
print(type(6661232313))
print(type(12.32))
print(type("xabxkw5"))
int_type = type(123)
print(int_type)