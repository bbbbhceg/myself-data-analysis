"""单一运算符
print("1+1=",1+1)
print("5-3=",5-3)
print("2*3=",2*3)
print("10/2=",10/2)
print("10/2=",10//2,"整除版本")
print("11%3=",11%3)
print("12%3=",12%3)
print("4**3=",4**3,"指数")
"""
# 复合运算符
thenum = 1+3*5-14
num = 1
num += 1
print("num += 1:",num)
num -= 1
print("num -= 1:",num)
num *= 8
print("num *= 8:",num)
num /= 3
print("num /= 3:",num)
num %= 1 # 8/3=2.67 2.67%1=0.67（2.67除以1得到的余数）
print("num %= 1:",num)
num = 5
num **= 3
print("num **= 3:",num)
num //=3
print("num //= 3:",num)
