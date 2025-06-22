"""
The prime 41 can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one hundred.

The longest sum of consecutive primes below one thousand that adds to a prime contains 
21 terms, and is equal to 953.

Which prime below one million can be written as the sum of the most consecutive primes?
"""
#%%
from utilities import is_prime
#%%
from time import time
t1 = time()
upper_bound = 1000_000 + 1
prime_sieve = [0]*upper_bound
consecutive_prime_sums = dict()
# sieve to find all of the primes below the upper bound
for i in range(2, upper_bound):
    if prime_sieve[i] == 0:
        prime_sieve[i] = 1
        val = 2*i
        while val < upper_bound:
            prime_sieve[val] = -1
            val += i

# there is where the checking begins
primes_below_upper_bound = [i for i in range(2, upper_bound) if prime_sieve[i] == 1]
max_ix = 0
check = primes_below_upper_bound[0]
while check <= upper_bound:
    max_ix += 1
    check += primes_below_upper_bound[max_ix]
primes_to_check = primes_below_upper_bound[:max_ix]
N = len(primes_to_check)
curr_length = 1
offset = 0
starting = 2
while offset <= N:
    initial_sum = sum(primes_to_check[offset:])
    res = initial_sum
    for j in range(N-offset-curr_length):
        if N - offset - j > curr_length:
            if j > 1:
                res -= primes_to_check[-j]
            if res <= upper_bound and prime_sieve[res] == 1:
                break_cond = True
                curr_length = N - j - offset 
                current_res = res
                starting = primes_to_check[offset]
                break
    offset += 1

print(f"The result is {current_res} with primes starting from {starting}",
      f"with length {curr_length}")
t2 = time()
print(f"Time taken: {t2 - t1}")

