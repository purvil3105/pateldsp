import numpy as np

# -----------------------------
# 1) COMPLEX EXPONENTIAL
# -----------------------------

n = np.arange(0, 20)                 # time index
r = 0.9                              # magnitude
omega = 0.4 * np.pi                  # frequency

# complex exponential
x = (r ** n) * np.exp(1j * omega * n)

# real and imaginary parts
x_real = np.real(x)
x_imag = np.imag(x)

print("Real part of x[n]:")
print(x_real)

print("\nImaginary part of x[n]:")
print(x_imag)


# -----------------------------
# 2) IMPULSE RESPONSE
# -----------------------------

h1 = np.array([0.6, 0.3, 0.1])
h2 = np.array([1.0, -0.5, 0.25, 0.125])

# impulse (delta)
delta = np.array([1.0])

# convolving with delta gives the impulse response
y_imp_h1 = np.convolve(delta, h1)
y_imp_h2 = np.convolve(delta, h2)

print("\nImpulse Response of h1:")
print(y_imp_h1)

print("\nImpulse Response of h2:")
print(y_imp_h2)


# -----------------------------
# 3) STEP RESPONSE
# -----------------------------

u = np.ones(20)    # unit step of length 20

y_step_h1 = np.convolve(h1, u)
y_step_h2 = np.convolve(h2, u)

print("\nStep Response of h1:")
print(y_step_h1)

print("\nStep Response of h2:")
print(y_step_h2)
