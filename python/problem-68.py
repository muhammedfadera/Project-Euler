"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and 
each line adding to nine.

       (4)
         \
         (3)
        /   \
     (1) --- (2)---(6)
    /
  (5)

Working clockwise, and starting from the group of three with the numerically 
lowest external node (4,3,2 in this example), each solution can be described uniquely. 
For example, the above solution can be described by the set:
4,3,2; 6,2,1; 5,1,3

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. 
There are eight solutions in total.

Total	Solution Set
9	  4,2,3; 5,3,1; 6,1,2
9	  4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is:
432621513

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.

What is the maximum 16-digit string for a "magic" 5-gon ring?


# Approach:
- use 3 tensors/see Munkres
"""
#%%
from itertools import permutations

n_digits = 16
m = 10
n = 5
first_branch = []

for i in range(m-n+1, 0, -1):
  perms = permutations([x for x in range(m, 0, -1) if x != i], 2)
  for d1d2 in perms:
    first_branch.append([i] + list(d1d2))


counter = 1
branch = {1: first_branch}
print_cond = True
while counter < n:
  if counter == n-1:
    next_branch = []
    for d1d2 in branch[counter]:
      curr_list = [x for x in range(m, 0, -1) if x not in d1d2]
      for last_digit in curr_list:
        if last_digit > d1d2[0] and \
          sum(d1d2[-3:]) == (last_digit + d1d2[-1] + d1d2[1]):
          actual_branch = d1d2 + [last_digit, d1d2[-1], d1d2[1]]
          branch_sum = sum(d1d2[-3:])
          next_branch.append((actual_branch, branch_sum))
          num = "".join(str(x) for x in actual_branch)
          if print_cond and len(num) == n_digits:
            print(num)
            print_cond = False

    counter += 1
    branch[counter] = next_branch
  else:
    next_branch = []
    for d1d2 in branch[counter]:
      curr_list = [x for x in range(m, 0, -1) if x not in d1d2]
      possible_leaves = permutations(curr_list, 2)
      for d3d4 in possible_leaves:
        if d3d4[0] > d1d2[0] and \
          sum(d1d2[-3:]) == (sum(d3d4) + d1d2[-1]):
          next_branch.append(list(d1d2) + [d3d4[0], d1d2[-1], d3d4[1]])
    counter += 1
    branch[counter] = next_branch
# %%
branch[n]
# %%
