import numpy as np
import matplotlib.pyplot as plt
# ---------- Input Sequences ----------
x = np.random.randint(-5, 6, 1024)   # Long input signal (length 1024)
h = np.array([1, 2, 3, 2, 1])        # Impulse response (FIR filter)
# ---------- Parameters ----------
L = 8                 # Block length 
M = len(h)            # Length of h[n]
N = L + M - 1         # FFT length for linear convolution of each block
# ---------- Initialize Output ----------
y_out = np.zeros(len(x) + M - 1)  # Final linear convolution result
# ---------- Overlap-Add Processing ----------
for start in range(0, len(x), L):
    # Extract block (may be shorter at end)
    x_block = x[start:start + L]
    # Zero-pad block and impulse response
    x_pad = np.pad(x_block, (0, N - len(x_block)))
    h_pad = np.pad(h, (0, N - len(h)))
    # FFT of block & impulse response
    X = np.fft.fft(x_pad, N)
    H = np.fft.fft(h_pad, N)
    # Multiply in frequency domain
    Y_block = np.fft.ifft(X * H).real
    # Add to final output (overlap-add)
    y_out[start:start + N] += Y_block
# ---------- Verification using Direct Convolution ----------
y_direct = np.convolve(x, h)
# ---------- Plot Results ----------
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(y_out, 'r', label='Overlap-Add (DFT Method)')
plt.title('Linear Convolution using Overlap-Add Method')
plt.xlabel('n'); plt.ylabel('Amplitude'); plt.legend(); plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(y_direct, 'b', label='Direct Convolution (np.convolve)')
plt.title('Linear Convolution using Direct Method')
plt.xlabel('n'); plt.ylabel('Amplitude'); plt.legend(); plt.grid(True)

plt.tight_layout()
plt.show()
