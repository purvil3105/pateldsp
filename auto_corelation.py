import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

N = len(x)

# Auto-correlation length = 2N - 1
r = [0] * (2*N - 1)

# Lag ranges from -(N-1) to +(N-1)
shift = N - 1

for m in range(-(N-1), N):
    total = 0
    for n in range(N):
        if 0 <= n + m < N:
            total += x[n] * x[n + m]
    r[m + shift] = total

print("Auto-Correlation =", r)

# Plot
plt.stem(range(-shift, shift+1), r)
plt.title("Auto-Correlation")
plt.xlabel("Lag")
plt.ylabel("rxx[m]")
plt.grid(True)
plt.show()
