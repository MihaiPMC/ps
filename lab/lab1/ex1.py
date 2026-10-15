import numpy as np
import matplotlib.pyplot as plt

t_desen = np.arange(0, 0.03, 0.0005)
t_esantion = np.arange(0, 0.03, 1 / 200)

x = np.cos(520 * np.pi * t_desen + np.pi / 3)
x_esantion = np.cos(520 * np.pi * t_esantion + np.pi / 3)

y = np.cos(280 * np.pi * t_desen - np.pi / 3)
y_esantion = np.cos(280 * np.pi * t_esantion - np.pi / 3)

z = np.cos(120 * np.pi * t_desen + np.pi / 3)
z_esantion = np.cos(120 * np.pi * t_esantion + np.pi / 3)

fig, axs = plt.subplots(3, 1)

axs[0].plot(t_desen, x)
axs[0].stem(t_esantion, x_esantion)

axs[1].plot(t_desen, y)
axs[1].stem(t_esantion, y_esantion)

axs[2].plot(t_desen, z)
axs[2].stem(t_esantion, z_esantion)

plt.savefig('ex1.pdf')
plt.show()

