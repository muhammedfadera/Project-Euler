'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, 
 may not include leading zeros.)

 1. Find Palindromes in base 10 and convert them to base to using 
 an base 2 conversion algorithm that can give both the from and last digits 
'''
#%%
import math as m
import time
t = time.time()
def is_palindromic(x: str) -> bool:
    # l = len(str_x)
    return x == x[::-1]

MAX = int(1e6)
# x = [i for i in range(100, MAX + 1) if i%10 != 0]
res = 0
res_list = []
x = range(1, MAX + 1, 2)
for n in x:
    str_n = str(n)
    if (str_n[0] != str_n[-1]):
        continue
    elif is_palindromic(str_n) and is_palindromic(bin(n)[2:]):
        res += n
        res_list.append((n, bin(n)[2:]))

print(f"The sum of all numbers, less than one {MAX}",\
        f"which are palindromic in base 10 and base 2 is {res}")
print(f"time taken {time.time() - t} seconds")
# %%
