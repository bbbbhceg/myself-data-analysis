# 读取文件
# 将文件写出到bill.txt.bak文件作为备份
# 同时，将文件内标记为测试的数据行丢弃
# OK，具体目标确立，接下来是实现的路径的规划。
# 为防止忘记，用with打开，as成bill，模式为r
# 使用readlines方法，一次性读取全部内容，赋值变量word
# 再次用with方法打开，路基设置和源文件一样，但是，名字改为bill_back,模式设置成为w,从而在路径下创建该文件
# 然后就是在文件对象bill_back中，用write方法将word写入。
bill =open(r"C:\Users\86159\Desktop\文章储备库\数据分析\python学习记录\文件操作测试文档.txt",'r',encoding='utf-8')
bill2 = open(r"C:\Users\86159\Desktop\文章储备库\数据分析\python学习记录\bill_back.txt", 'w', encoding='utf-8')
bill2.write(str(bill.readlines()))
bill.close()
bill2.close()
# 反思，在我真的先看要求，然后不去看他的解答思路直接去做的时候
# 就是在动手做的时候就发现了，write方法比如要求写入的东西是字符串类型，否则报错。
# 然后，就是读取文件时候，会读取到\n这个事情还是在实际操作的时候，没有考虑到
# 这个导致了在解决了writ这个点，之后成功完成操作，但是检查bill_back这个文档时候，就发现没有换行，且夹杂\n
# 这个文件我就不做修改了，我将另开一个文件解决问题



