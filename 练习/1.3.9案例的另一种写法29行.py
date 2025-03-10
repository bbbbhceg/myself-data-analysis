# 定义一个数字，范围在1-10，用户进行最多三次猜测。
# 每一次猜测都会提示用户，数字是比目标数字小或者大。
# 这个版本，相比第一个版本，更精简
# 第一，因为更利用了if，elif和else的逻辑。
# 第二，用的逻辑比较符号也更简单，没有有!= 这个逻辑运算符号

import random
num = random.randint(1,10)
print(num)
guess_num1 = int(input("开始你的第一次猜测吧！"))
if guess_num1 == num:
    print("你他奶奶的真是天才，第一次就猜中了")
else:
    if guess_num1 > num:
        print("有点可惜，你猜的有点大。")
    else :
        print("你猜的有点小。")
    guess_num2 = int(input("开始你的第二次猜测吧！"))
    if guess_num2 == num:
        print("你他奶奶的真是天才，第二次就猜中了")
    else:
        if guess_num2 > num:
            print("有点可惜，你猜的有点大")
        else :
            print("你猜的有点小")
        guess_num3 = int(input("开始你的第三次猜测吧！"))
        if guess_num3 == num:
         print("你他奶奶的真是天才，第三次就猜中了")
        else:
            if guess_num3 > num:
                print("有点可惜，你猜的有点大")
                print("很可惜，最后数字就是" + str(num) + "，再接再厉吧！")
            else :
                print("你猜的有点小")
                print("很可惜，最后数字就是" + str(num) + "，再接再厉吧！")
# 输入验证不足：用户输入的可能不是数字，或者输入的数字不在1到10的范围内。这种情况下，程序会抛出异常。