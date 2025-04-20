def convert_format(input_path):
    output_path = input_path.replace(".txt", "_转换后.txt")

    # 获取源文件编码（假设为GBK）
    with open(input_path, 'r', encoding='gbk') as f_in, \
            open(output_path, 'w', encoding='gbk') as f_out:  # 保持与源文件相同编码

        buffer = []
        for line in f_in:
            # 识别keyword块起始
            if line.startswith("keyword:"):
                if buffer:  # 处理前一个块
                    process_block(buffer, f_out)
                buffer = [line.strip('\n')]  # 初始化新块
            elif line.strip().endswith(',') and buffer:
                buffer.append(line.strip('\n'))
            else:
                if buffer:
                    buffer.append(line.strip('\n'))

        # 处理最后一个块
        if buffer:
            process_block(buffer, f_out)


def process_block(buffer, f_out):
    """处理单个keyword块并写入文件"""
    # 合并跨行内容
    merged = ' '.join(buffer).replace(' ,', ',').replace(', ', ',')

    # 提取元素并规范格式
    elements = [e.strip() for e in merged[len("keyword: "):].split(',') if e.strip()]
    cleaned = "keyword: " + ', '.join(elements).rstrip(',')

    # 写入规范格式
    f_out.write("source\n")
    f_out.write(cleaned + "\n\n")  # 块间空一行


# 使用示例（注意原始字符串）
input_file = r"C:\Users\86159\Desktop\毕业论文\test\新建 XLS 工作表aaa.txt"
convert_format(input_file)