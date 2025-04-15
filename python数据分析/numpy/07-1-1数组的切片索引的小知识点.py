import numpy
numpy.random.seed(1)
data = numpy.random.randint(1,10,size = (5,4))
print("第0次输出：",data)
"""
[[6 9 6 1]
 [1 2 8 7]
 [3 5 6 3]
 [5 3 5 8]
 [8 2 8 1]]
"""
print("第1次输出：",data[::,[-2,-1]])
"""
[[6 1]
 [8 7]
 [6 3]
 [5 8]
 [8 1]]
"""
print("第2次输出：",data[::,2:])
""""
[[6 1]
 [8 7]
 [6 3]
 [5 8]
 [8 1]]
"""
print("第3次输出：",data[:][[-2,-1]])
# 这个相当于data【【-2,1】】依然是仅仅对第一维度进行操作
"""
[[5 3 5 8]
 [8 2 8 1]]
"""
print("第4次输出：",data[:][-2,-1])  # 8
print("第5次输出：",data[-2,-1])     # 8
print("第5次输出：",data[:][:][:][:][:][-2,-1])  # 8
# 单纯的[:]几乎相当于没写。
# 因为是从list演进来的。所以要从源头看看。也要从维度的角度看看。