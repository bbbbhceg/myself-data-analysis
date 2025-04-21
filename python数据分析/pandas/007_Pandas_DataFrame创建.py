# 介绍学习DataFrame
# DataFrame是一个【表格型】的数据结构，可以看做是【由Series组成的字典】(共用同一个索引)。
# DataFrame由按一定顺序排列的多列数据组成。设计初衷是将Series的使用场景从一维拓展到多维。DataFrame既有行索引，也有列索引。
# ·行索引: index
# ·列索引: columns
# ·值: values (NumPy的二维数组)
import pandas
import numpy
