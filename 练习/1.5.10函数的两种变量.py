num = 100
def fun_a ():

    print(num)
def fun_b ():
    global num
    num = 200
    print(num)
def fun_c():
    print(num)
fun_a()
fun_b()
fun_c()
print(num)