# 我要先准备一个txt文档，OK名字叫文档操作测试文档
# f = open(r"C:\Users\86159\Desktop\文章储备库\数据分析\python学习记录\文件操作测试文档.txt",'r', encoding='UTF-8')
# 测试文件类型
# print(type(f))   # <class '_io.TextIOWrapper'>
'''
# 文件对象.read(num)方法进行读取
word = f.read(6)
print(word)
print(f.read())
word = f.read(6)
'''
# 文件对象.readlines(num)方法进行读取
# print(f.readlines())

# 文件对象.readline()的测试
# print(f.readline())   # 没有参数的输入，自然会进行整行整行的读取。
# print(f.readline(6))    # 如果没有临近上一行的操作的话，会和read()一样的输出结果
'''
# for循环的操作与文件读取的结合
for x in f :
    print("每一行的数据是：",x)
'''



with open(r"C:\Users\86159\Desktop\文章储备库\数据分析\python学习记录\文件操作测试文档.txt",'r', encoding='UTF-8') as f:
    '''
    在这里边，进行read，readlines，readline都可以
    且执行完毕后，会自动关闭文件对象
    '''

####
"""
i = 0
with open(r"C:\\Users\86159\Desktop\文章储备库\数据分析\python学习记录\文件操作测试文档.txt",'r', encoding='UTF-8') as f:
    for x in f :
        if x == '123456789\n':
            i += 1
            print(f"叭叭叭{i}")
# 在这个程序内，我需要注意的是
# 第一，x每次读取文件都是视为字符串格式的
# 第二，x每次读取的长度是一行，且是含有隐含的\n的

"""