"""
Take 192 the number and multiply it by each of 1, 2 and 3:

    192 X 1 = 192
    192 X 2 = 384
    192 X 3 = 576
 
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
call 192384576 the concatenated product of 192 and (1, 2, 3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 
5, giving the pandigital 918273645, which is the concatenated product of 9 and 
(1, 2, 3, 4, 5).

What is the largest 1 to 9 pandigital 9-digit (containing the digits 1 to 9?) number that can be formed as the 
concatenated product of an integer with (1, 2, ..., n) where n > 1?
"""
#%%
# pandigital factorisation?
# pandnditial prime numbers
# start with the largest 9 digi

from itertools import permutations
one_to_9 = list(range(1, 10))
import random
def check_pandigital(x):
    if x == "" or '0' in x or len(x) != 9:
        return False
    random.shuffle(one_to_9)
    for i in one_to_9:
        if x.count(str(i)) != 1:
            return False
    return True

import time
t1 = time.time()
largest_cond = False
perm_1_to_9 = permutations(
    ['9', '8', '7', '6', '5', '4', '3', '2', '1'], 9)
comp_num = '918273645'
while not largest_cond:
    x = "".join(next(perm_1_to_9))
    for base_num_ix in range(1, 9):
        base_num = int(x[:base_num_ix])
        for n in range(3, 10):
            num = str(base_num)
            for start_n in range(2, n):
                # if len(start_num) > 9:
                #     break
                num += str(base_num*start_n)
                if '0' in num or len(num) > 9:
                    break

                # comp_cond = False
                # for i in range(1, len(num)):
                #     if int(num[:i]) < int(comp_num[:i]):
                #         comp_cond = True
                #         break
                # if comp_cond:
                #     break
            # print(num)
            if (int(num) > 918273645) and check_pandigital(num):
                largest_cond = True
                break
        if largest_cond:
            break
t2 = time.time()
print(f"The largest concatenated pandigital product is {num} which is a product of {base_num} and {tuple(range(1, n))}")
print(f"time taken: {t2 - t1: .2f} seconds")