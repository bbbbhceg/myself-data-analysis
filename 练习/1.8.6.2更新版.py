# 在这个文件内，我将解决，备份格式和原格式不一致的问题
# 上一个文档的问题：格式不一致→\n未处理好      所以我将使用for循环，加上readline
# 我将存入bill_back2的文件。
bill =open(r"C:\Users\86159\Desktop\文章储备库\数据分析\python学习记录\文件操作测试文档.txt",'r',encoding='utf-8')
bill2 = open(r"C:\Users\86159\Desktop\文章储备库\数据分析\python学习记录\bill_back2.txt", 'w', encoding='utf-8')
for line in bill:
    line = line.strip() # 将line进行规整后重新赋值本身
    # if line.split(',')[4]== "测试"        可以用这个语句将测试和正式的分开
    bill2.write(line)
    bill2.write('\n')
bill.close()
bill2.close()

