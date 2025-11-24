import numpy as np
import matplotlib.pyplot as plt
x1 = np.array([4, 2, 3, 4])
n = np.arange(-len(x1) , len(x1))
impulse = np.where(n==0 , 1, 0)
unit = np.where(n>=0 ,1,0)
y = np.convolve(x1, impulse)
z = np.convolve(x1 , unit)
plt.subplot(2,1,1)
plt.stem(range(len(y)), y)
plt.xlabel('n')
plt.ylabel('Impulse Response h[n]')
plt.title('Impulse Response')
plt.grid()
plt.tight_layout()
plt.subplot(2,1,2)
plt.stem(range(len(z)) , z)
plt.xlabel('n')
plt.ylabel('Unit Step Response s[n]')
plt.title('Unit Step Response')
plt.grid()
plt.tight_layout()

plt.show()



