"""
The Champernowne's constant is an irrational number created by concatenating 
the positive integers:
    0.12345678910{1}112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.

if dn represents the nth digit of the fractional part, the the value of 
    d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000
"""
#%%
# def champernowne(n):
def number_n_digits(n_digits):
    start_n_digits = int(str(1)* (n_digits - 1 > 0) + 
                            '0'*((n_digits - 2)*(n_digits-2 > 0)) + '1')
    end_n_digits = int(str(1) + n_digits*'0')
    return n_digits * (end_n_digits - start_n_digits)
x = ''
N = [10**i for i in range(7)]
# n = N.pop(0)
res = 1
n_terms = 0
# for i in range(2, n):
# while True
ix = 0
# d = []
# X = []
cond = True
# while len(N) >= 1:
n_digits = 0
for n in N:
    while n_terms < n:
        ix += 1
        x += str(ix)
        n_terms += len(str(ix))
        # if n_terms >= n:
    idx = len(str(ix)) - (n_terms - n) - 1
    res *= int(str(ix)[idx])
    # d.append(str(ix))
    # while n_terms < n:
    #     n_digits += 1
    #     n_terms += number_n_digits(n_digits)
    # # n_digits_smaller = n_digits - 1
    # n_terms_smaller = n_terms - number_n_digits(n_digits) 
    # print(n_terms_smaller)
    # n_terms = n_terms_smaller
    # diff_to_smaller = n - n_terms_smaller
    # smallest_n_digit_num = int('0' + '9'*(n_digits-1)*(n_digits - 1 > 0))
                        
    # while n_terms_smaller < n:
    #     smallest_n_digit_num += 1
    #     # x += str(ix)
    #     n_terms_smaller += n_digits
    #     # if n_terms >= n:
    # # print(n_terms_smaller)
    # # print(smallest_n_digit_num)
    # # print(idx)
    # idx = n_digits - (n_terms_smaller-n) - 1
    # # idx = (n - n_terms_smaller)
    # d.append(str(smallest_n_digit_num)[idx])
    # res *= int(str(smallest_n_digit_num)[idx])
    # n_digits -= 1

print(res)
#%%
def d_n(n):
    """
    """
    if n <= 10:
        return int(str(n)[0])
    # n = n - 1 
    d = 0
    n_digits = 0
    while d < n:
        n_digits += 1
        d += number_n_digits(n_digits)
    # n_digits_smaller = n_digits - 1
    d_smaller = d - number_n_digits(n_digits) 
    diff_to_smaller = n - d_smaller
    # diff_to_larger = d - n
    # if diff_to_smaller < diff_to_larger: # closer to the begining of d_smaller digit numbers
    smallest_n_digit_num = int(str(1)* (n_digits - 1 > 0) + 
                        '0'*((n_digits - 1)*(n_digits-1 > 0))) - 1
    # n_digits_smaller = n_digits - 1
    # smallest_n_digit_num = int(str(1) + n_digits-1)*'0')
    n_times, remainder = divmod(diff_to_smaller, n_digits)
    number_closest_to_d_n = smallest_n_digit_num + n_times
    print(number_closest_to_d_n)
    print(n_times)
    print(remainder)
    if n_times == 0:
        return int(str(number_closest_to_d_n)[remainder])
    else:
        # return int(str(number_closest_to_d_n)[remainder])
        if remainder == 0:
            return int(str(number_closest_to_d_n)[-1])
        else:
            next_number = number_closest_to_d_n + 1
            return int(str(next_number)[remainder-1])
# d_n(15)
#%%
d_n(ix + 1) 
    # else:
# %%
x[ix]
