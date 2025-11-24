import numpy as np
import matplotlib.pyplot as py

x = np.array([1, 2, 3, 6, 10, 11, 12, 13, 14, 5, 3, 2, 1, 10, 11])
N = len(x)
Xr , Xi = np.zeros(N) , np.zeros(N)
for k in range(N):
    for n in range(N):
        angle = 2*np.pi*k*n/N
        Xr[k] +=x[n]*np.cos(angle)
        Xi[k] += x[n]*np.sin(-angle)
        X = Xr+1j*Xi

mag = np.sqrt(Xr**2 +Xi**2)
phase = np.arctan2(Xi,Xr)
### extra 
X_ex = np.zeros(N , dtype = complex)
for k in range(N):
    for n in range(N):
        angle = 2*np.pi*k*n/N
        X_ex[k] += x[n]*np.exp(1j*-angle)
#######
# inverse dft
t = np.zeros(N)
for n in range(N):
    for k in range(N):
        angle = 2*np.pi*k*n/N
        t[n]+= 1/N*(Xr[k]*np.cos(angle)-Xi[k]*np.sin(angle))


py.figure(figsize=(14,8))
py.subplot(2,2,1)
py.stem(np.arange(N),mag)
py.subplot(2,2,2)
py.stem(np.arange(N) , phase)
py.subplot(2,2,3)
py.stem(np.arange(N), t)
py.subplot(2,2,4)
py.stem(np.arange(N), np.abs(X_ex)) # as stem cant display complex
py.tight_layout()
py.show()




