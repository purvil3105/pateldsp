import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0 , 5 , 0.2)
a = float(input("enter the value of a :"))

x = np.exp(a*n)
plt.stem(n,x)
plt.xlabel('n')
plt.ylabel('Exponential Signal e^(an)')
plt.title('Exponential Signal')
plt.grid()
plt.show()
