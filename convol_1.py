import numpy as np 
import matplotlib.pyplot as plt 

def convol(x , h):
    N = len(x)
    M= len(h)
    y = [0]*(N+M-1)
    for n in range(N+M-1):
        for k in range(N):
            if 0<=n -k <M:
                y[n]+=x[k]*h[n-k]
    return y

x = [1,2,3,4]
h = [1,-1 ,2]
y =convol(x,h)
print(y)
plt.stem(range(len(y)) , y)
plt.title('convolution')
plt.show()