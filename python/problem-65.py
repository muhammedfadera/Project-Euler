"""
The square root of 2 can be written as an infinite continued fraction.

  √2 = 1 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / (2 + ...))))

The infinite continued fraction can be written as:

  √2 = [1; (2)]
Here, (2) indicates that 2 repeats ad infinitum.
In a similar way, √23 = [4; (1, 3, 1, 8)].

It turns out that the sequence of partial values of continued fractions for square 
roots provides the best rational approximations.
Let us consider the convergents for √2:

  1 + 1/2 = 3/2
  1 + 1/(2 + 1/2) = 7/5
  1 + 1/(2 + 1/(2 + 1/2)) = 17/12
  1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29

Hence the sequence of the first ten convergents for √2 is:

  1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant:

  e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...]

The first ten terms in the sequence of convergents for e are:

  2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is:

  1 + 4 + 5 + 7 = 17

Question:
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

"""
#%%
from math import ceil
def e_n_term(n):
    if n <= 2:
        return n
    else:
        n_minus_2_divides_3 = (n-2)%3 != 0
        y = 2/3*n + 2/3
        return n_minus_2_divides_3 + ceil(y)*(1-n_minus_2_divides_3)

def n_convergent(n):
    n -= 1
    if n == 0:
        return (2, 1)
    a_n = e_n_term(n)
    # print(a_n)
    a, b = 1, a_n # a/b
    # print(a, b)
    for i in range(n-1, 0, -1):
        a, b = b, b*e_n_term(i) + a
    return (2*b + a, b)
    # return (a, b)

N = 100
a, b = n_convergent(N)

res = sum(int(d) for d in str(a))
print(f"The sum of the digits in the numerator of the {N}th convergent is {res}")

# %%
