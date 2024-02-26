'''
The number 197, is called a circular prime because all rotations of the digits: 
917, 719 and 971 are themselves prime.

There are thirteen such primes below 100
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 79 and 97: 


How many circular primes are there below one million?

First approach:
1. We only have to check up to 500_000. 
2. Furthermore, for n digit numbers, we only have to check up to 10**(n)/2
1. First filter out all primes other the single digits that contain the numbers
    0, 2, 4, 5, 6, 8
    because this will be divisible by 2, 5 or 10.
2. How do we avoid checking all permutations? In particular if the number is indeed a
   circular prime, then do we have to check all rotation of the digits? Is there a 
   rotation of digits that do not change the number of factors of a number? We can 
   enumerate all primes containing the digits 1, 3, 7 and 9 and check if they and their 
   reverse are primes. 
'''
#%%
import time
t = time.time()
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

def includes_others(n):
    '''
    checks if the number contains a 0, 2, 4, 6, 8 or 5
    '''
    exclude = ['0', '2', '4', '6', '8', '5']
    ix = 0
    for i in str(n):
        if i in exclude:
            return (ix, int(i))
        ix += 1
    return (-1, -1)

def all_rotations(n):
    '''
    returns the rotations of digits of n and whether all of them are prime
    input: a prime number
    '''
    str_n = str(n)
    l = len(str_n)
    if l > 1:
        str_n = str_n + str_n*(l-1)
    i = 1    
    res = [n]
    cond = 1
    while i < factorial(l):
        curr_n = int(str_n[i:(i+l)])
        cond *= is_prime(curr_n)
        if curr_n == n or (cond == 0):
            break
        res.append(curr_n)
        i += 1
    return res, cond

steps = [2, 4, 2, 2] # 11, 13, 17, 19, 31, ..
d_next = {0:1, 2:3, 4:7, 6:7, 8:9}
primes = [2, 3, 5, 7]
reset = 4
# initial_batch = {} # dictionary indexed by the number of digits in the #
initial_batch = []
MAX = 1000_000
# MAX = 100
ix = 0
n = 11 # starting from 11
exclude = []
# keeps track of the number of cyclic primes
# the initial value here is for the single digit primes
res = 4 
while n <= MAX:
    # take the digits in the number in from smallest to largest
    str_n = str(n)
    first_digit = int(str_n[0])
    ix1, d = includes_others(n)
    if ix1 != -1:
        l = len(str_n[ix1:])-1
        n = int(str_n[:ix1]+ str(d_next[d]*10**l + 1))
        continue
    # key = ''.join(sorted(str_n)) 
    # checks if the number of permutations is reached
    if (n not in exclude) and is_prime(n):
        rotations, test = all_rotations(n)
        if test:
            # initial_batch.append((n, len(rotations)))
            res += len(rotations)
        exclude.extend(rotations)
    n += steps[ix%reset]
    ix += 1
    # n += 1

print(f'The number of cyclic prime primes below {MAX} is {res}')
print(f'Time taken: {time.time()-t}')
