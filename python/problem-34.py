'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

# factorial grows much faster than additions. Put a bound on the number of digits
# Can we think of the problem in terms of Problem 31 where the we consider a currency
system where the denominations are from 1 to 9! and we are seeking for numbers 
which are equal to some ordering of the digits its representation including repeats. 
# use a directed graph with nodes encoded by (p, d) the place value d, and the digit 
itself d. Maybe breadth first search?
'''

#%%
from math import factorial
from math import comb

fact = {i:factorial(i) for i in range(10)}

def factorial_digit_sum(N): return sum(fact[int(d)] for d in str(N))

#%%
# def isFactorial_sum(n):
N = 11
# while True:
n_digits = 2
N = int('1' + (n_digits-1)*'0')
res = 0
factorial_digits = []
while N <= 100000:
    if str(N) == '5'*n_digits:
        n_digits += 1
        N = int('1' + (n_digits-1)*'0')
    else:
        N_fact = factorial_digit_sum(N)
        if N_fact == N:
            # print("we are here")
            factorial_digits.append(N)
            res += N
    # elif len(str(N_fact)) > len(str(N)):
    #     n_digits += 1
    #     N = int('1' + (n_digits-1)*'0')
    # else:
    N += 1
print(f"The set of such numbers {factorial_digits} with sum {res}")
