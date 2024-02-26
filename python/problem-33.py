import time
t0 = time.time()
'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
correct, is obtained by cancelling the 9s.

We shall consider fractions like 30/50, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.



Approach
1. We are seeking for a quadruplet X, Y and x, y such that 

X/Y = x/y => Xy = xY 
where the
a. the number of digits in both X and Y is 2.
b. X < Y
c. The trailing digits of both X and Y cannot be 0. Since we are dealing with 
only two digit numbers, this excludes multiples of 10. 
d. Furthermore, since X goes into Y, both X and Y cannot be prime. 

'''


# see ipad Project-Euler for notes

# sets of all possible values of X and Y are 2 digit numbers
#%%
import time
t0 = time.time()
two_three_digit_primes = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                          53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def gcd(a, b):
    '''
    finds the greatest common divisor of two numbers
    '''
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


n_digits = 2 # only two digit numbers

y_prod = 1
x_prod = 1

min_X_Y = 10 
max_X_Y = 100
all_possible_X_Y = [i for i in range(min_X_Y, max_X_Y) if i % 10 != 0]
n = len(all_possible_X_Y)
res = {} # dictionary with key X and values (Y, x, y)

for j in range(n):
    for k in range(j+1, n):
        X = all_possible_X_Y[j]
        Y = all_possible_X_Y[k]
        # the denominator cannot prime or multiple of 10 and must not be prime
        # and the cannot both be in the same 10
        if not (Y in two_three_digit_primes or gcd(X, Y) == 1):
            X_ = str(X)
            Y_ = str(Y)
            for ix in range(n_digits):
                for iy in range(n_digits):
                    if X_[ix] == Y_[iy]:
                        # index of the other digit
                        ix1 = 0 if ix == 1 else 1 
                        iy1 = 0 if iy == 1 else 1
                        # the other digits
                        x_ = int(X_[ix1])
                        y_ = int(Y_[iy1])
                        if X*y_ == Y*x_:
                            if X not in res.keys():
                                res[X] = [(Y, x_, y_)]
                            else:
                                res[X].append((Y, x_, y_))
                            print(X, Y)
                            x_prod *= x_
                            y_prod *= y_

# print(res)
print(f"The final answer is {y_prod/gcd(y_prod, x_prod)}")
print(f"finished in {time.time() - t0:.3g} seconds")
# %%
