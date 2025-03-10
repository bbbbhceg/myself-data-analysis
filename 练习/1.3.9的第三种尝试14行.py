# 第二个版本，相对于第一个版本代码更精简，是因为，虽然技术没有更新，但优化了逻辑，所以做到了精简。
# 在这个版本中，我将更新技术，用定义函数和使用循环的方法，看看代码量能否更精简
# 定义一个数字，范围在1-10，用户进行最多三次猜测。且用已知户只会在1到10之前进行输入
# 每一次猜测都会提示用户，数字是比目标数字小或者大。
# 循环的部分是输入和输入后的判断
import random
def guess_num():
    random_num = random.randint(1,10) # 限定目标数字是1到10之间的。
    for attempt in range(1,4):   # 限定最多进行三次循环。
        person_guess = int(input(f"请进行你的第{attempt}次的猜数字吧："))
        if person_guess == random_num:
            print(f"哇，恭喜你猜中了，数字就是{random_num}，你一共猜了{attempt}次。")
            break
        elif person_guess > random_num:
            print("你猜的有点大诶")
        else:
            print("你猜的有点小")
    print(f"很可惜，三次机会都用完了，最后的数字是{random_num}，再接再厉吧！")
guess_num()


