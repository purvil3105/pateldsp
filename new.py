import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# Given impulse response
h = np.array([1, 2, 3, 4, 5, 6, 7])
n_samples = len(h)


# Display symbolic Z-transform
print("\nImpulse Response h[n]:", h)
print("\nZ-Transform H(z) = ", end="")
for i in range(n_samples):
    term = f"{h[i]}z^(-{i})"
    print(term + (" + " if i < n_samples-1 else ""), end="")
print("\n")


# Compute Z-transform magnitude vs |z|
z_mag = np.linspace(0.1, 2, 200)
H_mag = []


for z_val in z_mag:
    H = sum(h[n] * (z_val ** (-n)) for n in range(n_samples))
    H_mag.append(abs(H))


# ROC for finite-length causal sequence: |z| > 0 (except possibly z=0)
print("ROC: |z| > 0 (entire z-plane except possibly z=0)")
print("System Type: Causal, Finite-length (FIR)")


# Plot magnitude response
fig, axes = plt.subplots(1, 2, figsize=(14, 5))


axes[0].plot(z_mag, H_mag, 'b-', linewidth=2)
axes[0].axvline(1, color='r', linestyle='--', alpha=0.5, label='|z|=1 (Unit Circle)')
axes[0].set_title("Magnitude of H(z) vs |z|", fontsize=13, fontweight='bold')
axes[0].set_xlabel("|z|", fontsize=11)
axes[0].set_ylabel("|H(z)|", fontsize=11)
axes[0].grid(True, alpha=0.6)
axes[0].legend()


# ROC visualization
theta = np.linspace(0, 2*np.pi, 400)
unit_circle = np.exp(1j * theta)


axes[1].plot(unit_circle.real, unit_circle.imag, 'b-', linewidth=2, label='Unit Circle')
axes[1].fill(unit_circle.real*3, unit_circle.imag*3, color='lightgreen',
             alpha=0.3, label='ROC: |z|>0')
axes[1].scatter([0], [0], s=100, c='red', marker='x', linewidth=3,
                label='Excluded: z=0', zorder=5)
axes[1].set_title("Region of Convergence (ROC)", fontsize=13, fontweight='bold')
axes[1].set_xlabel("Re{z}", fontsize=11)
axes[1].set_ylabel("Im{z}", fontsize=11)
axes[1].axis('equal')
axes[1].grid(True, alpha=0.6)
axes[1].legend()
axes[1].set_xlim(-3.5, 3.5)
axes[1].set_ylim(-3.5, 3.5)


plt.tight_layout()
plt.show()