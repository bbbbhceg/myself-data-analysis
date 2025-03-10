# 语法1:
# range(num)
# 获取一个从0开始，到Num结束的数字序列(不含Num本身)如Range(5)取得的数据是：[0，1，2，3，4]
# for x in range(10):
#     print(x,"1")
# 语法2:
# range(num1, num2)
# 获得一个从num1开始，到num2结束的数字序列（不含num2本身)如，range(5,10)取得的数据是:[5,6,7,8,9]
# for x in range(-3,10):
#     print(x,"2")
# 语法3:
# range(num1, num2, step)
# 获得一个从num1开始，到num2结束的数字序列（不含num2本身)数字之间的步长，以step为准( step默认为1)
# 如，range(5,10,2)取得的数据是:[5,7,9]
# for x in range(5,10,2):
#     print(x,"3")
""""""
# 我将进行有几个偶数的练习
# 要求是，用for循环和range，计算右多少偶数，并将结果进行输出。
i = 0
for x in range(0,101,2):
    i += 1
# 因为0不算，所以下一行要减掉1，虽然它符合定义
print(f"0到100（包含）一共有{i-1}个偶数","，我真(づ｡◕‿‿◕｡)づ"+"厉害捏%d。" % 666,"。")
count = 0
for x in range(1,101):
    if x % 2 == 0:
        count += 1
print(f"{count}")