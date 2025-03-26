# union类型的联合注解
from  typing import  Union

my_list: list[Union[int,str]] = [1,2,"itcast","itheima"]

my_dict: dict[str,Union[str,int]] ={ "name":"周杰轮","age":31}

def func(data: Union[int,str]) -> Union[int,str]:
    pass

func()