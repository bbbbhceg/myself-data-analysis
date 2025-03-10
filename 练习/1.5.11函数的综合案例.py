# 我要按照1.5.11的视频50秒的样子做一个atm菜单
# 第一，我需要先将样子写出来，在完善功能。
# 第二，因为涉及函数内更改函数外变量，所以要用到global关键字和多个函数的调用
# 第三，一共有四个选择，也就是最起码得做四个函数
money = 100000 #一共十万
name = input("请输入您的名称")
print()
# 取钱函数
def withdraw():
    global money
    print(f"------------取款------------\n欢迎您使用取款功能，当前账户余额剩余：{money}元")
    count = int(input("请入您需要取出多少？"))
    if count > money:
        print("抱歉，您的账户余额不足")
    else:
        money = money - count
    print(f"好的，{name}，当前账户余额还剩余：{money}元")

# 存钱函数
def saving():
    global money
    print(f"------------存款------------\n欢迎您使用存钱功能，当前账户余额剩余：{money}元")
    money = money +  int(input("请入您需要取出多少？"))
    print(f"好的，{name}，当前账户余额还剩余：{money}元")

# 余额函数
def balance():
    print(f"------------余额------------\n好的，{name}，当前账户余额还剩余：{money}元")


while True:
    choose = input(f"------------主菜单------------\n{name}，您好，欢迎来到ATM的主菜单，请选择操作\n查询余额\t【输入1】\n存款\t\t【输入2】\n取款\t\t【输入3】\n退出\t\t【输入4】\n请输入您的选择：")
    if choose == "3":
        withdraw()
    elif choose == "2":
        saving()
    elif choose == "1":
        balance()
    else:
        print("程序已退出，祝您生活愉快")
        break
    continue
# 这个程序符合题目的要求，但是没有防呆涉及，一旦在该输入数字的时候输入字符串，则会异常。
# 好的，现在已经修改完毕了，在菜内，进行了防呆设计，但是函数内没有进行防呆设计。
# 另外惊讶的是，视频教学，if条件判断是比较的字符串而非数字，这样就可以不多费一行的解决主菜单的防呆设计了！
