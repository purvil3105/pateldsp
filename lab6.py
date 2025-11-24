import numpy as np
import matplotlib.pyplot as plt

# Given impulse response
h = [1, 2, 3, 4, 5]

# ---------------- Z-TRANSFORM ----------------
def z_transform(h, z):
    H = 0
    for n in range(len(h)):
        H += h[n] * z**(-n)
    return H

# Print symbolic Z-transform
print("Z-Transform H(z) = ", end="")
for i in range(len(h)):
    if i == 0:
        print(f"{h[i]}", end="")
    else:
        print(f" + {h[i]}z^-{i}", end="")
print("\n")

# ---------------- MAGNITUDE vs |z| ----------------
z_values = np.linspace(0.1, 2, 100)
H_mag = []

for z in z_values:
    H_mag.append(abs(z_transform(h, z)))

plt.plot(z_values, H_mag)
plt.title("Magnitude of H(z) vs |z|")
plt.xlabel("|z|")
plt.ylabel("|H(z)|")
plt.grid(True)
plt.show()

# ---------------- ROC VISUALIZATION ----------------
theta = np.linspace(0, 2*np.pi, 400)
unit_circle = np.exp(1j * theta)

plt.plot(unit_circle.real, unit_circle.imag, label="Unit Circle")
plt.fill(unit_circle.real*3, unit_circle.imag*3, color='lightgreen', alpha=0.3,
         label="ROC: |z| > 0")
plt.scatter(0, 0, color='red', marker='x', label="Excluded Point z=0")

plt.title("ROC for Finite-Length Causal Sequence")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()

print("ROC: |z| > 0 (Entire z-plane except origin)")
print("System Type: Causal FIR System")
