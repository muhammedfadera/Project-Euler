"""
It is possible to show that the square root of 2 can be expressed as an infinite continued fraction.

√2 = 1 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are:
99/70, 239/169, and 577/408.

But the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

Question:
In the first one thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""
#%%

def continued_fraction(n):
    a, b = 1, 2
    k = 1
    while k <= n:
        a = 2*b + a
        temp = b
        b = a
        a = temp
        k += 1
    return (b - a, a)

expansions = 8
n_expansions = 1000
numerator_larger_than_denominator = 0
while expansions <= n_expansions:
    a, b = continued_fraction(expansions)
    if len(str(a)) > len(str(b)):
        numerator_larger_than_denominator += 1
    expansions += 1
