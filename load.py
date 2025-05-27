import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

# 设置 matplotlib 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False  # 负号显示

# 加载 WAV 文件
audio_filename = 'zrk_audio.wav' #正常录音完成后是.m4a文件，用这个网站可以转https://convertio.co/zh/m4a-wav/

y, sr = librosa.load(audio_filename, sr=None) # sr=None 保留原始采样率
print(f"音频文件 '{audio_filename}' 加载成功，采样率: {sr} Hz，时长: {len(y)/sr:.2f} 秒")
print(f"声道数: {1 if y.ndim == 1 else y.shape[0]}")
# 绘制波形图
plt.figure(figsize=(12, 6))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.xlabel("时间 (秒)")
plt.ylabel("幅度")
plt.grid()
plt.show()