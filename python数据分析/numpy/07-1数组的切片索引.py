import numpy

list = [
  [80,89,86,67,79],
  [78,97,89,67,81],
  [90,94,78,67,74],
  [91,91,90,67,69],
  [76,87,75,67,86],
  [70,79,84,67,84],
  [94,92,93,67,64],
  [86,85,83,67,80]
]
list = numpy.array(list)

list_2 = list[2,:3]    # 对第三个列表的前三个元素进行切片，赋予list_2
print(list_2)   # [90 94 78]

list_3 = list[1][:3]   # 对第二个列表的前三个元素进行切片。赋予list_3
print(list_3)   # [78 97 89]

list_4  = list[2,[0,2,4,2,4,0] ] # 访问第3个列表的，下标为0,2,4的三个元素进行访问。
print(list_4)   # [78 97 89]
# list[2,:3] = 99999999  # 多元素批量修改
# 我在此发现切片索引，索引并没有真的copy数值。
# 证据是，在切片之后，不进行立刻打印，而是变动切片处，最后打印切片也会随着变化



#  当数组是数值数组时，可以进行比较运算
xxx = list > 90
print(xxx)
"""
[[False False False False False]
 [False  True False False False]
 [False  True False False False]
 [ True  True False False False]
 [False False False False False]
 [False False False False False]
 [ True  True  True False False]
 [False False False False False]]
"""
aaa = list[list > 90]
print(aaa)  # [97 94 91 91 94 92 93]

