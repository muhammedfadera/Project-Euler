"""
Maximum Path Sum in a Triangle

By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23:

      3
    7   4
   2  4  6
 8  5  9  3

That is, the path 3 → 7 → 4 → 9 gives the sum:
3 + 7 + 4 + 9 = 23

Problem:
Find the maximum total from top to bottom in the file triangle.txt, a 15KB text 
file containing a triangle with 100 rows.

NOTE:
This is a more difficult version of Problem 18.
It is not possible to try every route to solve this problem, as there are 2^99 possible paths.
Even if you could check one trillion (10^12) routes per second, it would take over 
twenty billion years to evaluate all of them. There is, however, an efficient algorithm to solve it.
"""
#%%

with open("0067_triangle.txt", "r") as f:
    x = f.read().split("\n")

y = []
for n in x:
	try:
		y.append([int(i) for i in n.split(" ")])
	except ValueError:
            print(n)
def replace_upper_triangle(x, y):
    """
	given two lists x and y with len(y) = len(x) + 1, 
    replace each element of x with the maximal triangle sum. 
    e.g 
    x =   [66, 63, 04, 68]
	y = [04, 62, 98, 27, 23]
	returns [66 + 62, 63 + 98, 04 + 98, 68 + 27]
    """
    output = x.copy()
    for i in range(len(x)):
        output[i] = x[i] + max(y[i], y[i+1])
    return output

curr_largest_from_the_bottom = y[-1]

for ix in range(len(y)-2, -1, -1):
	curr_largest_from_the_bottom = replace_upper_triangle(
		y[ix], curr_largest_from_the_bottom)
res = max(curr_largest_from_the_bottom)

print(f"The maximum total from top to bottom in the file triangle.txt is {res}")
# %%
