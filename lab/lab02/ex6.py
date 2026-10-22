import numpy as np
import matplotlib.pyplot as plt

A = 1
phi = 0
fs = 1000

t = np.arange(0, 1, 1 / fs)

f1 = fs / 2
f2 = fs / 4
f3 = 0

x = A * np.sin(2 * np.pi * f1 * t + phi)
y = A * np.sin(2 * np.pi * f2 * t + phi)
z = A * np.sin(2 * np.pi * f3 * t + phi)

plt.subplot(3, 1, 1)
plt.xlim(0, 0.1)
plt.plot(t, x)
plt.stem(t, x)
plt.title('f1 = fs/2')

plt.subplot(3, 1, 2)
plt.xlim(0, 0.1)
plt.plot(t, y)
plt.stem(t, y)
plt.title('f2 = fs/4')

plt.subplot(3, 1, 3)
plt.plot(t, z)
plt.stem(t, z)
plt.title('f3 = 0')

plt.tight_layout()
plt.savefig('ex6.pdf')
plt.show()

#pentru f = fs/2 semnalul esantionat este nul deoarece esantioanele coincid cu zerourile functiei sinus
#pe grafic nu este perfect 0 din cauza erorilor de rotunjire

#pentru f = fs/4 semnalul are 4 esantioane pe perioada, deci se observa sinusoidala

#pentru f = 0 semnalul este constant si egal cu 0