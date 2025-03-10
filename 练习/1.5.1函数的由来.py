# 引例，计算指定三个字符串的长度
str1 = "abcdef"
str2 = "breakaway1watchman"
str3 = "aabbcc"
# count = 0
# for i in str1 :
#     count +=1
# print(f"字符串{str1}的长度是:{count}")
#
# count = 0
# for i in str2 :
#     count +=1
# print(f"字符串{str2}的长度是{count}")
#
# count = 0
# for i in str3 :
#     count +=1
# print(f"字符串{str3}的长度是{count}")
"""
# 反思，我在第一次操作中，将count和i都写成了i
# 导致在“count +=1”的操作中出现了数字和字符串的相加
# 所以程序直接报错。我几番修改，最后还是问的ai才知道的结果。
"""
# 这三个计算指定字符串长度的程序，长得非常相似
# 那如果我们不想一遍遍的写，该怎么办？
# 这就引出了函数。如下所示.我已经把上三个注释掉了
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是：{count}")
my_len(str1)
my_len(str2)
my_len(str3)
