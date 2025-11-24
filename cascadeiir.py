import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfreqz

# -----------------------------------------------------
# Function: quantize a coefficient to fixed-point
# -----------------------------------------------------
def quantize(x, bits=8):
    # signed fixed point: Q(bits-1)
    step = 2**(-(bits-1))
    return np.round(x / step) * step


# -----------------------------------------------------
# Step 1: Design a Butterworth IIR Low-Pass Filter
# -----------------------------------------------------
order = 6
cutoff = 0.3   # normalized cutoff

sos = butter(order, cutoff, output='sos')

print("Original SOS (Cascade form):\n", sos)

# -----------------------------------------------------
# Step 2: Quantize the filter coefficients
# -----------------------------------------------------
bits = 8   # try 8-bit fixed-point
sos_q = quantize(sos, bits)

print("\nQuantized SOS:\n", sos_q)

# -----------------------------------------------------
# Step 3: Compute frequency responses
# -----------------------------------------------------
w, h = sosfreqz(sos, worN=2000)
_, hq = sosfreqz(sos_q, worN=2000)

# -----------------------------------------------------
# Step 4: Plot magnitude response comparison
# -----------------------------------------------------
plt.plot(w/np.pi, 20*np.log10(abs(h)), label='Original')
plt.plot(w/np.pi, 20*np.log10(abs(hq)), '--', label=f'Quantized ({bits}-bit)')
plt.title("Coefficient Quantization Effect on IIR Cascade Filter")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.legend()
plt.show()
