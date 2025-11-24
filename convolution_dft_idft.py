import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N = len(x)
    Xr , Xi = np.zeros(N) , np.zeros(N)
    for k in range(N):
        for n in range(N):
            angle = 2*np.pi*k*n/N
            Xr[k]+=x[n]*np.cos(angle)
            Xi[k]+=x[n]*np.sin(-angle)
    
    return Xr , Xi
def idft(Xr , Xi):
    N = len(Xr)
    x = np.zeros(N)
    for n in range(N):
        for k in range(N):
            angle = 2*np.pi*k*n/N
            x[n]+=1/N*(Xr[k]*np.cos(angle)-Xi[k]*np.sin(angle))
    return x
x = np.array([1, 7, 2, 4, 6, 9, 10]) # Input signal
h = np.array([1, 1, 1, 1, 1, 1, 10, 7, 2, 4]) # impulse reponse
N = len(x)+ len(h)-1
x_pad = np.pad(x , (0 ,N- len(x)))
h_pad = np.pad(h , (0,N-len(h)))
Xr , Xi = dft(x_pad)
Hr ,Hi = dft(h_pad)
Yr = Xr*Hr - Xi*Hi
Yi = Xr*Hi + Xi*Hr
y = idft(Yr , Yi)
y_np = np.convolve(x,h)
plt.subplot(2,1,1)
plt.stem(np.arange(len(y)) ,y)
plt.title('Convolution using DFT and IDFT')
plt.subplot(2,1,2)
plt.stem(np.arange(len(y_np)) , y_np)
plt.title('Convolution using Numpy')
plt.tight_layout()
plt.show()
