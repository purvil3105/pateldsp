import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# --- System coefficients ---
b = [2, 16, 44, 56, 32]
a = [3, 3, -15, 18, -12]

# --- Partial Fraction Expansion ---
def partial_fraction_expansion(b, a):
    poles = np.roots(a)
    zeros = np.roots(b)
    da = np.polyder(a)
    residues = []
    for pk in poles:
        Rk = np.polyval(b, pk) / np.polyval(da, pk)
        residues.append(Rk)
    return np.array(residues), np.array(poles), np.array(zeros)

residues, poles, zeros = partial_fraction_expansion(b, a)

# --- Sort poles and unique magnitudes ---
order = np.argsort(np.abs(poles))
sorted_poles = poles[order]
sorted_residues = residues[order]
unique_mags = np.unique(np.round(np.abs(sorted_poles), 4))

# --- Build ROC boundaries and types ---
ROC_mags = [0] + list(unique_mags) + [np.inf]
ROC_types = ['Anti-causal'] + ['Two-sided']*(len(unique_mags)-1) + ['Causal']
ROCs = []
ROCs.append(f"|z| < {unique_mags[0]:.4f}")
for i in range(len(unique_mags)-1):
    ROCs.append(f"{unique_mags[i]:.4f} < |z| < {unique_mags[i+1]:.4f}")
ROCs.append(f"|z| > {unique_mags[-1]:.4f}")

print("\nPoles sorted by magnitude:", sorted_poles)
print("Unique pole magnitudes:", unique_mags)
print("\nPossible ROCs and types:")
for i, (roc, typ) in enumerate(zip(ROCs, ROC_types), 1):
    print(f"ROC {i}: {roc} ({typ})")

# --- Improved Pole–Zero Plot with ROC circles and separate ROC label scale ---

plt.figure(figsize=(12, 10))
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

ax = plt.gca()
ax.set_aspect('equal')

max_radius = max(unique_mags[-1], 1) + 1
plt.xlim(-max_radius, max_radius + 3)     # extra space on right for text
plt.ylim(-max_radius, max_radius)

# Unit circle
uc = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='dashed', linewidth=1.5)
ax.add_artist(uc)

# ROC circles
colors = ['purple', 'green', 'orange', 'brown']

for i, r in enumerate(unique_mags):
    circle = plt.Circle((0, 0), r, color=colors[i % len(colors)], fill=False,
                        linestyle='dotted', linewidth=2)
    ax.add_artist(circle)

# Extra outer ROC circle
outer_r = unique_mags[-1] + 0.5
circle = plt.Circle((0, 0), outer_r, color=colors[-1], fill=False,
                    linestyle='dotted', linewidth=2)
ax.add_artist(circle)

# Poles and zeros
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', s=100, color='blue', label='Zeros')
plt.scatter(np.real(poles), np.imag(poles), marker='x', s=100, color='red', label='Poles')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xlabel('Real Part', fontsize=14)
plt.ylabel('Imaginary Part', fontsize=14)
plt.title('Pole–Zero Plot of G(z) with ROC Boundaries', fontsize=16)
plt.legend(fontsize=12)

# ------------- New Separate ROC Label Column -------------
roc_x = max_radius + 1.2   # x-position for labels
y_start = max_radius - 1   # start high on Y-axis
y_step = 1.5               # spacing

plt.text(roc_x, y_start + 1, "ROC Regions", fontsize=14, fontweight="bold")

for i, (roc, typ) in enumerate(zip(ROCs, ROC_types)):
    plt.text(roc_x, y_start - i * y_step,
             f"ROC {i+1}:\n{roc}\n({typ})",
             fontsize=11, color=colors[i % len(colors)],
             verticalalignment='top')

plt.show()



# --- Frequency Response ---
w, h = freqz(b, a, worN=1024)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(w, np.abs(h), 'b')
plt.title('Magnitude Response |H(e^{jω})|')
plt.xlabel('ω [rad/sample]')
plt.ylabel('|H(e^{jω})|')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(w, np.angle(h), 'r')
plt.title('Phase Response ∠H(e^{jω})')
plt.xlabel('ω [rad/sample]')
plt.ylabel('Phase [radians]')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Compute impulse responses for each ROC ---
n = np.arange(-20, 30)
h_rocs = []

for i in range(len(ROCs)):
    h = np.zeros_like(n, dtype=complex)
    r_min = ROC_mags[i]
    r_max = ROC_mags[i+1]
    for Rk, pk in zip(sorted_residues, sorted_poles):
        mag = np.abs(pk)
        if ROC_types[i] == 'Causal':
            # Right-sided: n >= 0
            h += Rk * (pk ** n) * (n >= 0)
        elif ROC_types[i] == 'Anti-causal':
            # Left-sided: n < 0
            h += -Rk * (pk ** n) * (n < 0)
        else:
            # Two-sided: both sides
            h += Rk * (pk ** n)
    h_rocs.append(h)

# --- Plot impulse responses with ROC types ---
plt.figure(figsize=(12, 10))
for i, h in enumerate(h_rocs):
    plt.subplot(2, 2, i+1)
    plt.stem(n, np.real(h), basefmt=" ")
    plt.title(f"ROC{i+1}: {ROCs[i]} ({ROC_types[i]})")
    plt.xlabel('n')
    plt.ylabel('h[n] (real part)')
    plt.grid(True)
plt.tight_layout()
plt.show()