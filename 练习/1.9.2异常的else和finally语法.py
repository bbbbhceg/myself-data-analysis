# 在这个文件内，我要进行异常else和finally的测试。
try:
    print(1)
except Exception as a:
    print(a)
else:
    print('出现此结果，说明程序运作正常，没有异常出现')

# 以下是finally的示例
# try:
#     f = open('abcd.txt','r')
# except Exception as a:   # 提示：子句过于宽泛:11
#     f = open('abcd.txt','w')
#     # 直接在此文件路径下，新建了目标文件对象
# else:
#     print('到此为止，没有异常')
# finally:
#     f.close()   # 这里提示：名称'f可能未定义:17
