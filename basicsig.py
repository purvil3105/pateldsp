import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# User-defined sampling frequency
# -------------------------------
Fs = 50                 # Sampling frequency (samples/sec)
Ts = 1/Fs               # Sampling time
t = np.arange(-1, 1, Ts)  # Time vector

# -------------------------------
# Basic Signals
# -------------------------------

# 1. Unit Impulse δ(t)
impulse = np.zeros_like(t)
impulse[np.where(t == 0)] = 1

# 2. Unit Step u(t)
unit_step = np.where(t >= 0, 1, 0)

# 3. Ramp r(t)
ramp = np.where(t >= 0, t, 0)

# 4. Exponential e^(−t)
expo = np.exp(-t) * (t >= 0)

# 5. Discrete Sine
f = 5  # frequency in Hz
sine = np.sin(2 * np.pi * f * t)

# 6. Discrete Cosine
cosine = np.cos(2 * np.pi * f * t)

# -------------------------------
# Plotting
# -------------------------------
plt.figure(figsize=(12, 12))

plt.subplot(3, 2, 1)
plt.stem(t, impulse)
plt.title("Unit Impulse δ[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.subplot(3, 2, 2)
plt.stem(t, unit_step)
plt.title("Unit Step u[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.subplot(3, 2, 3)
plt.stem(t, ramp)
plt.title("Ramp r[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.subplot(3, 2, 4)
plt.plot(t, expo)
plt.title("Exponential e^{-t} u(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")

plt.subplot(3, 2, 5)
plt.stem(t, sine)
plt.title("Discrete Sine Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.subplot(3, 2, 6)
plt.stem(t, cosine)
plt.title("Discrete Cosine Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
