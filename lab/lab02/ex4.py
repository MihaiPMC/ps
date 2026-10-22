import numpy as np
import matplotlib.pyplot as plt

f = 5
T = 1
t = np.arange(0, T, 1 / 1000)

sin = np.sin(2 * np.pi * f * t)
sawtooth = np.mod(f * t, 1)
combined = sin + sawtooth

plt.subplot(3, 1, 1)
plt.plot(t, sin)
plt.title('Sinus')

plt.subplot(3, 1, 2)
plt.plot(t, sawtooth)
plt.title('Sawtooth')

plt.subplot(3, 1, 3)
plt.plot(t, combined)
plt.title('Combined')

plt.tight_layout()
plt.savefig('ex4.pdf')
plt.show()

