# from 变量 import *
# num()
# say_hi()

# 虽然没有讲，但是，意外发现了模块的导入，调入函数的机制，即先将模块整体运行一遍
# 这样做的目的是，防止调用的函数用到全局变量，如果没有提前运行，则会无法正常使用的场景

import my_module as f
# 不用*，而是这样导入自定义模组全部，__all__的用法就不会生效
f.test_a()
f.test_b()
import tom.tom1
tom.tom1.say_hi()
tom.tom1.hollow()
# 或者可以用from语句
from tom import tom2
tom2.learn()
tom.tom2.learn

