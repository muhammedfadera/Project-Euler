"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists
"""

# from itertools
#%%
from math import isqrt
from itertools import permutations
def is_pandigital(x):
    if '0' in x:
        return False
    n = len(x)
    for i in range(1, n+1):
        if x.count(str(i)) != 1:
            return False
    return True
# taken from problem 35
def pandigital_prime(n):
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True
# def is_prime(n):
#     if n <= 3:
#         return n > 1
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     limit = isqrt(n)
#     for i in range(5, limit+1, 6):
#         if n % i == 0 or n % (i+2) == 0:
#             return False
#     return True


cond = False
# note that pandigital numbers with 1 to 9
# and 1 to 8 are all disible by 3
largest = '7654321' # largest possible pandigital number
n = 7

while not cond:
    perm_1_to_n = permutations(largest, n)
    for x in perm_1_to_n:
        x = "".join(x)
        last_digit = x[-1]
        if last_digit in ['0', '2', '4', '6', '8', '5']:
            # largest = str(int(largest) - 2)
            continue
        sum_digits = sum(int(digit) for digit in largest)
        while len(str(sum_digits)) > 1:
            sum_digits = sum(int(digit) for digit in str(sum_digits))
        if sum_digits % 3 == 0:
            # largest = str(int(largest) - 2)
            continue
        if is_pandigital(x) and pandigital_prime(int(x)):
            cond = True
            break
    n -= 1
    largest = ''
    for i in range(1, n+1):
        largest += str(i)
    largest = largest[::-1]

print(f"The largest pandigital prime number is {x}")

