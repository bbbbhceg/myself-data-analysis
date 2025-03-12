# 我将在此进行open方法的r模式无法创建文件对象的错误进行示例
# 以展示捕获异常
try:
    open(r"C:\Users\86159\Desktop\文章储备库\数据分析\python学习记录\捕获异常.txt",'r',encoding='utf-8')
except:
    print('你的模式选择有问题，我已捕获异常')



try:
    print(nickname)
except NameError as a:
    print('你出现了变量未定义的异常，异常的描述如下： %f' %a)

# 这个是%f方法，进一步理解和学习。
'''
try:
    print(nickname)
except NameError as a:
    print(a)   # name 'nickname' is not defined
    print(type(a))  # <class 'NameError'>

    # print('你出现了变量未定义的异常，异常的描述如下： %f' % a)
    # 上一行是有错误的，因为%f 是用来格式化浮点数的，而非格式化所有！！！
'''
# 接下来是如何捕获多个指定异常的练习
'''
try:
    print(1/0)
    print(nickname)
except(NameError,ZeroDivisionError) as b:
    print('出现了变量未定义 或者 除以0的异常错误')
'''

# 这个是，捕获指定异常和捕获所有异常相比，独特应用场景
'''
try:
    # 可能引发多种异常的代码
    result = 10 / 0         # 第一种异常
    # result = 10 / '...'    第二种异常
except ZeroDivisionError:
    print("除数不能为零。")
except TypeError:
    print("类型错误，操作数类型不匹配。")

'''