import numpy as np
import matplotlib.pyplot as plt

# 设置参数
frequency = 1  # 频率
sampling_rate = 100  # 采样率
duration = 2  # 持续时间（秒）

# 生成时间轴
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# 生成正弦波
y = np.sin(2 * np.pi * frequency * t)

# 绘制图形
plt.figure(figsize=(10, 4))
plt.plot(t, y, label='Sine Wave', color='b')
plt.title('Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()