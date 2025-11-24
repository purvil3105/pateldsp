import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import sympy as sp

def inverse_z_transform_partial_fraction(num, den, n_samples=15, tol=1e-12, causal=True):
    """
    Compute partial fractions of H(z), inverse Z-transform x[n], 
    correct pole-zero plot, and ROC shading.
    """

    # -------------------------------------------------------
    # TRUE poles and zeros from polynomials
    # -------------------------------------------------------
    true_zeros = np.roots(num)
    true_poles = np.roots(den)

    # -------------------------------------------------------
    # Residues for inverse transform
    # -------------------------------------------------------
    residues, poles_res, direct_term = signal.residuez(num, den)

    # Remove extremely tiny residues from x[n] computation (NOT PLOTTING)
    mask = np.abs(residues) > tol
    residues_clean = residues[mask]
    poles_clean = poles_res[mask]

    # -------------------------------------------------------
    # ROC from TRUE poles
    # -------------------------------------------------------
    if causal:
        roc_val = np.max(np.abs(true_poles))
    else:
        roc_val = np.min(np.abs(true_poles))

    roc_string = f"|z| {'>' if causal else '<'} {roc_val:.4f}"

    # -------------------------------------------------------
    # Numeric inverse Z-transform
    # -------------------------------------------------------
    n = np.arange(n_samples)
    x_numeric = np.sum([r * (p ** n) for r, p in zip(residues_clean, poles_clean)], axis=0)

    # Direct terms (if polynomial component exists)
    if len(direct_term) > 0:
        x_numeric[:len(direct_term)] += direct_term

    # -------------------------------------------------------
    # Symbolic inverse Z-transform
    # -------------------------------------------------------
    n_sym = sp.Symbol("n", integer=True, nonnegative=True)
    u = sp.Function("u")

    x_symbolic = sum(sp.N(r) * (sp.N(p) ** n_sym) * u(n_sym)
                     for r, p in zip(residues_clean, poles_clean))

    # Direct terms (symbolic)
    if len(direct_term) > 0:
        for i, k in enumerate(direct_term):
            x_symbolic += sp.N(k) * u(n_sym - i)

    # -------------------------------------------------------
    # PRINT OUTPUT
    # -------------------------------------------------------
    print("\n==== TRUE ZEROS ====")
    print(true_zeros)

    print("\n==== TRUE POLES ====")
    print(true_poles)

    print("\n==== RESIDUE EXPANSION (used for x[n]) ====")
    for i, (r, p) in enumerate(zip(residues_clean, poles_clean)):
        print(f"r[{i}] = {r:.6f},   p[{i}] = {p:.6f}")

    print("\n==== SYMBOLIC x[n] ====")
    sp.pprint(sp.Eq(sp.Symbol("x[n]"), x_symbolic))

    print("\n==== NUMERIC x[n] ====")
    for i, v in enumerate(x_numeric):
        print(f"x[{i}] = {np.real_if_close(v):.6f}")

    print("\nROC =", roc_string)

    # -------------------------------------------------------
    # PLOTS
    # -------------------------------------------------------
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))

    # --- x[n] plot ---
    ax[0].stem(n, np.real_if_close(x_numeric), basefmt=" ")
    ax[0].set_title("Inverse Z-transform x[n]")
    ax[0].set_xlabel("n")
    ax[0].set_ylabel("x[n]")
    ax[0].grid(True, linestyle="--", alpha=0.5)

    # --- pole-zero plot ---
    ax[1].scatter(true_zeros.real, true_zeros.imag,
                  edgecolors='blue', facecolors='none', s=120, label="Zeros")
    ax[1].scatter(true_poles.real, true_poles.imag,
                  color='red', marker='x', s=120, label="Poles")

    # unit circle
    th = np.linspace(0, 2 * np.pi, 500)
    ax[1].plot(np.cos(th), np.sin(th), 'k--')

    # axis scaling
    R = max(1.5, 1.3 * np.max(np.abs(np.concatenate([true_zeros, true_poles]))))
    ax[1].set_xlim(-R, R)
    ax[1].set_ylim(-R, R)

    # ROC shading
     # --- pole-zero plot ---
    # ROC shading first (sent to background)
        # --- pole-zero plot (with axes) ---

    # Draw ROC shading first (background)
    if causal:
        ax[1].add_patch(plt.Circle((0, 0), R, color="#cce5ff", alpha=0.30, zorder=0))
        ax[1].add_patch(plt.Circle((0, 0), roc_val, color="white", zorder=1))
    else:
        ax[1].add_patch(plt.Circle((0, 0), roc_val, color="#cce5ff", alpha=0.30, zorder=0))

    # Plot zeros
    ax[1].scatter(
        true_zeros.real, true_zeros.imag, 
        edgecolors='blue', facecolors='none',
        s=140, linewidths=2, label="Zeros", zorder=5
    )

    # Plot poles (always visible)
    ax[1].scatter(
        true_poles.real, true_poles.imag, 
        color='red', marker='x', s=160, linewidths=3, label="Poles", zorder=6
    )

    # Unit circle
    th = np.linspace(0, 2*np.pi, 500)
    ax[1].plot(np.cos(th), np.sin(th), 'k--', linewidth=1, zorder=4)

    # ===== X and Y axes =====
    ax[1].axhline(0, color="black", linewidth=1.2, zorder=10)  # x-axis
    ax[1].axvline(0, color="black", linewidth=1.2, zorder=10)  # y-axis

    # axis scaling
    ax[1].set_xlim(-R, R)
    ax[1].set_ylim(-R, R)
    ax[1].set_aspect("equal")

    ax[1].grid(True, linestyle="--", alpha=0.5)
    ax[1].legend()
    ax[1].set_title("Pole–Zero Plot with ROC")
    ax[1].set_xlabel("Real Axis")
    ax[1].set_ylabel("Imag Axis")
    plt.tight_layout()
    plt.show()

    return x_numeric, roc_string


# -------------------------------------------------------
# ★★★ Example Input (NUM, DEN) HERE ★★★
# -------------------------------------------------------
if __name__ == "__main__":

    # YOUR INPUT TRANSFER FUNCTION:
    # H(z) = (1 – 0.4 z⁻¹ + 0.6 z⁻² – 0.2 z⁻³)
    #        ---------------------------------
    #        (1 – 1.5 z⁻¹ + 1.2 z⁻² – 0.5 z⁻³ + 0.08 z⁻⁴)

    num = [1, -0.4, 0.6, -0.2]
    den = [1, -1.5, 1.2, -0.5, 0.08]

    inverse_z_transform_partial_fraction(num, den, causal=True)
