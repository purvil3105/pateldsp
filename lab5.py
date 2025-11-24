import numpy as np
import matplotlib.pyplot as plt

x = [2,1,2]
y = [1,2,3,4]

def convolution(x,y):
    len_x = len(x)
    len_y = len(y)

    len_z = (len_x + len_y - 1)
    z = [0]*len_z

    for n in range(len_z):
        total = 0
        for k in range(len_x):
            j = n-k
            if 0 <= j < len_y:
                total += x[k]*y[j]
        z[n] = total
    return z

def DFT(x):
    N = len(x)
    omega = 2 * np.pi / N
    z = [0] * N 
    for m in range(N): 
        temp = 0
        for n in range(N): 
            temp += x[n] * np.exp(-1j * omega * m * n)
        z[m] = temp
    return np.array(z)

def inverseDFT(X):
    N = len(X)
    omega = 2 * np.pi / N
    x_reconstructed = [0] * N
    for n in range(N):
        temp = 0
        for k in range(N):
            temp += X[k] * np.exp(1j * omega * n * k)
        x_reconstructed[n] = (1 / N) * temp
    return np.real(x_reconstructed)

N = len(x) + len(y) - 1

x_padded = np.pad(x, (0, N - len(x)))
y_padded = np.pad(y, (0, N - len(y)))

X = DFT(x_padded)
Y = DFT(y_padded)

Z = X * Y

z = inverseDFT(Z)

conv = convolution(x,y)

print("Linear Convolution :", conv)
print("Linear Convolution using DFT:", z)

plt.figure(figsize=(10,5))

plt.subplot(2, 1, 1)
plt.stem(range(len(conv)), conv)
plt.title("Linear Convolution")
plt.xlabel("n")
plt.ylabel("z[n]")
plt.grid(True)


plt.subplot(2, 1, 2)
plt.stem(range(len(z)), z)
plt.title("Linear Convolution using DFT")
plt.xlabel("n")
plt.ylabel("z[n]")
plt.grid(True)

plt.tight_layout()
plt.show()

