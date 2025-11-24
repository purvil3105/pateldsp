import numpy as np
import matplotlib.pyplot as plt


def cross(x,h):
    N = len(x)
    M = len(h)
    y= [0]*(M+N-1)
    shift = M-1
    for n in range(-(M-1) , N):
        sum =0
        for k in range(N):
            if 0<= n+k < M:
                sum+= x[k]*h[n+k]
        y[n+shift] = sum
    return y 
x = [1, 2, 3, 4]
h = [1, -1, 2]
r = cross(x,h)
print(r)
plt.stem(range(len(r)) , r)
plt.show()