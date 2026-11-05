import numpy as np
import matplotlib.pyplot as plt

N = 8

n = np.arange(N)

line = n.reshape((N, 1))
col = n.reshape((1, N))


F = np.exp(-2j * np.pi * (line @ col) / N)

print(F)

fig, axis = plt.subplots(N, 2, figsize=(14, 20))

for i in range(N):
    axis[i, 0].plot(F[i, :].real)
    axis[i, 0].set_title(f"Real {i}")
    axis[i, 0].set_ylim(-1.1, 1.1)

    axis[i, 1].plot(F[i, :].imag)
    axis[i, 1].set_ylim(-1.1, 1.1)
    axis[i, 1].set_title(f"Imag {i}")

plt.tight_layout()
plt.savefig('ex1.pdf')
plt.show()

I = np.eye(N)
P = F.conj().T @ F

print(np.allclose(P, N * I))