import pandas as pd
s=pd.Series({
    '语文':100,
    '数学':150,
    '英语':110,
    'Python': 130,
    'Pandas': 150,
    'NumPy': 150
})

#切片
# Series是—维数组
#隐式切片:左闭右开s[1:4]
a = s.iloc[1 :4]
print(a)
#显式切片:左闭右闭
b = s['数学':'Python']
print(b)
c = s.loc['数学': 'Python']
print(c)

