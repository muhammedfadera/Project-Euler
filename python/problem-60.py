"""
The primes 3, 7, 109, and 673 are quite remarkable. 
By taking any two of these primes and concatenating them in any order, 
the result is always a prime. For example, taking 7 and 109, both 7109 and 1097 are prime.

The sum of these four primes, 792, represents the lowest sum for a set of four 
primes with this property.

Question:
Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.

forward and backward pass
"""
# from 
#%%
from utilities import miller_rabin
from gmpy2 import is_prime
from time import time
t1 = time()
def is_prime_from_list(x, prime_list_less_than_x):
    sqrt_x = int(x**0.5)
    for p in prime_list_less_than_x:
        if p <= sqrt_x and x % p == 0:
            return False
    return True


min_seq_length = 5
primes_forward_pass = dict()
prime_list_less_than_x = [2]
# prime_list = set([2])
k = 3
while True:
    # if is_prime_from_list(k, prime_list_less_than_x):
    # if miller_rabin(k):
    if is_prime(k):
        for p in prime_list_less_than_x:
            N = int("".join([str(p), str(k)]))
            N_rev = int("".join([str(k), str(p)]))
            # if is_prime(N):
            # if miller_rabin(N):
            if is_prime(N):
                # prime_list.add(N)
                # if is_prime(N_rev):
                # if miller_rabin(N_rev):
                if is_prime(N_rev):
                    # prime_list.add(N_rev)
                    try:
                        primes_forward_pass[k].append(p)
                    except KeyError:
                        primes_forward_pass[k] = [p]
        prime_list_less_than_x.append(k)
    k += 1
    try:
        current_prime_list_k = primes_forward_pass[k-1]
        if len(current_prime_list_k) >= min_seq_length:
            test_prime = [current_prime_list_k[0]]
            m = 1
            while m < len(current_prime_list_k):
                p_in_the_list = current_prime_list_k[m]
                cond = sum([p in primes_forward_pass[p_in_the_list] for p in test_prime])
                if cond == len(test_prime):
                    test_prime.append(p_in_the_list)
                m += 1
            if len(test_prime) == min_seq_length - 1:
                test_prime = test_prime + [k-1]
                print(f"The required list of primes is {test_prime}") 
                break
    except KeyError:
        continue

print(f"Result is {sum(test_prime)}")
print(f"Time taken: {time() - t1:.2f} seconds")
# %%
