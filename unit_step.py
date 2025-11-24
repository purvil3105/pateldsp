import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-10 , 11)
step = np.where(n>=0 ,1,0)
plt.stem(n,step)
plt.xlabel('n')
plt.ylabel('Unit Step Signal u[n]')
plt.title('Unit Step Signal')
plt.grid()
plt.show()
