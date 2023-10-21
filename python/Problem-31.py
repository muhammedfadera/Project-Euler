# In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
#
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?

# currency denominations
# denominations = [25, 50, 10, 20, 50, 100, 200, 500, 1_000, 2_000]
denominations = [1, 2, 5, 10, 20, 50, 100, 200]
denominations.sort(reverse = True)

def n_ways(x, den = denominations, res_dict = {}, atom = 1):
    denominations = den[:]
    denominations = [atom*d for d in denominations]
    res = 0 # keep track of the sum
    while len(denominations) != 0:
        # take the current largest elements and remove it from the list of
        # denominations.
        k = denominations[0]
        denominations.remove(k)
        if k > x:
            continue
        # n here is the maximum number of ways one could denominations k
        n = x // k
        n += 1
        if x % k == 0:
            res += 1
            n -= 1
        for i in range(1, n):
            try:
                curr = res_dict['(' + str(n) + ',' +  str(k) + ',' + str(i) + ')']
                res += curr
            except KeyError:
                curr = n_ways(x - i*k, denominations)[0]
                res_dict['(' + str(n) + ',' + str(k) + ',' + str(i) + ')'] = curr
                res += curr
    return res, res_dict

n, res_dict = n_ways(1000)
# print(res_dict)
print(n)
# the solution above is correct
# now we need to actually print a list of all of the different combinations


