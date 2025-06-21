"""
The series 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.

Find the last ten digits of the series 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.
"""
#%%
# simple properties of modulo arithmetic
res = 0
k = 1
n_digits = 10
p = 10**n_digits
last_pow = 1000
while k <= last_pow:
    res += (k % p)**k
    res = res % p
    k += 1

print(res)