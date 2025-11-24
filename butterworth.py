import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfreqz

# ------------------------------
# Filter specifications
# ------------------------------
lowcut = 0.2      # Lower cutoff (normalized)
highcut = 0.5     # Upper cutoff
order = 4         # Butterworth filter order

# ------------------------------
# Design Butterworth Bandpass
# ------------------------------
sos = butter(order, [lowcut, highcut], btype='bandpass', output='sos')

print("Second Order Sections (SOS):")
print(sos)

# ------------------------------
# Frequency Response
# ------------------------------
w, h = sosfreqz(sos, worN=2000)

plt.plot(w/np.pi, 20*np.log10(np.abs(h)))
plt.title("Butterworth Bandpass IIR Filter")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.show()