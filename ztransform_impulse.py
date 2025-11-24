import sympy as sp

h_val = [3,5,1,2]
n_value = [-2,-1,0,1]

z = sp.symbols('z')
H = 0                     # accumulator for Z-transform

for h, n in zip(h_val , n_value):
    H += h * z**(-n)      # correct summation

H_simplified = sp.simplify(H)

print("\nZ-transform H(z) =", H_simplified)

n_min = min(n_value)
n_max = max(n_value)

if n_min >= 0:
    roc = "ROC: |z| ≠ 0   (causal / right-sided sequence)"
elif n_max <= 0:
    roc = "ROC: |z| ≠ ∞   (anti-causal / left-sided sequence)"
else:
    roc = "ROC: |z| ≠ 0 and |z| ≠ ∞   (non-causal / two-sided sequence)"

print("\n" + roc)

num = sp.factor(sp.numer(H_simplified))
den = sp.factor(sp.denom(H_simplified))

zero = sp.solve(num , z)
pole = sp.solve(den , z)

numer =1 
dener =1
for z0 in zero:
    numer *=(1-z0*z**(-1))
for p0 in pole:
    dener *=(1-p0*z**(-1))

H_rational = sp.simplify(numer/dener)
print("H(z) =", H_rational)
