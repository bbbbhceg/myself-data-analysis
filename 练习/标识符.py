# 规则1：内容限定，限定只能使用：中文，英文，下划线(_),注意：不能以数字开头
# 错误示范之数字开头 1_name = "张三"
# 错误示范之使用非法符号 name_! = "李四"
"""
name1 = "zhangsan"
print(name1)
# 规则2：大小写是敏感的,也就是不会混淆大小写的标识符
"""
"""
Wzbb = 666
wzbb = 999
print(wzbb)
print(Wzbb)
"""
# 规则3：不可使用关键字
"""
print = 1
print(print)
像是上述这样占用关键字 print就会报错
"""
