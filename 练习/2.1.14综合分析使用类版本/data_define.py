"""
数据定义的类
"""

class Record :
    """
    每一条一月份的数据，就可以划分为日期，订单号，销售额，省份四个部分
    又因为，这个四个部分都是必须的，所以使用init魔术方法，将四个参数放入
    、；颗粒剂哦莱卡棉，。，。
    """
    def __init__(self,date,order_id,money,province):
        self.date = date            # 订单日期
        self.order_id = order_id    # 订单ID
        self.money = money          # 订单金额
        self.province = province    # 订单省份

    def __str__(self):
        return f"{self.date},{self.order_id},{self.money},{self.province}"