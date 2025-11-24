import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def z_transform_analysis(num, den):
    """
    Perform Z-transform analysis for a given transfer function H(z).
     Parameters:
        num : list or ndarray
            Numerator coefficients of H(z)
        den : list or ndarray
            Denominator coefficients of H(z)
    """

    # ------------------- Zeros, Poles, Gain -------------------
    zeros, poles, gain = signal.tf2zpk(num, den)

    print("\n========= Z-Transform Analysis =========")
    print("Numerator (b):", num)
    print("Denominator (a):", den)
    print("Zeros:", zeros)
    print("Poles:", poles)
    print("Gain:", gain)

    # ROC
    roc = np.max(np.abs(poles))
    print(f"Region of Convergence (Causal): |z| > {roc:.4f}")

    # Frequency Response
    w, h = signal.freqz(num, den)
    mag_db = 20 * np.log10(np.abs(h))
    phase = np.unwrap(np.angle(h))

    # Plotting
    fig, ax = plt.subplots(1, 2, figsize=(13, 6))
    fig.suptitle("Z-Transform System Analysis", fontsize=15, fontweight='bold')

    # ===== LEFT: Pole-Zero Plot =====
    ax[0].set_title("Pole-Zero Plot", fontsize=13)
    ax[0].set_xlabel("Real")
    ax[0].set_ylabel("Imaginary")
    ax[0].grid(True, linestyle='--', alpha=0.6)

    # Unit circle
    uc = plt.Circle((0, 0), 1, fill=False, color='black', linestyle='--', linewidth=1.5)
    ax[0].add_artist(uc)

    # Plot zeros & poles
    ax[0].scatter(np.real(zeros), np.imag(zeros), marker='o',
                  facecolors='blue', edgecolors='cyan', s=120, label="Zeros")
    ax[0].scatter(np.real(poles), np.imag(poles), marker='x',
                  color='orange', s=140, label="Poles")

    ax[0].legend()

    # === FIX: Proper axis limits ===
    all_points = np.concatenate((zeros, poles, [1, -1, 1j, -1j]))
    limit = np.max(np.abs(all_points)) * 1.3
    ax[0].set_xlim(-limit, limit)
    ax[0].set_ylim(-limit, limit)

    ax[0].set_aspect('equal', 'box')   # ensure perfect circle

    # ===== RIGHT: Magnitude and Phase =====
    ax[1].set_title("Magnitude & Phase Response", fontsize=13)
    ax[1].set_xlabel("Normalized Frequency (×π rad/sample)")
    ax[1].set_ylabel("Magnitude (dB)", color='purple')

    ax[1].plot(w/np.pi, mag_db, linewidth=2, color='purple')
    ax[1].grid(True, linestyle='--', alpha=0.6)

    # Phase response
    axP = ax[1].twinx()
    axP.set_ylabel("Phase (radians)", color='green')
    axP.plot(w/np.pi, phase, linestyle='--', color='green', linewidth=1.8)

    plt.tight_layout()
    plt.show()


# ---------------------- Example Usage ----------------------
if __name__ == "__main__":
    num = [0.0675, 0.1349, 0.0675]
    den = [1.0, -1.14298, 0.4128]

    z_transform_analysis(num, den)
