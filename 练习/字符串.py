name = 'zfc'
name1 = "zfc"
name2 = """1333"""
name3 = """w
s
z
f
c"""
print(type(name3))
print(name3)
print(type(name2))
print(type(name1))
print(type(name))
# 当字符串内含有双引号，用单引号定义
name4 = '它是"yuan"'
print(type(name4))
# 当字符串内含有单引号，用双引号定义
name5 = "他是'monkey'"
print(type(name5))
# 也可以使用 \ 解除引号的效果,这样，单引号，双引号，三引号就可以随意用了。
name6 = "\"monkey\"是它"  # 可以注解除一个双引号，也可以均解除掉，为了规范，要全解除掉
print(name6,"name6")
name7 = '他有\'五元\''
print(name7)
