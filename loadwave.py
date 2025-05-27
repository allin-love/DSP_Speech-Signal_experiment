import wave
import matplotlib.pyplot as plt
import numpy as np
f = wave.open(r"zrk_audio.wav", "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(nchannels,sampwidth,framerate,nframes)
str_data = f.readframes(nframes)
print(str_data[:10])
wave_data = np.fromstring(str_data, dtype=np.short)
print(wave_data[:10])
wave_data = wave_data*1.0/(max(abs(wave_data)))
print(wave_data[:10])
time = np.arange(0, nframes) * (1.0 / framerate)
plt.figure(figsize=(10,4))
plt.plot(time, wave_data,c="g")
plt.xlabel("time (seconds)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
