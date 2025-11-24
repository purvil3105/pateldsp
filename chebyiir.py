import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cheby1, sosfilt, sosfreqz

# -------------------------------------------------------
# Filter Specifications (You can change these)
# -------------------------------------------------------
Rp = 1          # passband ripple (dB)
wp = 0.4        # passband edge (normalized: 1 = Nyquist)
ws = 0.2        # stopband edge (normalized)
As = 40         # stopband attenuation (dB)

# -------------------------------------------------------
# Step 1: Compute Minimum Filter Order
# -------------------------------------------------------
from scipy.signal import cheb1ord

N, Wn = cheb1ord(wp, ws, Rp, As)
print("Filter order N:", N)
print("Critical frequency Wn:", Wn)

# -------------------------------------------------------
# Step 2: Design Chebyshev Type-1 Highpass Filter
# -------------------------------------------------------
sos = cheby1(N, Rp, Wn, btype='highpass', output='sos')

print("\nSecond Order Sections:")
print(sos)

# -------------------------------------------------------
# Step 3: Frequency Response
# -------------------------------------------------------
w, h = sosfreqz(sos, worN=2000)

plt.plot(w/np.pi, 20*np.log10(abs(h)))
plt.title("Chebyshev Type-1 IIR High-pass Filter")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.show()
