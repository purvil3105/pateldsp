import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10 , 11)
delta = np.zeros(len(n))
delta[n==0]=1

plt.stem(n ,delta)
plt.title('impulse signal')
plt.xlabel('n')
plt.ylabel('delta')
plt.grid(True)
plt.show()
