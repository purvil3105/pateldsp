import sympy as sp
# ----- Symbol -----
z = sp.symbols('z')

# ----- Rational Z-transform H(z) -----
H = (1 - 0.5*z**(-1)) / ((1 - 0.8*z**(-1)) * (1 + 0.6*z**(-1)))
print("H(z) =", sp.simplify(H))
# ----- Convert to rational polynomial (remove negative powers) -----
H_poly = sp.together(H)  # combine numerator & denominator
k = sp.degree(sp.denom(H_poly), z) - sp.degree(sp.numer(H_poly), z)
H_rational = sp.simplify(H_poly * z**k)
print("\nH(z) in polynomial rational form =", H_rational)

# ----- Partial Fraction Expansion -----
H_pf = sp.apart(H_rational, z)
print("\nPartial Fraction Expansion of H(z):")
print(H_pf)

