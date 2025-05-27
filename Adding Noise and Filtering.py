import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import librosa
import numpy as np
from scipy.io import wavfile  # 导入用于保存 WAV 文件的模块
# 导入 IIR 和 FIR 滤波器设计函数
from IIR_filter import design_iir_filter
from FIR_filter import design_fir_filter

# 设置 matplotlib 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False  # 负号显示

# 加载 WAV 文件并提取原始采样率
audio_filename = 'your_audio.wav'
y, sr = librosa.load(audio_filename, sr=None) 

# 生成高斯白噪声
noise_power = 0.005  # 噪声功率，可以调整
noise = np.random.normal(0, np.sqrt(noise_power), len(y))
y_noisy = y + noise

# 保存含噪音频
wavfile.write('.\\wav\\audio_noisy.wav', sr, (y_noisy * 32767).astype(np.int16))
print("已保存含噪音频到 audio_noisy.wav")

# 选择要处理的信号
signal_to_filter = y_noisy 
print("使用含噪信号进行滤波" if np.array_equal(signal_to_filter,y_noisy) else "使用原始信号进行滤波")

# 绘制含噪信号时域波形和频谱
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
librosa.display.waveshow(signal_to_filter, sr=sr)
plt.title('含噪/待滤波语音信号时域波形')
plt.xlabel('时间 (秒)')
plt.ylabel('幅度')
plt.grid(True)

N_noisy = len(signal_to_filter)
Y_noisy = np.fft.fft(signal_to_filter)
freq_noisy = np.fft.fftfreq(N_noisy, d=1/sr)
positive_freq_indices_noisy = np.where(freq_noisy >= 0)
positive_frequencies_noisy = freq_noisy[positive_freq_indices_noisy]
positive_Y_magnitude_noisy = np.abs(Y_noisy[positive_freq_indices_noisy])

plt.subplot(2, 1, 2)
plt.plot(positive_frequencies_noisy, positive_Y_magnitude_noisy)
plt.title('含噪/待滤波语音信号频谱图')
plt.xlabel('频率 (Hz)')
plt.ylabel('幅度')
plt.xlim(0, sr/2)
plt.grid(True)
plt.tight_layout()
plt.show()

# --- 4.1 设计 IIR 和 FIR 滤波器 ---
# IIR 滤波器参数
filter_type_iir = 'lowpass'
cutoff_freq_iir = 5000
order_iir = 4
# 调用 IIR 滤波器设计函数
b_iir, a_iir, filter_desc_iir = design_iir_filter(sr, filter_type_iir, cutoff_freq_iir, order_iir)

# FIR 滤波器参数
filter_type_fir = 'lowpass'
numtaps_fir = 101
cutoff_freq_fir = 5000
lowcut_fir = 500
highcut_fir = 2500
# 调用 FIR 滤波器设计函数
b_fir, a_fir, filter_desc_fir, cutoff_freq_fir, lowcut_fir, highcut_fir = design_fir_filter(sr, filter_type_fir, numtaps_fir, cutoff_freq_fir, lowcut_fir, highcut_fir)

# 应用 IIR 滤波器 ---
y_filtered_iir = signal.lfilter(b_iir, a_iir, signal_to_filter)
# 应用 FIR 滤波器 ---
y_filtered_fir = signal.lfilter(b_fir, a_fir, signal_to_filter)

# 绘制 IIR 滤波后的时域波形和频谱 ---
print(f"\n--- {filter_desc_iir} 滤波后 ---")
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
librosa.display.waveshow(y_filtered_iir, sr=sr)
plt.title(f'经过 {filter_desc_iir} 滤波后的时域波形')
plt.xlabel('时间 (秒)')
plt.ylabel('幅度')
plt.grid(True)

N_filtered_iir = len(y_filtered_iir)
Y_filtered_iir = np.fft.fft(y_filtered_iir)
freq_filtered_iir = np.fft.fftfreq(N_filtered_iir, d=1/sr)
pos_idx_iir = np.where(freq_filtered_iir >=0)
pos_freq_iir = freq_filtered_iir[pos_idx_iir]
pos_Y_mag_iir = np.abs(Y_filtered_iir[pos_idx_iir])

plt.subplot(2, 1, 2)
plt.plot(pos_freq_iir, pos_Y_mag_iir)
plt.title(f'经过 {filter_desc_iir} 滤波后的频谱图')
plt.xlabel('频率 (Hz)')
plt.ylabel('幅度')
plt.xlim(0, sr/2)
plt.grid(True)
plt.tight_layout()
plt.show()

# 绘制 FIR 滤波后的时域波形和频谱 ---
print(f"\n--- {filter_desc_fir} 滤波后 ---")
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
librosa.display.waveshow(y_filtered_fir, sr=sr)
plt.title(f'经过 {filter_desc_fir} 滤波后的时域波形')
plt.xlabel('时间 (秒)')
plt.ylabel('幅度')
plt.grid(True)

N_filtered_fir = len(y_filtered_fir)
Y_filtered_fir = np.fft.fft(y_filtered_fir)
freq_filtered_fir = np.fft.fftfreq(N_filtered_fir, d=1/sr)
pos_idx_fir = np.where(freq_filtered_fir >=0)
pos_freq_fir = freq_filtered_fir[pos_idx_fir]
pos_Y_mag_fir = np.abs(Y_filtered_fir[pos_idx_fir])

plt.subplot(2, 1, 2)
plt.plot(pos_freq_fir, pos_Y_mag_fir)
plt.title(f'经过 {filter_desc_fir} 滤波后的频谱图')
plt.xlabel('频率 (Hz)')
plt.ylabel('幅度')
plt.xlim(0, sr/2)
plt.grid(True)
plt.tight_layout()
plt.show()

# 保存滤波后的音频
# wavfile.write('audio_filtered_iir.wav', sr, (y_filtered_iir * 32767).astype(np.int16))
# wavfile.write('audio_filtered_fir.wav', sr, (y_filtered_fir * 32767).astype(np.int16))