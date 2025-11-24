import numpy as np
import matplotlib.pyplot as plt

# Given parameters
fs = 1000        # Sampling frequency (Hz)
T = 1.0          # Duration (seconds)
t = np.linspace(0, T, int(fs * T), endpoint=False)  # Time vector

# Input signal (two sine waves: 50Hz and 120Hz)
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

N = len(signal)  # Number of samples

# --- Compute DFT manually ---
X = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        X[k] += signal[n] * np.exp(-1j * 2 * np.pi * k * n / N)

# --- Compute IDFT manually ---
x_reconstructed = np.zeros(N, dtype=complex)
for n in range(N):
    for k in range(N):
        x_reconstructed[n] += X[k] * np.exp(1j * 2 * np.pi * k * n / N)
x_reconstructed = x_reconstructed / N

# --- Frequency axis (for plotting up to Nyquist) ---
freqs = np.arange(N) * fs / N

# --- Plot Results ---
plt.figure(figsize=(14, 8))

# Original Signal
plt.subplot(2, 2, 1)
plt.plot(t, signal)
plt.title("Original Signal (Time Domain)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# Magnitude Spectrum
plt.subplot(2, 2, 2)
plt.stem(freqs[:N//2], np.abs(X[:N//2]) * 2 / N)
plt.title("Magnitude Spectrum |X[k]|")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)

# Phase Spectrum
plt.subplot(2, 2, 3)
plt.stem(freqs[:N//2], np.angle(X[:N//2]))
plt.title("Phase Spectrum ∠X[k]")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Phase [radians]")
plt.grid(True)

# Reconstructed Signal
plt.subplot(2, 2, 4)
plt.plot(t, x_reconstructed.real)
plt.title("Reconstructed Signal (IDFT Output)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()

# --- Check accuracy ---
print("Reconstruction Error (should be near zero):", np.max(np.abs(signal - x_reconstructed.real)))
