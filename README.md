# DSP_Speech Signal Experiment

此存储库包含用于语音信号数字处理的 Python 脚本。它包括加载音频、可视化波形、FFT 频谱和语谱图、设计和应用 IIR 和 FIR 滤波器、添加噪声以及观察这些操作效果的功能。

## 文件结构

*   `load.py`: 加载 WAV 音频文件，显示其波形、FFT 频谱和语谱图。
*   `IIR_filter.py`: 实现 IIR 滤波器设计（巴特沃斯：低通、高通、带通、带阻）并可视化其频率响应。可以独立运行以查看滤波器特性。
*   `FIR_filter.py`: 实现 FIR 滤波器设计（汉明窗：低通、高通、带通、带阻）并可视化其频率响应。可以独立运行以查看滤波器特性。
*   `Adding Noise and Filtering.py`: 演示向音频信号添加高斯白噪声，然后使用 [`IIR_filter.design_iir_filter`](IIR_filter.py) 和 [`FIR_filter.design_fir_filter`](FIR_filter.py) 设计的 IIR 和 FIR 滤波器对其进行滤波。可视化噪声信号和滤波后的信号（波形和 FFT）。
*   `zrk_audio.wav`: 用于实验的主要示例音频文件。
*   `Experiment Log.md`: 一个 Markdown 文件，记录了实验结果和相关图表。
*   `wav/`: 目录，用于保存处理后的音频文件（例如，由 `Adding Noise and Filtering.py` 生成的 `audio_noisy.wav`）。
*   `fig/`: 目录，通常包含从实验中保存的绘图（如 `Experiment Log.md` 中引用的图像所示）。

## 功能特性

*   **音频加载与基础可视化**:
    *   使用 `librosa` 加载 `.wav` 音频文件。
    *   显示时域波形。
    *   计算并显示快速傅里叶变换 (FFT) 以进行频谱分析。
    *   生成并显示语谱图。
*   **滤波器设计与分析**:
    *   **IIR 滤波器**: 设计巴特沃斯滤波器（低通、高通、带通、带阻）。可视化幅度和对数幅度响应。 ([`IIR_filter.py`](IIR_filter.py))
    *   **FIR 滤波器**: 使用汉明窗设计 FIR 滤波器（低通、高通、带通、带阻）。可视化幅度和对数幅度响应。 ([`FIR_filter.py`](FIR_filter.py))
*   **噪声添加与信号滤波**:
    *   生成高斯白噪声并将其添加到音频信号中。
    *   将设计的 IIR 和 FIR 滤波器应用于音频信号。
    *   在时域和频域中可视化原始信号、噪声信号和滤波后信号。 ([`Adding Noise and Filtering.py`](Adding Noise and Filtering.py))
*   **输出**:
    *   生成各种用于分析的图表。
    *   将处理后的音频（如加噪音频）保存到 `wav/` 目录。

## 依赖库

*   Python 3.x
*   `librosa`
*   `numpy`
*   `matplotlib`
*   `scipy`

您可以使用 pip 安装这些依赖项：
```bash
pip install librosa numpy matplotlib scipy
```
确保 `matplotlib` 配置为支持中文显示（脚本中已通过 `plt.rcParams` 设置）。

## 如何运行

1.  **加载和基础音频分析 ([`load.py`](load.py))**:
    要可视化 `zrk_audio.wav` 的波形、FFT 和语谱图：
    ```bash
    python load.py
    ```

2.  **设计和可视化 IIR 滤波器 ([`IIR_filter.py`](IIR_filter.py))**:
    此脚本可以运行以查看预定义 IIR 滤波器的频率响应（默认为低通）。您可以修改 `if __name__ == "__main__":` 块中的参数以测试不同的 IIR 滤波器类型和规格。
    ```bash
    python IIR_filter.py
    ```

