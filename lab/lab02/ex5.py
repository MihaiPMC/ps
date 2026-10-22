import numpy as np
import sounddevice as sd
from scipy.io import wavfile

T = 1
fs = 10000
t = np.arange(0, T, 1 / fs)

f1 = 500
f2 = 1000

x = np.sin(2 * np.pi * f1 * t)
y = np.sin(2 * np.pi * f2 * t)

z = np.concatenate((x, y))

sd.play(z, fs)
sd.wait()
wavfile.write('ex5.wav', fs, z)

# se aud 2 sunete conseutive, al 2 lea este mai inalt decat primul