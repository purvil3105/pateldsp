import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(64)
N = len(x)
omega = 2 * np.pi / N

z = [0] * N 

for m in range(N): 
    temp = 0
    for n in range(N): 
        y = np.exp(-1j * omega * m * n)
        temp += x[n] * y
    z[m] = temp  

mag = [np.abs(val) for val in z]
phase = [np.angle(val) for val in z]   

X_fft = np.fft.fft(x)

print("Discrete Fourier Transform is: ", z)

plt.figure(figsize=(18,6))

plt.subplot(2, 2, 1)
plt.stem(range(N), z)
plt.grid(True)
plt.xlabel("index")
plt.ylabel("X[k]")
plt.title("Discrete Fourier Transform")

plt.subplot(2, 2, 2)
plt.stem(range(N), X_fft)
plt.grid(True)
plt.xlabel("index")
plt.ylabel("X[k]")
plt.title("Discrete Fourier Transform using FFT")

plt.subplot(2, 2, 3)
plt.stem(range(N), mag)
plt.grid(True)
plt.xlabel("index")
plt.ylabel("Magnitude")
plt.title("Magnitude plot of X[k]")

plt.subplot(2, 2, 4)
plt.stem(range(N), phase)
plt.grid(True)
plt.xlabel("index")
plt.ylabel("Radian")
plt.title("Phase plot of X[k]")


plt.tight_layout()
plt.show()
