"""
If p is the perimeter of a right angle triangle with integral length sides, a, b, c, 
there are exactly three solutions for p = 120. (20,48,52), (24,45,51), (30,40,50). 
For which value of p <= 1000, is the number of solutions maximised?


solution approach:
    https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Generating_all_Pythagorean_triples_using_a_predetermined_positive_integer
"""
#%%
# at least on of the numbers should be even
from math import ceil
perimeter_limit = 1000
min_known = 120
min_triple_known = 20
solution_dict = dict()
for x in range(min_triple_known, perimeter_limit, 2):
    for div in range(1, x):
        x_sqr = x**2
        if x_sqr % div == 0:
            y = x_sqr/(2*div) - div/2
            if ceil(y) != y:
                    continue
            z = x_sqr/(2*div) + div/2
            if ceil(z) != z:
                    continue
            # remove triples which are not integers 
            perimeter = x + y + z
            if min_known <= perimeter <= perimeter_limit:
                try:
                    solution_dict[perimeter].add((x, y, z))
                except KeyError:
                    solution_dict[perimeter] = set((x, y, z))
#%%
res = min_known
res_length = len(solution_dict[res])
#%%
for (k, v) in solution_dict.items():
     if len(v) > res_length:
          res = k
          res_length = len(v)

print(f"The solution is {res}")
# %%
