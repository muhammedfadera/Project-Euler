"""
The cube 41063625 (which is 345³) can be permuted to produce two other cubes:
56623104 = 384³
66430125 = 405³
In total, there are three cubes that are permutations of one another's digits, and 
41063625 is the smallest such cube with exactly three cube permutations.

Find the smallest cube for which exactly five permutations of its digits are also perfect cubes.
"""
#%%
def digits(n):
    return tuple(sorted([d for d in str(n)]))

n = 1
n_permutations = 5
permutations_counter = {}
while True:
    n_cube = n**3
    digits_in_n_cube = digits(n_cube)
    try:
        permutations_counter[digits_in_n_cube][1] += 1
        permutations_counter[digits_in_n_cube][0].append(n_cube)
    except KeyError:
        permutations_counter[digits_in_n_cube] = [[n_cube], 1]
    if permutations_counter[digits_in_n_cube][1] == n_permutations:
       res = permutations_counter[digits_in_n_cube][0][0]
       print(f"The smallest number with {n_permutations} permutations which are cubes is {res}") 
       break
    n += 1