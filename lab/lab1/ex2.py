import numpy as np
import matplotlib.pyplot as plt

# a
f = 400
fs = 1600

t = np.arange(1600) / fs

x = np.sin(2 * np.pi * f * t)

plt.plot(t, x)
plt.savefig('ex2a.pdf')
plt.xlim(0, 0.01)
plt.savefig('ex2a_zoom.pdf')
plt.show()



# b
f = 800
fs = 3200

t = np.arange(0, 3, 1 / fs)
x = np.sin(2 * np.pi * f * t)

plt.plot(t, x)
plt.savefig('ex2b.pdf')
plt.xlim(0, 0.01)
plt.savefig('ex2b_zoom.pdf')
plt.show()


# c
f = 240
fs = 2400

t = np.arange(0, 1, 1 / fs)
x = np.mod(f * t, 1)

plt.plot(t, x)
plt.savefig('ex2c.pdf')
plt.xlim(0, 0.01)
plt.savefig('ex2c_zoom.pdf')
plt.show()

# d
f = 300
fs = 3000

t = np.arange(0, 1, 1 / fs)
x = np.sign(np.sin(2 * np.pi * f * t))

plt.plot(t, x)
plt.savefig('ex2d.pdf')
plt.xlim(0, 0.01)
plt.savefig('ex2d_zoom.pdf')
plt.show()

# e
x = np.random.rand(128, 128)
plt.imshow(x)
plt.savefig('ex2e.pdf')
plt.show()

# f
x = np.zeros((128, 128))

x[32:96, 32:96] = np.ones((64, 64))

plt.imshow(x)
plt.savefig('ex2f.pdf')
plt.show()

