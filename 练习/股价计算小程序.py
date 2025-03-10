name = "地球公司"
stock_price = 11
stock_code = 12931
stock_price_daliy_growth_factor = 1.248
growth_days = 12
# 要求1.计算并输出经过12天的增长后，股价达到了多少前钱
# 要求2.使用字符串格式化进行输出，如果是浮点数，要求小数点精度2位数。
print(f"公司名称是：{name}，这个公司的股票代码是：{stock_code}，当前股价是：{stock_price}")
print("每日增长系数是：%.2f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daliy_growth_factor,growth_days,(11 *(1.248**12 ))))
# 如果觉得这个最后一个输出函数括号太多，可以将最后一个计算式子提前存入一个变量,例如:
finala = stock_price *  stock_price_daliy_growth_factor ** growth_days
print("每日增长系数是：%.2f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daliy_growth_factor,growth_days,finala))