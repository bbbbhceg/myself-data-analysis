"""
if int(input("你的身高是多少：")) >= 120 :
    print("你的身高大于免费标准")
    print("请问你游玩等级是多少：")
    if int(input()) >= 2:
        print("你的等级大于2是可以免费游玩的，祝您游玩愉快。")
    else :
        print("抱歉，您的等级不够。需要正常购票才能入园。")
else :
    print("祝您游玩愉快")
"""
# 以下是1.3.8的礼物条件题目
# 要求如下：第一必须大于等于18岁小于等于30岁的成年人。否则无法领取。
# 第二，同时满足入职是时间大于两年，或者级别大于4或者等于2才可以领取礼物。否则无法领取。
if 30 >= int(input("请输入你的年龄：")) >= 18:
    print("你的年龄是符合条件的")
    years = int(input("你的入职时间是多少年：")) # 之所以要写出了，而不是直接在融合到下一行，是因为这样代码的可读性更好。
    if years >= 2:
        print("符合领取条件，可以领取")
    else :
        level = int(input("抱歉，您的入职年龄不符合条件，但是请问你的级别是几级？"))
        if level >=4 or level ==  -3:
            print("符合领取条件，可以领取")
        else:
            print("抱歉您无法领取。1")

else:
    print("抱歉您无法领取。2")
# 在这个案例里出现的错误：elif   int(input("抱歉，您的入职年龄不符合条件，但是请问你的级别是几级？")) >= 4  or 2:
# 以下是反思：
# 第一，这错误行，之所以不使用else，是因为，else的执行条件是，当所有 if 和 elif 条件都不满足时执行的代码块，会执行。本身不能额外添加判断条件。
# 第二，这里 or 不会达到自己想要的，级别大于四或者等于2都可以领取的效果，因为单独一个2是布尔类型，
# 即默认为true，加上or是两边任何一个为true就可以执行，所以就变成输入任何数字都可以领取。你即使在2前加一个 == 的判断也不符合Python的语法。
# 所以在细读要求之后，更改了上述的版本，非常地贴近ai修改版本。
print("祝你生活愉快")
""" 此下为ai修改版本
age = int(input("请输入你的年龄："))
if 18 <= age <= 30:
    print("你的年龄是符合条件的")
    years = int(input("你的入职时间是多少年："))
    if years >= 2:
        print("您的年龄和入职时间是符合领取条件的，可以领取礼物")
    else:
        level = int(input("抱歉，您的入职时间不符合条件，但是请问你的级别是几级？"))
        if level >= 4 or level == 2:  # 级别大于等于4或者等于2
            print("符合领取条件，可以领取")
        else:
            print("抱歉您无法领取。")
else:
    print("抱歉您无法领取。")

print("祝你生活愉快")
"""
