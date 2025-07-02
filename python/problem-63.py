"""
The 5-digit number 16807 = 7⁵ is also a fifth power.
Similarly, the 9-digit number 134217728 = 8⁹ is a ninth power.

Question:
How many n-digit positive integers exist which are also an nᵗʰ power?
"""
#%%
from math import log10, ceil
from utilities import is_int

n_digits_upper_bound = ceil(1/(1-log10(9))) # 
counter = 0
# for base in range(2, 11):
for n_digits in range(1, n_digits_upper_bound):
    for base in range(1, 11):
        number = base**n_digits
        if len(str(number)) == n_digits:
            counter += 1
#%% another solution
sum(int(1/(1-log10(base))) for base in range(1, 10))
# print(counter)