import numpy as np
import sounddevice as sd
from scipy.io import wavfile

# a
f = 400
fs = 1600

t = np.arange(1600) / fs
x = np.sin(2 * np.pi * f * t)

sd.play(x, fs)
sd.wait()
wavfile.write("ex3a.wav", fs, x)


# b
f = 800
fs = 3200

t = np.arange(0, 3, 1 / fs)
x = np.sin(2 * np.pi * f * t)

sd.play(x, fs)
sd.wait()
wavfile.write("ex3b.wav", fs, x)

# c
f = 240
fs = 2400

t = np.arange(0, 1, 1 / fs)
x = np.mod(f * t, 1)

sd.play(x, fs)
sd.wait()
wavfile.write("ex3c.wav", fs, x)


# d
f = 300
fs = 3000

t = np.arange(0, 1, 1 / fs)
x = np.sign(np.sin(2 * np.pi * f * t))

sd.play(x, fs)
sd.wait()
wavfile.write("ex3d.wav", fs, x)