"""
collection of functions that keeps appearing
"""
from math import isqrt

def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


def check_composite(n, a, d, r):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(r - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return False
    return True

def miller_rabin(n):
    if n < 2:
        return False
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if a >= n:
            continue
        if check_composite(n, a, d, r):
            return False
    return True

is_palindromic = lambda x: str(x) == str(x)[::-1]
triangular = lambda n: int(n*(n+1)/2)
square = lambda n: int(n**2)
pentagonal = lambda n: int(n*(3*n-1)/2)
hexagonal = lambda n: int(n*(2*n-1))
heptagonal = lambda n: int(n*(5*n - 3)/2)
octagonal = lambda n: int(n*(3*n - 2))