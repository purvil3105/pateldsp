import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10 , 11)
delta = np.concatenate((np.zeros(10) , np.ones(1) , np.zeros(10)))
plt.stem(n ,delta)
plt.title('impulse signal')
plt.xlabel('n')
plt.ylabel('delta')
plt.grid(True)
plt.show()
