import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cheb1ord, cheby1, freqz

# -----------------------------------------------------
# DIGITAL CHEBYSHEV TYPE-1 HIGH-PASS FILTER DESIGN
# -----------------------------------------------------

# Given filter specifications for DSP Lab
Fs = 1000           # Sampling frequency (Hz)
fp = 200            # Passband cutoff frequency (Hz)
fs = 100            # Stopband cutoff frequency (Hz)
Rp = 1              # Maximum passband ripple (dB)
Rs = 40             # Minimum stopband attenuation (dB)

# -----------------------------------------------------
# 1. Convert real frequencies → normalized digital freqs
#    Normalized frequency = f / (Fs/2), range = 0 to 1
# -----------------------------------------------------
wp = fp / (Fs/2)    # Passband edge (normalized)
ws = fs / (Fs/2)    # Stopband edge (normalized)

# -----------------------------------------------------
# 2. Determine minimum filter order (N) and cutoff (Wc)
#    cheb1ord() solves inequalities for ripple & attenuation:
#       |H(jw)| >= -Rp dB in passband
#       |H(jw)| <= -Rs dB in stopband
# -----------------------------------------------------
N, Wc = cheb1ord(wp, ws, Rp, Rs)
print("Chebyshev-I Highpass Filter")
print("Order       :", N)
print("Cutoff (Wc) :", Wc)

# -----------------------------------------------------
# 3. Design Chebyshev Type-1 HIGH-PASS filter
#    cheby1() returns IIR filter coefficients (b, a)
# -----------------------------------------------------
b, a = cheby1(N, Rp, Wc, btype='high')

print("\nNumerator coefficients  :", b)
print("Denominator coefficients:", a)

# -----------------------------------------------------
# 4. Compute frequency response using freqz()
#    freqz() returns:
#       w  → digital radian frequency
#       h  → complex frequency response H(e^jw)
# -----------------------------------------------------
w, h = freqz(b, a, 2048)        # 2048-point response for smooth curve

# Convert magnitude to decibels
Hdb = 20 * np.log10(np.abs(h) + 1e-9)   # avoid log(0)

# -----------------------------------------------------
# 5. Plot the frequency response
# -----------------------------------------------------
plt.figure(figsize=(10,5))
plt.plot(w/np.pi, Hdb)   # Normalize w by π → plot 0 to 1
plt.title("Chebyshev-I Digital Highpass Filter Response")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.show()
