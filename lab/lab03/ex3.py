import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1 / fs)

f1 = 3
f2 = 5
f3 = 12

x = np.cos(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t) + np.sin(2 * np.pi * f3 * t)

plt.plot(t, x)
plt.xlabel("Timp")
plt.ylabel("Amplitudine")
plt.grid(True)
plt.savefig("ex3_semnal.pdf")
plt.show()


N = len(x)
omegas = np.arange(0, 20, 1)
X = np.zeros(len(omegas), dtype=complex)

for i, omega in enumerate(omegas):
    for n in range(N):
        X[i] += x[n] * np.exp(-2j * np.pi * omega * n / fs)



plt.stem(omegas, np.abs(X))
plt.xlabel("Frecventa")
plt.ylabel("Modulul transformatei Fourier")
plt.grid(True)
plt.savefig("ex3_fourier.pdf")
plt.show()