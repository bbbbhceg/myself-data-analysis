# 我将在这个文件内，进行函数多返回值的测试。
def test_return():
    return 1,2,3,{1:"nihao"},"nihao",[1,True],(55,"niaho")
x = test_return()
print(x)
# ↑结果：(1, 2, 3, {1: 'nihao'}, 'nihao', [1, True], (55, 'niaho'))

print(type(x))
# ↑结果：<class 'tuple'>
"""
def test_return():
    return 1,2,"nihao",[55,"niaho"],(555,"nihao"),{1,2,3,4},{"nihao":1}
x,y,z,a,b,c,e= test_return()
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(e))
会正确识别类型
"""


