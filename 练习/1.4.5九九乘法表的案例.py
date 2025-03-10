# 我的目的是输出阶梯式的九九乘法表
# 这是两层循环。每一行算一次循环。行数和a*b的b有关
j = 1
while j < 10: # 控制行数
    i = 1
    while i  <= j:
        print(f"{i}*{j}={i*j}\t",end='')
        i += 1
    j += 1
    print()
print("已经结束")