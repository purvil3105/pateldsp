import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# -------------------------------
# 1. Filter Specifications
# -------------------------------
# Fs  : Sampling frequency of the digital system (in Hz)
# fp  : Desired passband edge frequency of HPF
# fs  : Desired stopband edge frequency of HPF
# Rp  : Maximum ripple allowed in passband (dB)
# Rs  : Minimum attenuation required in stopband (dB)
Fs = 1000
fp = 200
fs = 100
Rp = 1
Rs = 40

# -------------------------------
# 2. Normalized Digital Frequencies
# -------------------------------
# For digital filters frequencies must be normalized
# to the Nyquist frequency (Fs/2).
# Wp and Ws lie between 0 and 1.
Wp = fp / (Fs/2)
Ws = fs / (Fs/2)

# -------------------------------
# 3. Find Minimum Filter Order
# -------------------------------
# cheb1ord() returns:
# N  -> Minimum order of Chebyshev Type-1 filter
# Wn -> Cutoff frequency that satisfies given specs
# 'analog=False' ensures we are designing a DIGITAL filter.
N, Wn = signal.cheb1ord(Wp, Ws, Rp, Rs, analog=False)

print("Filter Order =", N)
print("Cutoff (Wn) =", Wn)

# -------------------------------
# 4. Design Chebyshev Type-1 Highpass Filter
# -------------------------------
# cheby1() designs the actual HPF using the order (N) and cutoff (Wn)
# b, a represent the numerator and denominator polynomial coefficients
# of the IIR digital filter's transfer function.
b, a = signal.cheby1(N, Rp, Wn, btype='high', analog=False)

print("\nNumerator Coefficients (b):\n", b)
print("\nDenominator Coefficients (a):\n", a)

# -------------------------------
# 5. Frequency Response Plot
# -------------------------------
# freqz() computes the discrete-time frequency response.
# w is frequency (in rad/sample), h is the complex response.
# 20*log10(|h|) gives amplitude in dB.
w, h = signal.freqz(b, a, worN=1024)

plt.figure(figsize=(10, 5))
plt.plot(w/np.pi, 20*np.log10(abs(h)))  # Convert to dB scale
plt.title("Chebyshev Type-1 High Pass Filter Response")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.show()
