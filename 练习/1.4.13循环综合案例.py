# 公司准备一万块奖金池，一共20名员工按顺序进行抽奖。
# 抽奖规则1：中奖可以得到1000
# 抽奖规则2：每个人系统会随机在1到10生成随机数字
# 如果数字小于6(不含)，则未抽中，直接下一位
# 如果奖金池清空或者20人全部抽完则抽奖结束。
# 根据要求，判断人数，判断奖池存量，判断幸运数字。存量为0则直接结束。人数到20也结束。
"""
money = 10000
import random
for i in range(1,21):
    luck = random.randint(1, 10)
    if money >0 and luck >=6:
        print(f"恭喜员工{i}，幸运分达到惊人的{luck}，可以领取1000元大奖")
        money -= 1000
        print(f"现在奖池还有{money}元")
    elif money == 0:
        print("奖池已经清空，祝福大家生活愉快。")
        break
    elif luck <6 :
        print(f"员工{i}你的幸运分还差一点，抱歉，继续下一位")
print("你们都是太棒了！")
"""
####  以下是有continue和break版本
"""
import random
money = 10000
for i in range(1, 21):
    if money == 0:
        print("奖池已经清空，祝福大家生活愉快。")
        break
    luck = random.randint(1, 10)
    if luck < 6:
        print(f"员工{i}你的幸运分还差一点，抱歉，继续下一位")
        continue
    print(f"恭喜员工{i}，幸运分达到惊人的{luck}，可以领取1000元大奖")
    money -= 1000
    print(f"现在奖池还有{money}元")
else:
    print("你们都是太棒了！")
"""
### 以下是使用while循环
import random

money = 10000
employee = 1

while employee <= 20:
    if money == 0:
        print("奖池已经清空，祝福大家生活愉快。")
        break
    luck = random.randint(1, 10)
    if luck < 6:
        print(f"员工{employee}你的幸运分还差一点，抱歉，继续下一位")
        employee += 1
        continue
    print(f"恭喜员工{employee}，幸运分达到惊人的{luck}，可以领取1000元大奖")
    money -= 1000
    print(f"现在奖池还有{money}元")
    employee += 1
else:
    print("你们都是太棒了！")