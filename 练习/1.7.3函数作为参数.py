# 如果不使用函数作为参数进行数据的分析111111111111111111111111111111111
# 假设我们有一组数据
data = [10, 20, 30, 40, 50]

# 求和
def sum_data(data):
    return sum(data)

result_sum = sum_data(data)
print(f"Result of sum_data: {result_sum}")

# 求平均值
def average_data(data):
    return sum(data) / len(data)

result_average = average_data(data)
print(f"Result of average_data: {result_average}")

# 求最大值
def max_data(data):
    return max(data)

result_max = max_data(data)
print(f"Result of max_data: {result_max}")

#  使用函数作为参数进行数据分析的版本22222222222222222222222222222222222222222222222
# 假设我们有一组数据
data = [10, 20, 30, 40, 50]

# 定义一个通用的数据处理函数
def process_data(data, operation):
    result = operation(data)  # 调用传入的操作函数
    print(f"Result of {operation.__name__}: {result}")

# 定义不同的操作函数
def sum_data(data):
    return sum(data)

def average_data(data):
    return sum(data) / len(data)

def max_data(data):
    return max(data)

# 使用通用函数处理数据
process_data(data, sum_data)    # 求和
process_data(data, average_data)# 求平均值
process_data(data, max_data)    # 求最大值