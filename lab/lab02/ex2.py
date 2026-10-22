import numpy as np
import matplotlib.pyplot as plt

A = 1
f = 5

T = 1
t = np.arange(0, T, 1 / 1000)

faza = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]

for phi in faza:
    x = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, x, label=f'phi={phi:.2f} rad')

plt.legend()
plt.tight_layout()
plt.savefig("ex2a.pdf")
plt.show()

x = A * np.sin(2 * np.pi * f * t + faza[0])

z = np.random.normal(0, 1, len(x))
snr_values = [0.1, 1, 10, 100]

for snr in snr_values:
    gamma = np.linalg.norm(x) / (
        np.sqrt(snr) * np.linalg.norm(z)
    )

    y = x + gamma * z
    plt.plot(t, y, label=f'SNR={snr}')
    plt.legend()
    plt.savefig(f"ex2b_snr_{snr}.pdf")
    plt.show()
