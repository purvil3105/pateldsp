import numpy as np
import matplotlib.pyplot as plt

# -------- USER INPUT --------
zeros = [0.5, -0.8]          # change as needed
poles = [0.7, -0.6]          # change as needed
gain = 2

# -------- FORM RATIONAL Z-TRANSFORM --------
z = np.poly1d([1, 0])        # variable z

num = gain
for z0 in zeros:
    num = num * (z - z0)

den = 1
for p0 in poles:
    den = den * (z - p0)

print("Rational Z-Transform H(z):\n")
print("H(z) =")
print("-----------------")
print(num)
print("-----------------")
print(den)

# -------- ROC (for causal system) --------
roc = max(abs(p) for p in poles)
print(f"\nROC : |z| > {roc}")

# -------- PLOT POLE-ZERO DIAGRAM --------
plt.figure(figsize=(6,6))

# Unit circle
theta = np.linspace(0, 2*np.pi, 400)
unit_circle = np.exp(1j*theta)
plt.plot(unit_circle.real, unit_circle.imag, 'k--', label="Unit Circle")

# Plot zeros
plt.scatter(np.real(zeros), np.imag(zeros), 
            marker='o', s=120, edgecolors='blue',
            facecolors='none', label="Zeros")

# Plot poles
plt.scatter(np.real(poles), np.imag(poles), 
            marker='x', s=120, color='red', label="Poles")

# Plot ROC boundary
roc_circle = plt.Circle((0,0), roc, color='green', fill=False, 
                        linestyle='--', label="ROC Boundary")
plt.gca().add_artist(roc_circle)

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.title("Pole-Zero Plot with ROC")
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
