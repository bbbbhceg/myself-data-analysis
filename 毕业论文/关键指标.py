import matplotlib.pyplot as plt
import numpy as np

# 示例数据
support = np.random.rand(20)
confidence = np.random.rand(20)
lift = np.random.rand(20)

# 创建图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制 3D 散点图
scatter = ax.scatter(support, confidence, lift, c=lift, cmap='viridis', marker='o')

# 添加轴标签
ax.set_xlabel('Support')
ax.set_ylabel('Confidence')
ax.set_zlabel('Lift')

# 添加颜色条
cbar = plt.colorbar(scatter)
cbar.set_label('Lift Value')

plt.title('Relationship between Support, Confidence and Lift')
plt.show()