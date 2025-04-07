import numpy as np

arr_1 = np.random.randint(0,10,size=(6,6))
print("创建一个（6,6）形状的数组\n",arr_1)
"""
 [[5 7 6 6 7 0]
 [8 2 7 9 4 5]
 [0 2 0 2 4 7]
 [4 4 5 8 5 7]
 [4 1 8 2 8 1]
 [3 7 9 4 8 6]]
"""
# 直接指定切割的份数。
arr_2 = np.split(arr_1,indices_or_sections=2,axis=0)  # 默认数值是0 行分离。又因为行与行之间是垂直堆叠，所以使用vsplit
print("split关键词，axis是默认值0的情况\n",arr_2)
"""
[array([[5, 7, 6, 6, 7, 0],
       [8, 2, 7, 9, 4, 5],
       [0, 2, 0, 2, 4, 7]], dtype=int32), array([[4, 4, 5, 8, 5, 7],
       [4, 1, 8, 2, 8, 1],
       [3, 7, 9, 4, 8, 6]], dtype=int32)]
"""
arr_3 = np.vsplit(arr_1,indices_or_sections=2)
print("vsplit，等同于默认是0的情况\n",arr_3)
"""
 [array([[5, 7, 6, 6, 7, 0],
       [8, 2, 7, 9, 4, 5],
       [0, 2, 0, 2, 4, 7]], dtype=int32), array([[4, 4, 5, 8, 5, 7],
       [4, 1, 8, 2, 8, 1],
       [3, 7, 9, 4, 8, 6]], dtype=int32)]
"""
arr_4 = np.hsplit(arr_1,indices_or_sections=2)
print("hsplit等同于默认值是1的情况\n",arr_4)
"""
 [array([[5, 7, 6],
       [8, 2, 7],
       [0, 2, 0],
       [4, 4, 5],
       [4, 1, 8],
       [3, 7, 9]], dtype=int32), array([[6, 7, 0],
       [9, 4, 5],
       [2, 4, 7],
       [8, 5, 7],
       [2, 8, 1],
       [4, 8, 6]], dtype=int32)]
"""