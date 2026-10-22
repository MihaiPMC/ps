import numpy as np
import matplotlib.pyplot as plt

A = 5
f = 5
T = 1

t = np.arange(0, T, 1 / 1000)

x = A * np.sin(2 * np.pi * f * t)
y = A * np.cos(2 * np.pi * f * t - np.pi / 2)

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Sinus')

plt.subplot(2, 1, 2)
plt.plot(t, y)
plt.title('Cosinus')

plt.tight_layout()
plt.savefig('ex1.pdf')
plt.show()
