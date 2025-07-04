"""
Consider quadratic Diophantine equations of the form:

  x² − D·y² = 1

For example, when D = 13, the minimal solution in x is:

  649² − 13 × 180² = 1

It can be assumed that there are no solutions in positive integers when D is a perfect square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

  3² − 2 × 2² = 1
  2² − 3 × 1² = 1
  9² − 5 × 4² = 1 ← largest x among these
  5² − 6 × 2² = 1
  8² − 7 × 3² = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D = 5.

Question:
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

# using https://en.wikipedia.org/wiki/Pell%27s_equation
"""
#%%
from utilities import is_int, sqrt_continued_fraction

# def minimal_x(D):
#     y = 1
#     while (not is_int((D*y**2 + 1)**0.5)):
#         y += 1
#     x = int((D*y**2 + 1)**0.5)
#     return x

def minimal_x(D):
    c_fraction = sqrt_continued_fraction(D)
    A = c_fraction[0]
    B = c_fraction[1]
    lB = len(B)
    if lB % 2 != 0:
        B = 2*B
    a, b = 1, B[-2]  # a/b
    for e_n in B[:-2][::-1]:
        a, b = b, b*e_n + a
    # (x, y) = (A*b + a, b) 
    x = A*b + a
    return x
N = 1000
x0 = -1
idx = -1
for D in range(2, N+1):
    if not is_int(D**0.5):
        x = minimal_x(D)
        if x > x0:
            x0 = x
            idx = D
print(f"The largest smallest solution corresponds to {idx}")

# %%
