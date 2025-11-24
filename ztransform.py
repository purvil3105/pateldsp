import sympy as sp

# Define symbols
n, z, a = sp.symbols('n z a', real=True)

# Define unit step function u[n]
def unit_step(n):
    return sp.Piecewise((1, n >= 0), (0, True))

# Define the impulse response h[n] = a^n * u[n]
h_n = a**n * unit_step(n)

# Compute the Z-transform manually (using summation)
H_z = sp.summation(h_n * z**(-n), (n, 0, sp.oo))  # sum from n=0 to infinity (causal)

# Simplify the result
H_z_simplified = sp.simplify(H_z)

# Display the result
print("Z-transform H(z):")
sp.pprint(H_z_simplified)

# Region of Convergence (ROC)
print("\nROC: |z| > |a|  (for convergence of causal system)")
