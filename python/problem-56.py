"""
A googol (10^100) is a massive number: one followed by one hundred zeros.
100^100 is almost unimaginably large: one followed by two hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form a^b, where a and b are both less 
than 100, what is the maximum digital sum?
"""
#%%
from math import log10
N = 100
maximal_digital_sum = 0
A = 0; B = 0
for a in range(N+1, 1, -1):
    for b in range(N + 1, 1, -1):
        if int(b*log10(a)) + 1 >= len(str(maximal_digital_sum)):
            digital_sum = sum(int(d) for d in str(a**b))
            if digital_sum > maximal_digital_sum:
                maximal_digital_sum = digital_sum
                A = a; B = b
print(f"Maximal digital sum is {maximal_digital_sum} at a = {A} and b = {B}")

# one liner 
print( max(map(lambda x: sum(int(c) for c in str(x)),
	set(a**b for a in range(2, 101) for b in range(2, 101)))))