import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 6, 10, 11, 12, 13, 14, 5, 3, 2, 1, 10, 11])
N = len(x)
Xr , Xi = np.zeros(N) , np.zeros(N)
for k in range(N):
    for n in range(N):
        angle = 2*np.pi*k*n/N
        Xr[k]+= x[n]*np.cos(angle)
        Xi[k]+= x[n]*np.sin(-angle)
X = Xr+1j*Xi

mag = np.sqrt(Xr**2+Xi**2)
phase = np.arctan2(Xi , Xr)

# extra 
X_ex = np.zeros(N , dtype=complex)
for k in range(N):
    for n in range(N):
        angle = 2*np.pi*n*k/N
        X_ex[k] +=x[n]*np.exp(-1j*angle)

#inverse 
t = np.zeros(N)
for n in range(N):
    for k in range(N):
        angle = 2*np.pi*k*n/N
        t[n] +=1/N* (Xr[k]*np.cos(angle) - Xi[k]*np.sin(angle))

plt.figure(figsize=(14,8))
plt.subplot(2,2,1)
plt.stem(range(len(x)) , x)
plt.subplot(2,2,2)
plt.stem(range(len(x)) , mag)
plt.subplot(2,2,3)
plt.stem(range(len(x)) , phase)
plt.subplot(2,2,4)
plt.stem(range(len(x)) , t)

plt.show()



