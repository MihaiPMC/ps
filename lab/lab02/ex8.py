import numpy as np
import matplotlib.pyplot as plt

alpha =np.linspace(-np.pi / 2, np.pi / 2, 1000)

x = np.sin(alpha)

taylor = alpha

plt.plot(alpha, x, label='sin(alpha)')
plt.plot(alpha, taylor, label='Taylor')

plt.legend()
plt.savefig('ex8.pdf')
plt.show()

errorTaylor = np.abs(x - taylor)
plt.plot(alpha, errorTaylor)
plt.title('Error Taylor')
plt.savefig('ex8_error.pdf')
plt.show()

pade = (alpha - 7 * alpha**3 / 60) / (1 + alpha**2 / 20)
plt.plot(alpha, pade, label='Pade')
plt.legend()
plt.savefig('ex8_pade.pdf')
plt.show()


errorPade = np.abs(x - pade)
plt.plot(alpha, errorPade)
plt.title('Error Pade')
plt.savefig('ex8_error_pade.pdf')
plt.show()

plt.semilogy(alpha, errorPade, label = 'Pade')
plt.semilogy(alpha, errorTaylor, label = 'Taylor')
plt.legend()
plt.title('Error Taylor vs Pade')
plt.savefig('ex8_error_taylor_vs_pade.pdf')
plt.show()