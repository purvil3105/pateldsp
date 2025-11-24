import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-10 ,11 )
no = int(input("enter the valeu of no"))
ramp = np.where(n-no>=0 , n-no , 0)
plt.stem(n,ramp)
plt.xlabel('n')
plt.ylabel('Ramp Signal r[n-no]') 
plt.title('Ramp Signal')
plt.xticks(np.arange(-10, 12, 1))
plt.grid()
plt.show()

