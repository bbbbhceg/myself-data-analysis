# 基础语法：   变量:类型   variety n.种类
import random,json

# 基础数据类型注解
var_1:int   = 10
var_2:float = 3.1415
var_3:bool  = True
var_4:str   = "abc"

# 类对象类型注解
class Student:
    pass

# 构建一个Student的类对象，
stu_1:Student = Student()
# 这表示stu_1这个变量的类型是  Student。不是int，float什么什么类型。

# 基础容器类型注解  也就是简易版
my_list_0:list   = [1,2,3]
my_tuple_0:tuple =(1,2,3)
my_set_0:set     = {1,2,3}
my_dict_0:dict   = {"num":123}
my_str_0:str     = "abcd"

# 容器类型详细注解，详细版
my_list_1:list[int]   = [1,2,3]

# 元组（tuple）类型，设置详细注解时，需要将每一个元素都标记出来
# 如果注解和实际不一致,会警告，但是不会报错耽误调用运行
my_tuple_1:tuple[str,int,bool] =(1,2,3)
my_tuple_2:tuple[str,int,bool] =("abcd",2,True)

my_set_1:set[int]     = {45}
# 字典类型，设置详细注解，需要2个类型，第一个是key第二个是value
my_dict_1:dict[str,int]   = {"num":123}
# my_str:str     = "abcd"   字符串比较特殊
print(my_tuple_1)

# 除了使用变量:类型，这种语法做注解外，也可以在注释中进行类型注解。
# 语法:  # type:类型
# 注释中进行类型注解

class Student_1:
    pass

var_4 = random.randint(1,10)    # type: int
var_5 = json.loads('{"name":"tom"}')  # type: dict[str,str]
def  func():
     return 10
var_6 = func()                        # type: int




