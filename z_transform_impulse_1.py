import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
h_value = [1, -3, 2]      
n_value = [0, 1, 2]       
z = sp.Symbol('z')
H = 0
for h, n in zip(h_value, n_value):
    H += h * z**(-n)
print("Z-Transform H(z) =", H)
H_simplified = sp.simplify(H)
n_min = min(n_value)
if n_min >= 0:
    print("\nROC: |z| > 0  (causal sequence)")
else:
    print("\nROC depends on value of n")

H_poly = sp.simplify(H*z**max(n_value))

num_coeff = sp.poly(sp.numer(H_poly) ,z).all_coeffs()
den_coeff = sp.poly(z**max(n_value) ,z).all_coeffs()

num_coeff = np.array([float(c) for c in num_coeff])
den_coeff = np.array([float(c) for c in den_coeff])

print("\nNumerator coefficients =", num_coeff)
print("Denominator coefficients =", den_coeff)
# Find zeros and poles
zeros_np, poles_np, gain = signal.tf2zpk(num_coeff, den_coeff)
print("\nZeros =", zeros_np)
print("Poles =", poles_np)

# ---------------------------------------------------------
# Reconstruct H(z) correctly from poles and zeros
# ---------------------------------------------------------
numer = 1
denom = 1   
# (z - zero) form
for zo in zeros_np:
    numer *= (1 - zo * z**(-1))
# (z - pole) form
for po in poles_np:
    denom *= (1 - po * z**(-1))
H_rational = sp.simplify(numer / denom)
print("\nRational H(z) reconstructed from poles & zeros =")
print(H_rational)

#--- pole -zero and frequnecy 
# ================= PLOTS: Pole-Zero + Frequency Response =================

w,h = signal.freqz(num_coeff, den_coeff)
mag_db = 20 * np.log10(np.abs(h))
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.title("Pole–Zero Plot")
circle = plt.Circle((0,0) , 1 , fill =False , linestyle='--' , color ='gray')
plt.gca().add_patch(circle)
plt.scatter(np.real(zeros_np) , np.imag(zeros_np) ,  marker='o' , s=120 , label='Zeros')
plt.scatter(np.real(poles_np) , np.imag(poles_np) ,  marker='x' , s=140 , label='Poles')
plt.grid(True)
plt.axis('equal')
plt.subplot(2, 1, 2)
plt.plot(w/np.pi , mag_db)
plt.title("Frequency Response")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.tight_layout()
plt.show()

