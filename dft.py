import numpy as np
import matplotlib.pyplot as plt

# Input sequence
x = np.array([1, 2, 3, 4], dtype=complex)   # You can change this sequence
N = len(x)

# --- DFT computation ---
X = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

# --- IDFT computation ---
x_reconstructed = np.zeros(N, dtype=complex)
for n in range(N):
    for k in range(N):
        x_reconstructed[n] += X[k] * np.exp(1j * 2 * np.pi * k * n / N)
x_reconstructed = x_reconstructed / N

# --- Display Results ---
print("Input sequence x[n]:")
print(np.round(x, 3))

print("\nDFT X[k]:")
print(np.round(X, 3))

print("\nIDFT (reconstructed x[n]):")
print(np.round(x_reconstructed.real, 3))  # Only real part (imaginary part should be ≈ 0)

# --- Plotting ---
plt.figure(figsize=(12,6))

# Original sequence
plt.subplot(2,2,1)
plt.stem(np.arange(N), x.real)
plt.title("Original Sequence x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

# Magnitude Spectrum
plt.subplot(2,2,2)
plt.stem(np.arange(N), np.abs(X))
plt.title("Magnitude Spectrum |X[k]|")
plt.xlabel("k")
plt.ylabel("Magnitude")

# Phase Spectrum
plt.subplot(2,2,3)
plt.stem(np.arange(N), np.angle(X))
plt.title("Phase Spectrum ∠X[k]")
plt.xlabel("k")
plt.ylabel("Phase (radians)")

# Reconstructed sequence
plt.subplot(2,2,4)
plt.stem(np.arange(N), x_reconstructed.real)
plt.title("Reconstructed Sequence (IDFT)")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
