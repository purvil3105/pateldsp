import numpy as np
import matplotlib.pyplot as plt

x =np.array([1,2,3,3,2,1,-1,-2,-3,5,6,-1,2,0,2,1])
h = np.array([3,2,1,1])
L = 4                         # number of valid samples per block
M = len(h)
N = L + M - 1                 # FFT size
x_pad = np.pad(x, (M-1, 0))
h_pad = np.pad(h, (0, N - M))
H = np.fft.fft(h_pad)
y_out = []
for start in range(0, len(x), L):
    x_block = x_pad[start : start + N]       # take N samples
    X = np.fft.fft(x_block)
    y_block = np.fft.ifft(X * H).real
    y_valid = y_block[M-1:]                  # discard first M-1
    y_out.extend(y_valid)
y_out = np.array(y_out)
y_direct = np.convolve(x, h)
print("Overlap–Save Output = ", y_out)
print("Direct Convolution = ", y_direct)
plt.stem(y_out)
plt.title("Overlap–Save Method")
plt.grid(True)
plt.show()
