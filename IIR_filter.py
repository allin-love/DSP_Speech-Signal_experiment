import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import librosa
import numpy as np

# 设置 matplotlib 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False  # 负号显示
# 加载 WAV 文件并提取原始采样率
audio_filename = 'zrk_audio.wav' 
y, sr = librosa.load(audio_filename, sr=None) 

def design_iir_filter(sr, filter_type_iir='lowpass', cutoff_freq_iir=3000, order_iir=4, lowcut_iir=500, highcut_iir=2500):
    """
    设计 IIR 滤波器并返回滤波器系数和描述。
    参数:
        sr (int): 采样率。
        filter_type_iir (str): 滤波器类型，'lowpass', 'highpass', 'bandpass', 'bandstop'。
        cutoff_freq_iir (int): 截止频率 (用于低通和高通滤波器)。
        order_iir (int): 滤波器阶数。
        lowcut_iir (int): 低截止频率 (用于带通和带阻滤波器)。
        highcut_iir (int): 高截止频率 (用于带通和带阻滤波器)。

    返回:
        tuple: 包含滤波器系数 (b, a) 和滤波器描述的元组。
    """
    if filter_type_iir == 'lowpass':
        # Wn 归一化频率 = 2 * cutoff / sampling_rate
        Wn_iir = 2 * cutoff_freq_iir / sr
        b_iir, a_iir = signal.butter(order_iir, Wn_iir, btype='lowpass')
        filter_desc_iir = f'IIR 低通滤波器 (Butterworth, 阶数={order_iir}, 截止频率={cutoff_freq_iir}Hz)'
    elif filter_type_iir == 'highpass':
        Wn_iir = 2 * cutoff_freq_iir / sr
        b_iir, a_iir = signal.butter(order_iir, Wn_iir, btype='highpass')
        filter_desc_iir = f'IIR 高通滤波器 (Butterworth, 阶数={order_iir}, 截止频率={cutoff_freq_iir}Hz)'
    elif filter_type_iir == 'bandpass':
        Wn_iir = [2 * lowcut_iir / sr, 2 * highcut_iir / sr]
        b_iir, a_iir = signal.butter(order_iir, Wn_iir, btype='bandpass')
        filter_desc_iir = f'IIR 带通滤波器 (Butterworth, 阶数={order_iir}, 通带={lowcut_iir}-{highcut_iir}Hz)'
    else:  # bandstop
        Wn_iir = [2 * lowcut_iir / sr, 2 * highcut_iir / sr]
        b_iir, a_iir = signal.butter(order_iir, Wn_iir, btype='bandstop')
        filter_desc_iir = f'IIR 带阻滤波器 (Butterworth, 阶数={order_iir}, 阻带={lowcut_iir}-{highcut_iir}Hz)'
    
    return b_iir, a_iir, filter_desc_iir

if __name__ == "__main__":
    # 调用test
    filter_type_iir = 'lowpass'
    cutoff_freq_iir = 3000
    order_iir = 4
    lowcut_iir = 500
    highcut_iir = 2500
    # sr 在文件顶部已定义，此处可以直接使用
    b_iir, a_iir, filter_desc_iir = design_iir_filter(sr, filter_type_iir, cutoff_freq_iir, order_iir, lowcut_iir, highcut_iir)

    # 计算并绘制频率响应
    w_iir, h_iir = signal.freqz(b_iir, a_iir, worN=8000, fs=sr)

    plt.figure(figsize=(10, 5))
    plt.plot(w_iir, np.abs(h_iir), 'b')
    plt.title(f'{filter_desc_iir} - 幅度响应')
    plt.xlabel('频率 (Hz)')
    plt.ylabel('幅度增益')
    plt.grid(True)
    if filter_type_iir == 'lowpass' or filter_type_iir == 'highpass':
        plt.axvline(cutoff_freq_iir, color='red', linestyle='--', alpha=0.7)
    elif filter_type_iir == 'bandpass' or filter_type_iir == 'bandstop':
        plt.axvline(lowcut_iir, color='red', linestyle='--', alpha=0.7)
        plt.axvline(highcut_iir, color='red', linestyle='--', alpha=0.7)
    plt.ylim(0, 1.1)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(w_iir, 20 * np.log10(np.abs(h_iir) + 1e-9)) # 加上一个很小的数避免log10(0)
    plt.title(f'{filter_desc_iir} - 对数幅度响应 (dB)')
    plt.xlabel('频率 (Hz)')
    plt.ylabel('幅度增益 (dB)')
    plt.grid(True)
    if filter_type_iir == 'lowpass' or filter_type_iir == 'highpass':
        plt.axvline(cutoff_freq_iir, color='red', linestyle='--', alpha=0.7)
    elif filter_type_iir == 'bandpass' or filter_type_iir == 'bandstop':
        plt.axvline(lowcut_iir, color='red', linestyle='--', alpha=0.7)
        plt.axvline(highcut_iir, color='red', linestyle='--', alpha=0.7)
    plt.ylim(-60, 5) # 根据IIR滤波器的特性调整Y轴范围
    plt.tight_layout()
    plt.show()