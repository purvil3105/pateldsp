import numpy as np 
import matplotlib.pyplot as plt 

f = 5
fs = 12
n = np.arange(0,20) # no of smaple 

x = np.sin(2*np.pi * f/fs *n)
plt.stem(n,x)
plt.xlabel('n')
plt.ylabel('Sinusoidal Signal x[n]')
plt.title('Sinusoidal Signal')
plt.grid()
plt.show()



