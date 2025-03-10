"""
Name1 = "张三"+"wwww"
address = "西湖%s"%Name1
weight = "75"
print("他的名字是：",Name1,"我常常看见他，出现在"+address)
print("他的名字是：",Name1,"我常常看见他")
print("他的名字是：",Name1+"我常常看见他")
# 当变量存储的是纯数字，则变量和字符串之间无法用+拼接。将数字，字符串化就好。
print("他的名字是："+Name1+"，我常常看见他出现在"+address+"，体重是："+weight)
"""
"""
int_number = 11
float_number = float(int_number)
print(type(type(float_number)))   # 结果会显示<class 'type'>
print((((type(float_number)))))  # 此行会触发弱警告，但不会影响输出。
"""
num5 = 1
num5 += 1
print(num5)
text1 = "baxa + 22"