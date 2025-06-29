"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
the nine possible values — 13, 23, 43, 53, 73, and 83 — are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
Consequently, 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
 with the same digit, is part of an eight prime value family.
"""
# approach
# find primes and start swapping their digits
# We will start with 5 digit numbers
# We start with replacing 1 digit, then 2, then 3 and so on. 
#%%
# from utilities import is_prime
from gmpy2 import is_prime
# from utilities import miller_rabin as is_prime
from itertools import permutations
from time import time
t1 = time()
def str_replace(x, y, a):
    # for s in y:
    res = ''
    for i in range(len(x)):
        if i in y:
            res += a
        else:
            res += x[i]
    return res



start = 56993 + 1
# start = 9999 + 1
# start = 10
x = start
n_family = 8
n_family_found = 0
n_digits = len(str(start))
break_cond = False
# checked = {}
primes_checked = {}
while n_family_found < n_family:
    if is_prime(x):
        primes_checked[x] = True
        str_x = str(x)
        n_digits = len(str_x)
        for n in range(1, n_digits):
            positions = permutations(range(n_digits), n)
            if positions.__sizeof__() >= n_family:
                positions = list(positions)
                for idx in positions:
                    n_family_found = 0
                    primes_found = []
                    checked = set()
                    for y in range(10): # digits to replace
                    # checked = set()
                        N = str_replace(str_x, idx, str(y))
                        # if x == 13:
                        #     print(list(positions))
                        #     n_family_found = 10
                        #     break
                        # if x == 13:
                        if len(N) == len(str(int(N))) and N not in checked: # prevent checking numbers like 01 and 1
                                # print(N)
                            # print(str_x, N, idx, str(y))
                            cond = False
                            try:
                                cond = primes_checked[int(N)]
                            except KeyError:
                                # if N[-1] in ['0', '2', '4', '6', '8', '5'] or \
                                #     any([int(N[-j:]) % 2**j == 0 for j in range(2, 7)]) or \
                                #     sum(int(d) for d in N) % 3 == 0:
                                #     # int(N[-2:]) % 4 == 0 or \
                                #     # int(N[-3:]) % 8 == 0 or \
                                #     # int(N[-4:]) % 16 == 0 or \
                                #     # int(N[-5:]) % 64 == 0 or \
                                #         cond = False
                                #         primes_checked[int(N)] = cond
                                #         continue
                                # #     elif is_prime(int(N)):
                                # #         cond = True
                                # else:
                                    # cond = prime_sieve[int(N)] == 1
                                cond = is_prime(int(N))
                                primes_checked[int(N)] = cond
                            if cond:
                                n_family_found += 1
                                primes_found.append(int(N))
                            if n_family_found == n_family:
                                print(f"we have found {primes_found[0]} at indices {idx}")
                                break_cond = True
                                break
                            checked.add(N)
                    if break_cond:
                        break
                if break_cond:
                    break
            if break_cond:
                break
    x += 1
                 
print(f"Time taken: {time() - t1}")
# %%
