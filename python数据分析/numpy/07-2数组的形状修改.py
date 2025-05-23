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

#  使用reshape修改元素数据的顺序没有变化，变化的只是形状。
list2 = list.reshape(5,8)
# print(list2)
"""
[[80 89 86 67 79 78 97 89]
 [67 81 90 94 78 67 74 91]
 [91 90 67 69 76 87 75 67]
 [86 70 79 84 67 84 94 92]
 [93 67 64 86 85 83 67 80]]
"""

# 使用resize方法发现它修改的是源数据,这是它唯一区别于reshape的方法
# list3 = list.resize((5,8))
# print(list3)   # 返回 None
# print(list)
"""
[[80 89 86 67 79 78 97 89]
 [67 81 90 94 78 67 74 91]
 [91 90 67 69 76 87 75 67]
 [86 70 79 84 67 84 94 92]
 [93 67 64 86 85 83 67 80]]
"""

# 数组的转置T（已经注释resize）
list4 = list.T
print(list4)
print(list4.shape)  # (5, 8)