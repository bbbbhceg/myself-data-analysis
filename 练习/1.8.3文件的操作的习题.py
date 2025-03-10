# 我将读取指定的txt文档，然后去统计ithema这个字符串的个数
# 我想用with open打开
# 然后for循环读取每行一的数据
# 因为读取的数据视为字符串个格式，所以直接进行split操作，转化为列表格式，使用count进行计数就OK了
i = 0
count = 0
with open(r"C:\Users\86159\Desktop\文章储备库\数据分析\python学习记录\文件操作测试文档.txt",'r', encoding='UTF-8') as f:
    for line in f:
        i +=1
        count +=line.count("itheima")
        print(f'截止第{i}行，共发现了{count}个"itheima"')

# 反思：我只是记得字符串不可以进行修改，字符串split操作会生成一个列表，列表可以进行count操作
# 但是忘记，字符串是可以进行count操作的。因为它和列表一样都有检测重复数据的需求。
# 中途点字符串的1时候跳出来，才想起来。
'''
完全按照我自己刚开始的思路是行不通的。因为字符串分割变成列表后，位于每行末尾的元素会有\n的干扰。所以只能识别4个。
必须在split之前进行strip()的操作，将开头和结尾的空格和换行符剔除。
i = 0
count = 0
with open(r"C:\\Users\86159\Desktop\文章储备库\数据分析\python学习记录\文件操作测试文档.txt",'r', encoding='UTF-8') as f:
    for line in f:
        word = line.split(' ')
        print(word)
        count +=word.count('itheima')
        print(count)

'''