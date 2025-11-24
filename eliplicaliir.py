import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ellip, ellipord, sosfreqz

# ---------------------------------------------------
# Filter Specifications (change if needed)
# ---------------------------------------------------
Rp = 1          # Passband ripple (dB)
Rs = 40         # Stopband attenuation (dB)
wp = 0.3        # Passband edge (normalized, 1 = Nyquist)
ws = 0.5        # Stopband edge

# ---------------------------------------------------
# Step 1: Compute minimum filter order
# ---------------------------------------------------
N, Wn = ellipord(wp, ws, Rp, Rs)

print("Elliptic LPF order:", N)
print("Critical Wn:", Wn)

# ---------------------------------------------------
# Step 2: Design Elliptic IIR LPF
# ---------------------------------------------------
sos = ellip(N, Rp, Rs, Wn, btype='lowpass', output='sos')

# ---------------------------------------------------
# Step 3: Frequency response
# ---------------------------------------------------
w, h = sosfreqz(sos, worN=2000)

plt.plot(w/np.pi, 20*np.log10(abs(h)))
plt.title("Elliptic IIR Low-Pass Filter")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.show()
