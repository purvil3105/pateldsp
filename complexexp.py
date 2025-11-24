import numpy as np
import matplotlib.pyplot as plt 

omega = np.pi/4
n = np.arange(0,40)

x = np.exp(1j *omega *n)

plt.subplot(2,1,1)
plt.stem(n , np.real(x))
plt.xlabel('n')
plt.ylabel('Real Part')
plt.title('Complex Exponential Signal')
plt.grid()
plt.subplot(2,1,2)
plt.stem(n , np.imag(x))
plt.xlabel('n')
plt.ylabel('Imaginary Part')
plt.grid()
plt.show()
