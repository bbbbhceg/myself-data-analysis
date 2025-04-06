# 生成一个0到10，int类型的三维数组
import numpy
ar1 = numpy.random.randint(0,10,size=(2,3,4))

print(ar1)
print(ar1[1,1,[1,2]])
"""
[[[2 9 7 4]
  [3 0 9 0]
  [8 3 2 4]]

 [[5 6 0 3]
  [6 5 5 7]
  [7 2 8 9]]]
"""