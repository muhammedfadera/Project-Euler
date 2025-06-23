"""
It can be seen that the number 125874 and its double, 251748, contain exactly 
the same digits, but in a different order.

Find the smallest positive integer x such that 2x, 3x, 4x, 5x, and 6x contain the same digits.
"""
#%%
def same_digits(x, y):
    if len(x) == len(y):
        for i in range(len((x))):
            if x[i] not in y or y[i] not in x:
                return False
        return True
    else:
        return False
ix = 1
n_digits = 2
times = 6
break_cond = False
while True:
    # N = 6*ix
    # print(ix)
    # N = ix
    # print(f"Trying {n_digits} digit numbers")
    ix = int('1' + '0'*(n_digits - 1)) + 1
    while len(str(ix)) == len(str(6*ix)):
        n = times
        while same_digits(str(ix), str(n*ix)) and n >= 2:
            n -= 1
        if n == 1:
        # if same_digits(str(ix), str(n*ix)):
            print(f"The smallest number with the specified property is {ix}")
            break_cond = True 
            break
        ix += 1
    if break_cond:
        break
    # print(f"Exits {n_digits} digit numbers at {ix}")
    n_digits += 1
    

