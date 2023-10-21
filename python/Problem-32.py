
'''
We shall say that an n-digit number is pandigital if it makes use of all the
 digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
 5 pandigital.The product 7254 is unusual, as the identity, 39 × 186 = 7254,
 containing multiplicand, multiplier, and product is 1 through 9 pandigital.

 Find the sum of all products whose multiplicand/multiplier/product identity
 can be written as a 1 through 9 pandigital.
 HINT: Some products can be obtained in more than
       one way so be sure to only include it once in your sum.

 Apporach:
 1. Reduce the number of possibilities by grouping together compatible numbers
     Two numbers are compatible if their product
     - does not contain any of the digits contained in the previous
 2. List the possibilities for the last digit and then reduce the number of the
 second and the third and so on given the previous digits.
'''

#%%
import numpy as np
N_DIGITS = 0 # keeps track of the number of digits used sofar
multiplicand_digits_tracker = dict() # a key-value pair of the place value and the digit in the multiplicand
results_digits_tracker = dict() # ... in the product
x = np.arange(1, 10) # numbers from 1 to 9
# pairwise produce of no. from 1 to 9
multiplication_table = np.outer(x, x)
# print(multiplication_table)

def multiply(a, b):
    '''
    return the product of a and b
    '''
    return multiplication_table[a-1, b-1]

def nums_from_keys(x):
    '''
    return the number a, b from a dictionary key whose value is
    a*b
    '''
    res = x.split(x)
    a, b = res[0], res[1]
    return a, b
def n_digit(x, n):
    '''
    returns the n^th digit starting from the unit as the
    zeroth digit
    '''
    return int(str(x)[-1*(n + 1)])
def addition_table(x, y, repetitions = False):
    res = dict()
    for k1, i in x.items():
        for k2, j in y.items():
            res_keys = res.keys()
            cond1 = k1 + '+' + k2 not in res_keys
            if cond1:
                if not repetitions and (i == j):
                    next
                else:
                    res[k1 + '+' + k2] = i + j
    return res
# x = {str(i):i for i in range(1, 10)}
# print(addition_table(x, x))
# print(addition_table(range(10), range(10)))
# print(n_digit(40, 1))
# the maximum number of elements in the multiplication table
N = 9*9
# compatible = [None]*N
# mt for multiplication table
reduced_table = dict()
compatible = dict()
carrys = dict()
compt_digit = 1
carry_digit = 1
for i in range(1, 10):
    for j in range(i+1, 10):
        p = multiply(i, j)
        reduced_table[str(i) + ',' + str(j)] = p
        last_digit = p % 10
        if i != last_digit and j != last_digit and \
                last_digit != 0:
            # here we are only storing the indices
            # to find the product we just use multiply
            # compatible[ix] = [[i], [j]]
            curr_key = str(i) + '*' + str(j)
            compatible[curr_key] = last_digit
            # curr_carry_key = str(carry_digit) + '-c-' + curr_key
            remaining_digits = str(p - last_digit)[:-1]
            if len(remaining_digits) != 0 and int(remaining_digits) != 0:
                carrys[curr_key] = int(remaining_digits)
# count the first digit of the first and the first digit of the second
# and the first digit of the results
N_DIGITS += 3 #

result_last_digits = set(compatible.values())
possible_last_digits = list()
for k in compatible.keys():
    possible_last_digits.extend(k.split('*'))
possible_last_digits = [*set(possible_last_digits), ]
# update possible last digits in the multiplicand and the product
multiplicand_digits_tracker[1] = possible_last_digits
results_digits_tracker[1] = results_digits_tracker
# print(possible_last_digits)
# ------------ SECOND DIGITS ---------------------- #
second_digits = []
excluded = []
for k, d in compatible.items():
    pair = k.split('*')
    a, b = int(pair[0]), int(pair[1])
    x = multiplication_table[a-1, :]
    y = multiplication_table[b-1, :]
    x[[a-1, b-1]] = 0
    y[[a-1,b-1]] = 0
    x_ = {str(a) + '*' + str(i+1):x[i] for i in range(9) if x[i] != 0}
    y_ = {str(b) + '*' + str(i+1):y[i] for i in range(9) if y[i] != 0}
    try:
        k = str(a) + '*' + str(b)
        c = carrys[k]
        k_ = addition_table(x_, {str(c):c})
        v_ = addition_table(y_, {str(c):c})
    except KeyError:
        k_ = x_
        v_ = y_
    # this ensures that the location of a or b is excluded
    curr_add_table = {k:v for k, v in addition_table(k_, y_).items() \
                      if str(v)[-1] not in ['0'] + possible_last_digits}
    curr_add_table.update(
        {k:v for k, v in addition_table(x_, v_).items() \
         if str(v)[-1] not in ['0'] + possible_last_digits}
    )
    break
    curr_digit = [*set([u%10 for u in curr_add_table.values()]),]
    if len(curr_digit) == 0:
        excluded += [k]
    elif not set(curr_digit) <= set(second_digits):
        second_digits += curr_digit

for k in excluded:
    compatible.pop(k)

# print(second_digits)
print(compatible)

# %%
