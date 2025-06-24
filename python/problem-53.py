"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation:
C(5, 3) = 10

In general:
C(n, r) = n! / (r! × (n - r)!)
where r ≤ n,
n! = n × (n - 1) × ... × 3 × 2 × 1,
and 0! = 1.

It is not until n = 23 that a value exceeds one million:
C(23, 10) = 1144066

How many, not necessarily distinct, values of C(n, r) for 1 ≤ n ≤ 100 
are greater than one million?
"""
#%%
from time import time
from functools import lru_cache
@lru_cache
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

def n_choose_r(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

t1 = time()
N = 100
lower_bound = 10**6
n = 2
res = 0
while n <= N:
    r = -1
    turning_point = int(n/2 * (n % 2 == 0) + (n//2 + 1)*(n % 2 == 1))
    while r < turning_point: 
        r += 1
        if n_choose_r(n, r) > lower_bound:
            res += n - 2*r + 1
            break
    n += 1
print(f"The result is {res}")
print(f"Time taken: {time() - t1 :.2f}")