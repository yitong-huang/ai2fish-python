import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
z = np.cos(x)

# 创建图和坐标系（在后台自动完成）
plt.figure(figsize=(8, 4))            # 创建一个画布，指定大小
plt.plot(x, y, label='y=sin(x)', color='red')  # 在当前坐标系画图
# plt.plot(x, z, label='z=cos(x)')  # 在当前坐标系画图
plt.title('A Simple Sin Wave')        # 设置标题
plt.xlabel('x')                       # 设置x轴标签
plt.ylabel('y')                       # 设置y轴标签
plt.legend()                          # 显示图例
plt.grid(True)                        # 显示网格
plt.show()                            # 显示图形