# 第一就是位置参数，这是最原始，最直接的方式
def user_info(name,age,gender):
    print(f"用户的名字是：{name}，年龄是：{age}岁，性别是：{gender}")
user_info("张三",66,"男")

# 关键字参数
user_info(gender = "男",name = "李四",age = 55 )

# 位置参数和关键字参数混合使用,需要注意的是整体位置参数和整体关键字参数之前的前后。
user_info("王二",gender = "女",age = 55)

# 缺省参数的使用
# 需要注意的是，默认参数在定义的时候就要放在最后，否则会报错。
def user_info_2(name,age,gender="男"):
    print(f"用户的名字是：{name}，年龄是：{age}岁，性别是：{gender}")
user_info_2("l",55,)

# 不定长参数的传递---位置参数
def user_info3(*args):
    print(f"args参数的类型是：{type(args)},内容是：{args}")
user_info3('tom',15,True,'MAN',15)
# 不定长参数的传递---关键词参数
def user_info4(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)},内容是：{kwargs}")
user_info4(name = 'jack',age = 55,weight = 66,gender = 'man')