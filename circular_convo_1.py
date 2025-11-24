import numpy as np
import matplotlib.pyplot as plt

def circular(x, h):
    N = max(len(x), len(h))
    x = np.pad(x, (0, N - len(x)))
    h = np.pad(h, (0, N - len(h)))
    y = [0] * N
    for n in range(N):
        for k in range(N):
            y[n] += x[k] * h[(n - k) % N]   # <-- corrected
    return y

def cir(x, h):
    N = max(len(x), len(h))
    x = np.pad(x, (0, N - len(x)))
    h = np.pad(h, (0, N - len(h)))
    y = np.fft.ifft(np.fft.fft(x) * np.fft.fft(h))
    return np.real(y)

x = [1, 2, 3, 4]
h = [1, -1, 2]

r = circular(x, h)
k = cir(x, h)

print("Manual Circular Convolution =", r)
print("FFT based Circular Convolution =", k)
