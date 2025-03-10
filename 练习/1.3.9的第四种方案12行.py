# 在这个方案中，我连函数也舍弃掉，以只有一次的代价，得到了进一步地压缩。
import random
random_num = random.randint(1, 10)  # 限定目标数字是1到10之间的。
for attempt in range(1, 4):  # 限定最多进行三次循环。
    person_guess = int(input(f"请进行你的第{attempt}次的猜数字吧："))
    if person_guess == random_num:
        print(f"哇，恭喜你猜中了，数字就是{random_num}，你一共猜了{attempt}次。")
        break
    elif person_guess > random_num:
        print("你猜的有点大诶")
    else:
        print("你猜的有点小")
print(f"很可惜，三次机会都用完了，最后的数字是{random_num}，再接再厉吧！")