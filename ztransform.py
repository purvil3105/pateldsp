import numpy as np
from scipy.signal import zpk2tf

import  matplotlib.pyplot as plt

zeros=np.array([1,0.5])
pole=np.array([2,0.8,0.6])
gain=1

b,a=zpk2tf(zeros,pole,gain)

print(b)
print(a)

roc=max(abs(pole))
print(roc)

plt.scatter(np.real(zeros),np.imag(zeros),marker='o',label='zeros')
plt.scatter(np.real(pole),np.imag(pole),marker='x',label='pole')

theta=np.linspace(0,2*np.pi,500)
plt.plot(np.cos(theta),np.sin(theta))



# transfer
import numpy as np
from scipy.signal import residue

b = [1, -0.5]          
a = [1, -0.8, -0.1]

r,p,k=residue(b,a);

print(r)
print(p)
print(k)
