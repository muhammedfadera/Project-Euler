"""
Euler's totient function, φ(n) [sometimes called the phi function], is defined 
as the number of positive integers not exceeding n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8 are all less than or equal to 9 and 
relatively prime to 9, φ(9) = 6.

+----+------------------------+--------+------------+
| n  | Relatively Prime       | φ(n)   | n / φ(n)   |
+----+------------------------+--------+------------+
| 2  | 1                      | 1      | 2          |
| 3  | 1, 2                   | 2      | 1.5        |
| 4  | 1, 3                   | 2      | 2          |
| 5  | 1, 2, 3, 4             | 4      | 1.25       |
| 6  | 1, 5                   | 2      | 3          |
| 7  | 1, 2, 3, 4, 5, 6       | 6      | 1.1666...  |
| 8  | 1, 3, 5, 7             | 4      | 2          |
| 9  | 1, 2, 4, 5, 7, 8       | 6      | 1.5        |
| 10 | 1, 3, 7, 9             | 4      | 2.5        |
+----+------------------------+--------+------------+
It can be seen that n = 6 produces a maximum n / φ(n) for n ≤ 10.

Problem:
Find the value of n ≤ 1,000,000 for which n / φ(n) is a maximum.
"""
#%%
from utilities import miller_rabin

def prime_hist(factors):
    res = {}
    for p in factors:
        try:
            res[p] += 1
        except KeyError:
            res[p] = 1
    return res

def euler_totient(factors):
    factors = prime_hist(factors)
    res = 1
    for (p, k) in factors.items():
        res *= (p-1)*p**(k-1)
    return res
N = 1_000_000
# N = 1_0
# primes = [p for p in range(2, N+1) if miller_rabin(p)]
# primes = list(range(2, N+1))
prime_factors = {}
coprimes = {}
max_phi_n = (0, 0)
# coprimes = {n:set(range(2, n)) for n in primes}

for n in range(2, N+1):
    if millerrabin(n):
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
        phi_n = n/euler_totient(factors_n)
        if phi_n > max_phi_n[0]:
            max_phi_n = (phi_n, n)

print(f"The maximum value of n/φ(n) for values of n <= {N} is attained at n = {max_phi_n[1]}")

# %%
