# 我要用while循环进行1到100的累加，并输出


num = 1
result = 0
while num < 101:
    result += num
    num += 1
print(f"1到100的累加最终的结果是：{result}")
# 反思，因为是累加，求的还是累加的结果，根据标识符见名知意，应该不写result而是sum。
# 设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数。
# 要求是每一次都会提示大了或者小了。并且猜完之后提示一共猜了多少次。且不用break和try。
import random
num = random.randint(1,100)
print(f"这个随机数是{num}")
guess_num = 0
i = 0
flag = True
while flag :
    guess_num = int(input("输入你猜测的数字"))
    i += 1
    if guess_num == num:
        print("你猜中了")
        flag = False
    else :
        if guess_num > num:
            print("你猜的有点大")
        elif guess_num < num:
            print("你猜的有点小")
print(f"你一共猜测了{i}次，这数字就是{num}")

