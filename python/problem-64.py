"""
All square roots are periodic when written as continued fractions and can be written 
in the form:

  √N = a₀ + 1 / (a₁ + 1 / (a₂ + 1 / (a₃ + ...)))

For example, let us consider √23:

  √23 = 4 + √23 − 4 = 4 + 1 / (1 / (√23 − 4)) = 4 + 1 / (1 + (√23 − 3)/7)

If we continue, we would get the following expansion:

  √23 = 4 + 1 / (1 + 1 / (3 + 1 / (1 + 1 / (8 + ...))))

The process can be summarised as follows:

  a₀ = 4, 1 / (√23 − 4) = (√23 + 4)/7 = 1 + (√23 − 3)/7
  a₁ = 1, 7 / (√23 − 3) = 7(√23 + 3)/14 = 3 + (√23 − 3)/2
  a₂ = 3, 2 / (√23 − 3) = 2(√23 + 3)/14 = 1 + (√23 − 4)/7
  a₃ = 1, 7 / (√23 − 4) = 7(√23 + 4)/7 = 8 + √23 − 4
  a₄ = 8, 1 / (√23 − 4) = (√23 + 4)/7 = 1 + (√23 − 3)/7
  a₅ = 1, 7 / (√23 − 3) = 7(√23 + 3)/14 = 3 + (√23 − 3)/2
  a₆ = 3, 2 / (√23 − 3) = 2(√23 + 3)/14 = 1 + (√23 − 4)/7
  a₇ = 1, 7 / (√23 − 4) = 7(√23 + 4)/7 = 8 + √23 − 4

It can be seen that the sequence is repeating. For conciseness, we use the notation:

  √23 = [4; (1, 3, 1, 8)]

to indicate that the block (1, 3, 1, 8) repeats indefinitely.

The first ten continued fraction representations of irrational square roots are:

  √2 = [1; (2)]    period = 1
  √3 = [1; (1, 2)]  period = 2
  √5 = [2; (4)]    period = 1
  √6 = [2; (2, 4)]  period = 2
  √7 = [2; (1, 1, 1, 4)] period = 4
  √8 = [2; (1, 4)]  period = 2
  √10 = [3; (6)]    period = 1
  √11 = [3; (3, 6)]  period = 2
  √12 = [3; (2, 6)]  period = 2
  √13 = [3; (1, 1, 1, 1, 6)] period = 5

Exactly four continued fractions, for N ≤ 13, have an odd period.

Question:
How many continued fractions for N ≤ 10,000 have an odd period?
"""
#%%
from utilities import is_int


N = 1_000         
res = 0
for n in range(1, N+1):
   a_0 = n**0.5
   if is_int(a_0):
        continue
   a_0 = int(a_0)
   radical = (1, -a_0)
   ix = 0
   periods = []
   while radical not in periods: 
        periods.append(radical)
        b = radical[1]
        y = radical[0]
        denominator = (n - b**2)/y
        numerator = n**0.5 - b
        a_n = int(numerator/denominator)
        radical = (denominator, -b - a_n*denominator)
        ix += 1
   res += ix % 2


print(f"The number of odd periods less than {N} is {res}")
#%% 
def sqrt_continued_fraction(n):
   a_0 = n**0.5
   if is_int(a_0):
        return [a_0, []] 
   a_0 = int(a_0)
   # radical = (y, b) = y/(sqrt(n) + b)
   radical = (1, -a_0)
   output = [a_0, []]
   periods = []
   while radical not in periods:
        periods.append(radical)
        b = radical[1]
        y = radical[0]
		# base on observations, 
		# it turns out y always divides n - b**2
        denominator = (n - b**2)/y 
        numerator = n**0.5 - b
        a_n = int(numerator/denominator)
        radical = (denominator, -b - a_n*denominator)
        output[1].append(a_n)
        # ix += 1
   return output
output = sqrt_continued_fraction(13)

# %%
