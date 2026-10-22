import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1 / fs)

f = 100
x = np.sin(2 * np.pi * f * t)

y = x[::4]
z = x[1::4]


plt.subplot(3, 1, 1)
plt.xlim(0, 0.1)
plt.plot(t, x)
plt.stem(t, x)

plt.subplot(3, 1, 2)
plt.xlim(0, 0.1)
plt.plot(t[::4], y)
plt.stem(t[::4], y)

plt.subplot(3, 1, 3)
plt.xlim(0, 0.1)
plt.plot(t[1::4], z)
plt.stem(t[1::4], z)

plt.tight_layout()
plt.savefig('ex7.pdf')
plt.show()

# semnalul are aceeas frecventa si acelasi numar de esantioane ca la a
# dar este decalat in faza pentru ca esantionarea incepe de la al 2 lea element
# forma graficului difera desi frecventa semnalului ramana aceeasi
