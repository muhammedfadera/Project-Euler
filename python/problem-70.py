"""
Euler's totient function, φ(n) [sometimes called the phi function], is used to 
determine the number of positive numbers less than or equal to n which are 
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8 are all less 
than nine and relatively prime to nine, φ(9) = 6. The number 1 is 
considered to be relatively prime to every positive number, so φ(1) = 1.

Interestingly, φ(87109) = 79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10⁷, for which φ(n) is a permutation of n and the ratio n / φ(n) is a minimum.
"""
#%%
from utilities import is_permutation, miller_rabin, euler_totient


N = 10**7
# N = 1_0
# primes = [p for p in range(2, N+1) if miller_rabin(p)]
# primes = list(range(2, N+1))
prime_factors = {}
coprimes = {}
min_phi_n = (N, 0)
# coprimes = {n:set(range(2, n)) for n in primes}

for n in range(2, N+1):
    if miller_rabin(n):
        prime_factors[n] = [n]
        # coprimes[n] = n - 1
    else:
        # for (k, v) in prime_factors.items():
        for k in prime_factors:
            if n % k == 0:
                factors_n = [k] + prime_factors[n//k]
                # factors_n.update(prime_factors[n // k])
                prime_factors[n] = factors_n
                break
        phi_n = int(euler_totient(factors_n))
        if is_permutation(str(n), str(phi_n)) and n/phi_n < min_phi_n[0]:
            min_phi_n = (n/phi_n, n)

print(f"The minimum value of n/φ(n) for values of n <= {N} is attained at n = {min_phi_n[1]}")

# %%

