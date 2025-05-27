import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import librosa
import numpy as np

# 设置 matplotlib 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False  # 负号显示
# 加载 WAV 文件并提取原始采样率
audio_filename = 'your_audio.wav'
y, sr = librosa.load(audio_filename, sr=None) 

def design_fir_filter(sr, filter_type_fir='lowpass', numtaps_fir=101, cutoff_freq_fir=3000, lowcut_fir=500, highcut_fir=2500):
    """
    设计 FIR 滤波器并返回滤波器系数和描述。

    参数:
        sr (int): 采样率。
        filter_type_fir (str): 滤波器类型，'lowpass', 'highpass', 'bandpass', 'bandstop'。
        numtaps_fir (int): FIR 滤波器的阶数 (抽头数)，应为奇数以保证线性相位. 默认为101.
        cutoff_freq_fir (int): 截止频率 (用于低通和高通滤波器)。
        lowcut_fir (int): 低截止频率 (用于带通和带阻滤波器)。
        highcut_fir (int): 高截止频率 (用于带通和带阻滤波器)。

    返回:
        tuple: 包含滤波器系数 (b, a) 和滤波器描述的元组。
    """
    # 确保 numtaps 是奇数
    if numtaps_fir % 2 == 0:
        numtaps_fir += 1

    if filter_type_fir == 'lowpass':
        # 归一化截止频率 (对于 firwin，截止频率是相对于奈奎斯特频率 sr/2)
        nyq_rate = sr / 2.0
        normalized_cutoff_fir = cutoff_freq_fir / nyq_rate
        b_fir = signal.firwin(numtaps_fir, normalized_cutoff_fir, window='hamming')
        a_fir = 1.0 # FIR 滤波器的 a 系数总是1
        filter_desc_fir = f'FIR 低通滤波器 (Hamming窗, 阶数={numtaps_fir-1}, 截止频率={cutoff_freq_fir}Hz)'
    elif filter_type_fir == 'highpass':
        cutoff_freq_fir = 1000  # Hz
        nyq_rate = sr / 2.0
        normalized_cutoff_fir = cutoff_freq_fir / nyq_rate
        b_fir = signal.firwin(numtaps_fir, normalized_cutoff_fir, window='hamming', pass_zero=False)
        a_fir = 1.0
        filter_desc_fir = f'FIR 高通滤波器 (Hamming窗, 阶数={numtaps_fir-1}, 截止频率={cutoff_freq_fir}Hz)'
    elif filter_type_fir == 'bandpass':
        lowcut_fir = 500   # Hz
        highcut_fir = 2500 # Hz
        nyq_rate = sr / 2.0
        normalized_band_fir = [lowcut_fir / nyq_rate, highcut_fir / nyq_rate]
        b_fir = signal.firwin(numtaps_fir, normalized_band_fir, window='hamming', pass_zero=False)
        a_fir = 1.0
        filter_desc_fir = f'FIR 带通滤波器 (Hamming窗, 阶数={numtaps_fir-1}, 通带={lowcut_fir}-{highcut_fir}Hz)'
    else: # bandstop
        lowcut_fir = 1000  # Hz
        highcut_fir = 1500 # Hz
        nyq_rate = sr / 2.0
        normalized_band_fir = [lowcut_fir / nyq_rate, highcut_fir / nyq_rate]
        b_fir = signal.firwin(numtaps_fir, normalized_band_fir, window='hamming', pass_zero=True)
        a_fir = 1.0
        filter_desc_fir = f'FIR 带阻滤波器 (Hamming窗, 阶数={numtaps_fir-1}, 阻带={lowcut_fir}-{highcut_fir}Hz)'
    
    return b_fir, a_fir, filter_desc_fir, cutoff_freq_fir, lowcut_fir, highcut_fir

if __name__ == "__main__":
    # 调用test
    # 加载 WAV 文件并提取原始采样率 (如果 sr 不是全局变量，需要在这里重新加载或传递)
    # audio_filename = 'zrk_audio.wav' 
    # y_test, sr_test = librosa.load(audio_filename, sr=None) 

    filter_type_fir = 'lowpass'
    numtaps_fir = 101
    cutoff_freq_fir = 3000
    lowcut_fir = 500
    highcut_fir = 2500
    # 确保 sr 在这里是可用的，如果它是在模块顶部定义的，那么这里可以直接使用
    b_fir, a_fir, filter_desc_fir, cutoff_freq_fir, lowcut_fir, highcut_fir = design_fir_filter(sr, filter_type_fir, numtaps_fir, cutoff_freq_fir, lowcut_fir, highcut_fir)

    # 计算并绘制频率响应
    w_fir, h_fir = signal.freqz(b_fir, a_fir, worN=8000, fs=sr)

    plt.figure(figsize=(10, 5))
    plt.plot(w_fir, np.abs(h_fir), 'g')
    plt.title(f'{filter_desc_fir} - 幅度响应')
    plt.xlabel('频率 (Hz)')
    plt.ylabel('幅度增益')
    plt.grid(True)
    if filter_type_fir == 'lowpass' or filter_type_fir == 'highpass':
        plt.axvline(cutoff_freq_fir, color='red', linestyle='--', alpha=0.7)
    elif filter_type_fir == 'bandpass' or filter_type_fir == 'bandstop':
        plt.axvline(lowcut_fir, color='red', linestyle='--', alpha=0.7)
        plt.axvline(highcut_fir, color='red', linestyle='--', alpha=0.7)
    plt.ylim(0, 1.1)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(w_fir, 20 * np.log10(np.abs(h_fir) + 1e-9))
    plt.title(f'{filter_desc_fir} - 对数幅度响应 (dB)')
    plt.xlabel('频率 (Hz)')
    plt.ylabel('幅度增益 (dB)')
    plt.grid(True)
    plt.ylim(-100, 5)
    if filter_type_fir == 'lowpass' or filter_type_fir == 'highpass':
        plt.axvline(cutoff_freq_fir, color='red', linestyle='--', alpha=0.7)
    elif filter_type_fir == 'bandpass' or filter_type_fir == 'bandstop':
        plt.axvline(lowcut_fir, color='red', linestyle='--', alpha=0.7)
        plt.axvline(highcut_fir, color='red', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()