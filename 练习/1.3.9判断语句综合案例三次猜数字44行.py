# 定义一个数字，范围在1-10，用户进行最多三次猜测。
# 每一次猜测都会提示用户，数字是比目标数字小或者大。
import random
num = random.randint(1,10)
print("亲爱的用户，让我们来玩猜数字游戏吧，猜测范围是1到10")
print(num)
num1 = int(input("我已经准备好数字了，请开始猜测吧！"))
if num1 != num: # 先进行第一次输入是否等于的一级判断，然后再进行第一次输入大于和小于的二级判断
    if num1 > num:
        print("你猜的数字比目标数字大哦")
        num2 = int(input("哇，有些可惜，再来第2次吧"))
        if num2 != num:   # 进行第二次输入是否等于的一级判断，然后再进行第二次输入大于和小于的二级判断
            if num2 > num:
                print("你猜的数字比目标数字大哦")
                num3 = int(input("哇，有些可惜，再来最后一次吧"))
                if num3 != num:
                    print("很可惜，最后数字就是" + str(num) + "，再接再厉吧！1")
                else:
                    print("哇恭喜你猜中了！数字就是" + str(num))
            elif  num2 < num:
                print("你猜的数字比目标数字小哦")
                num3 = int(input("哇，有些可惜，再来最后一次吧"))
                if num3 != num:
                    print("很可惜，最后数字就是" + str(num) + "，再接再厉吧！1")
        else:
            print("哇恭喜你猜中了！数字就是" + str(num))
    else: # num1 <num
        print("你猜的数字比目标数字小哦")
        num2 = int(input("哇，有些可惜，再来第2次吧"))
        if num2 != num:
            if num2 > num:
                print("你猜的数字比目标数字大哦")
                num3 = int(input("哇，有些可惜，再来一次吧"))
                if num3 != num:
                    print("很可惜，最后数字就是" + str(num) + "，再接再厉吧！2")
            else:
                print("你猜的数字比目标数字小哦")
                num3 = int(input("哇，有些可惜，再来一次吧"))
                if num3 != num:
                    print("很可惜，最后数字就是" + str(num) + "，再接再厉吧！3")
                else:
                    print("哇恭喜你猜中了！数字就是" + str(num))
        else:
            print("哇恭喜你猜中了！数字就是" + str(num))
else:
    print("哇恭喜你猜中了！数字就是" + str(num))
# 输入验证不足：用户输入的可能不是数字，或者输入的数字不在1到10的范围内。这种情况下，程序会抛出异常。