3.  **设计和可视化 FIR 滤波器 ([`FIR_filter.py`](FIR_filter.py))**:
    与 `IIR_filter.py` 类似，此脚本可视化预定义 FIR 滤波器的频率响应（默认为低通）。可以在 `if __name__ == "__main__":` 块中调整参数。
    ```bash
    python FIR_filter.py
    ```

4.  **添加噪声和滤波音频 ([`Adding Noise and Filtering.py`](Adding Noise and Filtering.py))**:
    此脚本加载 `zrk_audio.wav`，添加噪声，将加噪后的版本保存到 `wav/audio_noisy.wav`，然后应用预定义的 IIR 和 FIR 低通滤波器。它将显示：
    *   噪声信号的波形和 FFT。
    *   IIR 滤波后信号的波形和 FFT。
    *   FIR 滤波后信号的波形和 FFT。
    ```bash
    python "Adding Noise and Filtering.py"
    ```
    *注意：滤波器参数（如截止频率、阶数、类型）可以直接在脚本中调整。*

## 实验日志

[`Experiment Log.md`](Experiment Log.md) 文件记录了进行的各种实验，包括显示以下内容的图表：
*   初始音频分析（波形、FFT、语谱图）。
*   IIR 和 FIR 滤波器的响应特性。
*   添加噪声和后续滤波的结果。

[`Experiment Log.md`](Experiment Log.md) 文件记录了进行的各种实验。以下是部分实验结果的图表：

### 音频加载与分析 (`load.py`)
#### 波形图
![](https://pppppall.oss-cn-guangzhou.aliyuncs.com/undefinedwaveform.png)
#### FFT 频谱图
![fft.png](https://pppppall.oss-cn-guangzhou.aliyuncs.com/undefinedfft.png)
#### 语谱图
![Spectrogram.png](https://pppppall.oss-cn-guangzhou.aliyuncs.com/undefinedSpectrogram.png)

### IIR 滤波器特性 (`IIR_filter.py`)
#### 低通滤波器 (巴特沃斯) - 幅度响应
![image.png](https://pppppall.oss-cn-guangzhou.aliyuncs.com/undefined20250527144558.png)
#### 低通滤波器 (巴特沃斯) - 对数幅度响应
![IIR_lowpass_Logarithmic amplitude response.png](https://pppppall.oss-cn-guangzhou.aliyuncs.com/undefinedIIR_lowpass_Logarithmic%20amplitude%20response.png)

### FIR 滤波器特性 (`FIR_filter.py`)
#### 低通滤波器 (汉明窗) - 幅度响应
![](https://pppppall.oss-cn-guangzhou.aliyuncs.com/undefinedFIR_lowpass_Amplitude%20Response.png)
#### 低通滤波器 (汉明窗) - 对数幅度响应
![FIR_lowpass_Logarithmic amplitude Response.png](https://pppppall.oss-cn-guangzhou.aliyuncs.com/undefinedFIR_lowpass_Logarithmic%20amplitude%20Response.png)

### 添加噪声与滤波 (`Adding Noise and Filtering.py`)
#### 含噪语音信号 - 波形与FFT
![Noisy speech signal waveform and FFT.png](https://pppppall.oss-cn-guangzhou.aliyuncs.com/undefinedNoisy%20speech%20signal%20waveform%20and%20FFT.png)
#### IIR 低通滤波后 - 波形与FFT
![IIR_lowpass_Waveform and FFT.png](https://pppppall.oss-cn-guangzhou.aliyuncs.com/undefinedIIR_lowpass_Waveform%20and%20FFT.png)
#### FIR 低通滤波后 - 波形与FFT
![FIR_lowpass_Waveform and FFT.png](https://pppppall.oss-cn-guangzhou.aliyuncs.com/undefinedFIR_lowpass_Waveform%20and%20FFT.png)

日志中的图像链接到外部源。对于本地查看，如果脚本执行期间将图保存到 `fig/` 目录，您可以参考该目录。