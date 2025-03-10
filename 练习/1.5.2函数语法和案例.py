def say_hi(x):
    if x > 5:
        print(f"hi,一天干饭{x}次，你就是资深干饭人。")
    else:
        print(f"抱歉，你一天才干{x}次饭，我无法进行资深干饭人的颁奖。")




def add (a,b):
      result = a + b
#     print(f"{a}+{b}={a+b}")
      return result
print(add(15,33))

# 要对10人进行干饭次数检测，但是数据是用random随机生成的
# 范围是1到10，数字小于6则拒绝他说hi，我是资深干饭人
# 否则，就接受
"""
import random
for x in range(1,11):
    num = random.randint(1, 10)
    print("参赛选手%s号，" % x,end="")
    print("我将对你进行干饭次数检测！")
    say_hi(num)
    print()
"""

