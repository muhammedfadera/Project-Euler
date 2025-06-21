"""
It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9 = 7 + 2 × 1²
15 = 7 + 2 × 2²
21 = 3 + 2 × 3²
25 = 7 + 2 × 3²
27 = 19 + 2 × 2²
33 = 31 + 2 × 1²

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime 
and twice a square?
"""
#%%
from math import isqrt, sqrt

import time
t1 = time.time()
i = 2
cond = False
prime_list = [2]
while not cond:
    # print(f"i = {i}")
    n = 2*i - 1
    i += 1
    prime_cond = True
    for p in prime_list:
        if n % p == 0:
            prime_cond = False
            break
    if prime_cond:
        prime_list.append(n)
        continue
    else:
        failed_representations = 0
        for p in prime_list:
            D, remainder = divmod(n - p, 2)
            D_sqrt = sqrt(D)
            if remainder == 0 and int(D_sqrt) - D_sqrt == 0:
                break
            else:
                failed_representations += 1
        if failed_representations == len(prime_list):
            cond = True
            
print(f"The result is {n}")
                            
t2 = time.time()
print(f"Time taken: {t2 - t1}")