"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed:
   {37}  36   35   34   33   32  {31}
    38  {17}  16   15   14  {13}  30
    39   18  {5}    4  {3}   12   29
    40   19   6   {1}   2    11   28
    41   20  {7}    8   9    10   27
    42   21   22   23   24   25   26
   {43}  44   45   46   47   48  {49}

It is interesting to note that the odd squares (1, 9, 25, 49, ...) lie along the 
bottom-right diagonal.

More interestingly, 8 out of the 13 numbers lying along both diagonals are prime numbers, 
which gives a prime ratio of 8 out of 13, or approximately 61.5%.

When one complete new layer is wrapped around the spiral above, a new square 
spiral with side length 9 is formed.

If this process is continued, adding new layers to increase the side length by 2 
each time (9, 11, 13, ...), at what side length does the ratio of primes along 
both diagonals first fall below 10%?
"""
#%%
# from utilities import is_prime
from gmpy2 import is_prime
# from utilities import miller_rabin as is_prime
from time import time
t1 = time()
n_diagonal = 1 # the one at the start
n_sides = 1
prime_proportion = 1.0
n_primes = 0
while prime_proportion >= 0.1:
    n_sides += 2
    square_corner = n_sides**2
    # for k in range(1, 4):
    #     p = square_corner + k*(- n_sides+1)
    #     if is_prime(p):
    #         n_primes += 1
    n_primes += sum([is_prime(square_corner + k*(- n_sides+1)) for k in range(1, 4)])
    n_diagonal += 4
    prime_proportion = n_primes/n_diagonal

print("The side length at which the proportion of primes on",
      f"the diagonal falls below 10 percent is {n_sides}")
print(f"Time taken: {time() - t1: .2f} seconds")

# %%
