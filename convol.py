import numpy as np
import matplotlib.pyplot as plt

# Two input sequences
x = [1, 2, 3, 4]
h = [1, -1, 2]

# Lengths
N = len(x)
M = len(h)

# Output length = N + M - 1
y = [0] * (N + M - 1)

# Convolution sum
for n in range(N + M - 1):
    for k in range(N):
        if 0 <= n - k < M:
            y[n] += x[k] * h[n - k]

print("x =", x)
print("h =", h)
print("Convolution y =", y)
plt.stem(np.arange(len(y)), y)
plt.title("Convolution Output")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)
plt.show()
