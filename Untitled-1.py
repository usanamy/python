# 导入所需库
import numpy as np
import matplotlib.pyplot as plt

# -------------------------- 1. 连续信号：余弦信号 --------------------------
# 1.1 定义信号参数
A = 1.0       # 振幅
f = 1.0       # 频率（Hz）
phi = 0.0     # 相位（弧度）
t_start = 0.0 # 时间起点
t_end = 2.0   # 时间终点（2个周期，f=1Hz时周期T=1s）
dt = 0.001    # 采样间隔（足够小，模拟连续信号）

# 1.2 生成连续时间序列和信号值
t_continuous = np.arange(t_start, t_end, dt)
x_continuous = A * np.cos(2 * np.pi * f * t_continuous + phi)

# 1.3 绘制连续余弦信号
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(t_continuous, x_continuous, 'b-', linewidth=1.5)
plt.title('连续信号：余弦信号 $x(t) = \cos(2\pi t)$', fontsize=12)
plt.xlabel('时间 t (s)', fontsize=10)
plt.ylabel('幅值 x(t)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-1.2, 1.2)

# -------------------------- 2. 离散信号：单位冲激信号 --------------------------
# 2.1 定义离散时间序列
n_start = -5
n_end = 5
n_discrete = np.arange(n_start, n_end + 1)  # 离散时间点 n = -5,-4,...,0,...,4,5

# 2.2 生成单位冲激信号：n=0时为1，其余为0
x_discrete = np.zeros_like(n_discrete)
x_discrete[n_discrete == 0] = 1.0

# 2.3 绘制离散单位冲激信号（stem函数专门用于绘制离散信号）
plt.subplot(1, 2, 2)
plt.stem(n_discrete, x_discrete, 'r-', basefmt='k-', use_line_collection=True)
plt.title('离散信号：单位冲激信号 $\delta[n]$', fontsize=12)
plt.xlabel('离散时间 n', fontsize=10)
plt.ylabel('幅值 x[n]', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-0.2, 1.2)
plt.xticks(n_discrete)

# 调整子图间距，显示图像
plt.tight_layout()
plt.show()