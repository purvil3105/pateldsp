import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,3,2,1 , -1 , -2 , -3 ,5,6,-1,2 ,0,2,1])
h = np.array([3,2,1,1]) # 4

L= 4
M = len(h)
N = L+M-1

y_out = np.zeros(len(x) + M-1)
for start in range(0 , len(x) , L):
    x_block = x[start:start+L]
    x_pad = np.pad(x_block, (0 , N-len(x_block)))
    h_pad = np.pad(h , (0, N-len(h)))
    X = np.fft.fft(x_pad , N) # zero pad if not equal to N
    H = np.fft.fft(h_pad , N)
    Y_block = np.fft.ifft(X*H).real
    y_out[start:start+len(Y_block)] += Y_block

y_direct = np.convolve(x,h)
print(y_out)
print(y_direct)


