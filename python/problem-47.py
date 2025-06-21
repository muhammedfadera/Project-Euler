"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?

# observation 
It seems no number on this can itself be prime. Otherwise the smallest such sequence 
with three numbers is 3, 4 and 5. 
"""
#%%
# from math import isqrt
from time import time
t1 = time()
max_factors = 4

prime_list = set() # sieving prime list
prime_factors = set() # keep tracks of the prime factors of the last max_factor integers
factors_of_the_first = set()
cond = True
stored_integer_prime_counter = 0
n = 1
distinct_counter = 0

from collections import OrderedDict

class CyclicDict(OrderedDict):
    def __init__(self, max_size, *args, **kwargs):
        self.max_size = max_size
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        elif len(self) >= self.max_size:
            self.popitem(last=False)  # Remove oldest
        super().__setitem__(key, value)

prime_factors_dict = CyclicDict(max_size=5000)


while True:
# while n <= 20:
    prime_cond = True
    print(f"current at n = {n}")
    prime_factors = set()
    test_primes = [p for p in prime_list if p <= n//2]
    for p in prime_list:
        q, remainder = divmod(n, p)
        if remainder == 0:
            prime_cond = False
            prime_factors.add(p)
            if q in prime_factors_dict:
                prime_factors.update(prime_factors_dict[q])
                break
    if n not in prime_factors_dict:
        prime_factors_dict[n] = prime_factors
    if prime_cond and n > 1:
        distinct_counter = 0
        prime_factors_dict[n] = set([n])
        prime_list.add(n)
        n += 1
        continue
    if len(prime_factors) == max_factors:
        distinct_counter += 1
    else:
        distinct_counter = 0
    if distinct_counter == max_factors:
        print(f"With {max_factors} distinct prime factors, n = {n-max_factors+1}")
        break
    n += 1

t2 = time()
print(f"Time taken: {t2 - t1: .2f}")

#%% smart solution from project euler's thread
# effortless implementation of sieve less than a given number

Limit=1000000     # Search under 1 million for now
factors=[0]*Limit # number of prime factors.
count=0
for i in range(2,Limit):
    if factors[i]==0:
        # i is prime
        count =0
        val =i
        while val < Limit:
            factors[val] += 1
            val+=i
    elif factors[i] == 4:
        count +=1
        if count == 4:
            print(i-3) # First number
            break
    else:
        count = 0