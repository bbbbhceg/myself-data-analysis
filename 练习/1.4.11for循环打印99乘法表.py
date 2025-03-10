# 我的目标是用单纯用for循环打印99乘法表。
# 其中乘法表可以看成i*j。每一行内是i逐渐加一，j不变。
# 所以根据上述的分析，外层嵌套是j行，内是i列。
for j in range(1,10): #限定行数是1到9
    for i in range(1,j+1):
        print(f"{i}*{j}={i*j}\t",end="")
    print()
