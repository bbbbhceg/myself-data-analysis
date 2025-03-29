"""
文件相关的类的定义
在这个类中定义三个类，一个父类，两个子类
三个类中只有一个读取数据的操作，不过因为读取数据的格式不同，所以有些许的区别

两个子类，所实现的功能是，接收文件路径，然后进行处理，期间巧妙使用data_define中的Record返回字典嵌套列表的那种标准json格式
"""
import json
from data_define import Record

# 先定义一个抽象类，用来做顶层设计，确定有哪些功能需要实现
class FileReader:
    def read_data(self):
        # 读取文件的数据，读到的每一条数据都转换为Record对象，将他们都封装到list内返回即可
        pass

# 子类1，用于实际读取文本格式的数据，也就是1月数据
class TextFileReader(FileReader):
    def __init__(self,path):        # 这段代码的存在，使得调用该类时，只用输入文件路径即可
        self.path = path            # 定义成员变量，记录输入文件的路径

    # 复写（用以实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="utf-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()   # 消除读取到的每一行数据中的\n
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)
        f.close()

        return  record_list

# 子类2，用于实际读取伪json格式，也就是二月数据
class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path    # 定义成员变量，记录文件的路径

    # 复写（用以实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")

        record_list:list[Record] = []      # 定义一个空列表
        for line in f.readlines():          # readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素会附带换行符。
            data_dict = json.loads(line)   # 转变为python格式。（源数据整体并不是json格式，但是readlines读取之后的单个元素是json格式，所以可以进行单行的json.loads转换。）
            record = Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)
        f.close()
        return  record_list
if __name__ == '__main__':
    text_file_reader = TextFileReader(r"D:\Program Files\黑马练习数据\2011年1月销售数据.txt")
    json_file_reader = JsonFileReader(r"D:\Program Files\黑马练习数据\2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:        # 如果data_define中不使用__str__魔术方法，则输出的值只会是：<data_define.Record object at 0x0000020B3D065480>
        print(l)           # 这样的内存地址   ，下方这个for循环也是一样的

    for l in list2:
        print(l)