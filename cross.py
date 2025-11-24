import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
h = [1, -1, 2]

N = len(x)
M = len(h)

# Output length N+M-1
r = [0] * (N + M - 1)

# Cross-correlation index shift starts from -(M-1)
shift = M - 1

for n in range(-(M-1), N):      # m = -2, -1, 0, 1, 2, 3   (for M=3, N=4)
    sum_val = 0
    for k in range(N):
        if 0 <= n+k < M:
            sum_val += x[k] * h[n + k]
    r[n + shift] = sum_val

print("Cross-Correlation r =", r)

plt.stem(r)
plt.title("Cross-Correlation Output")
plt.xlabel("n")
plt.ylabel("r[n]")
plt.grid(True)
plt.show()
