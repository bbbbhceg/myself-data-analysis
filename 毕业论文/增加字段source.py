# 读取文件1
with open(r"C:\Users\86159\Desktop\毕业论文\1.5.1无source测试.txt", 'r', encoding='ansi') as file1:
    lines = file1.readlines()

# 处理每一行并转换为文件2的格式
output_lines = []
for line in lines:
    line = line.strip()  # 去除每个元素的\n
    if line.startswith('keyword:'):
        # 提取关键词部分
        keywords = line[8:].strip()  # 去掉"keyword:"前缀
        # 组合成文件2的格式
        output_lines.append('source')
        output_lines.append(f'keyword: {keywords}')
        output_lines.append('')  # 添加空行分隔记录

# 写入转换后的内容到新的文件
with open("C:\\Users\86159\Desktop\毕业论文\outputPython处理后.txt", 'w', encoding='ansi') as output_file:
    output_file.write('\n'.join(output_lines))

print("转换完成，结果已保存到 output.txt")