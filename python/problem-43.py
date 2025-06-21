"""
The number 1406357289 is a 0 to 9 pandigital number because it is made up of each 
of the digits 0 to 9 in some order, but it also has a rather interesting sub-string 
divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

* d2d3d4 = 406 is divisible by 2
* d3d4d5 = 063 is divisible by 3
* d4d5d6 = 635 is divisible by 5
* d5d6d7 = 357 is divisible by 7
* d6d7d8 = 572 is divisible by 11
* d7d8d9 = 728 is divisible by 13
* d8d9d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
# the property: 
# 1. being 0 to 9 pandigital
# 2. substrings be divisible by first prime numbers
"""
#%%
largest_pandigital = '9876543210'
from itertools import permutations

perm_0_to_9 = permutations(largest_pandigital, 10)

result = 0
for n in perm_0_to_9:
    if int("".join(n[-3:])) % 17 == 0 and \
       int("".join(n[-4:-1])) % 13 == 0 and \
       int("".join(n[-5:-2])) % 11 == 0 and \
       int("".join(n[-6:-3])) % 7 == 0 and \
       int("".join(n[-7:-4])) % 5 == 0 and \
       int("".join(n[-8:-5])) % 3 == 0 and \
       int("".join(n[-9:-6])) % 2 == 0:
        result += int("".join(n))
    else:
        continue
print(f"The sum of all 0 to 9 pandigital numbers with this property is {result}")


