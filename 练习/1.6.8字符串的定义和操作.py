# 我要定义一个字符串，进行操作尝试
test1 = "1,2.22,'你好'，True"
index = test1.index("2,'")
print(index)  # 返回的数值是5
new_test = test1.replace(",","替换元素")
print(new_test)
# ↑输出的结果：1替换元素2.22替换元素'你好'，True

# 字符串数据容器独属的split的方法测试
new_list = test1.split(",")
print(new_list)  # 输出['1', '2.22', "'你好'，True"]
print(type(new_list)) # 输出<class 'list'>

# 字符串数据容器独属的strip的方法测试
test2 = "    gan fan zhen kai xin   " # 开头和结尾都有四个空格
# 当不传入参数时，就默认参数为取出开头结尾和空格
# 而且，要时刻谨记，字符串只读，strip是生成一个新字符串
new_str = test2.strip()
print(f"未处理之前是{test2}，操作之后是{new_str}")
# ↑输出的结果是↓
# 未处理之前是    gan fan zhen kai xin   ，操作之后是gan fan zhen kai xin


