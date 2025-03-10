name = "我爱干饭，干饭使我快乐，人是铁饭是钢。"
i = 0
for x in name:
    if x == "饭":
        print(x,end="!\t")
        i += 1
print(f"一共有{i}个饭字")
# print(x+"!\t")