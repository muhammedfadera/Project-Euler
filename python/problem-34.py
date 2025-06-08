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

fact = {i:factorial(i) for i in range(11)}
#%%
# # find the largest bound 
# cond = True
# x_0 = '9'
# while cond:
