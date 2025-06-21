"""
The arithmetic sequence 1487, 4817, 8147, in which each of the terms increases 
by 3330, is unusual in two ways:
(i) each of the three terms are prime, and
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""
#%%
from itertools import permutations, combinations
from time import time
t1 = time()
lower_limit = 1000
upper_limit = 9999 + 1
# using sieve of erathosthenes
prime_factor_counter = [0]*(upper_limit)
for i in range(2, upper_limit):
    if prime_factor_counter[i] == 0:
        val = i
        prime_factor_counter[val] = 1
        val += i
        while val < upper_limit:
            # if i == 5:
            #     print(val)
            prime_factor_counter[val] = -1
            val += i
break_cond = False
already_known = 1487
for i in range(lower_limit, upper_limit):
    if prime_factor_counter[i] == 1 and i != already_known:
        perm_digits_3 = combinations(permutations(str(i)), 3)
        for abc in perm_digits_3:
            a = abc[0]; b = abc[1]; c = abc[2]
            a = int("".join(a))
            b = int("".join(b))
            c = int("".join(c))
            if a != b and b != c and \
                b - a == c - b and \
                prime_factor_counter[a] == 1 and \
                prime_factor_counter[b] == 1 and \
                prime_factor_counter[c] == 1:
                res = str(a) + str(b) + str(c)
                break_cond = True
                break
    if break_cond:
        break

print(f"The result is {res}")
print(f"The arithmetic sequence is {a}, {b} and {c}", 
      f"with common difference of {b - a}")

t2 = time()
print(f"Time taken: {t2 - t1}")