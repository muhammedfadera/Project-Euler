# The number 3797 has an interesting property. 
# Being prime itself, it is possible to continuously 
# remove digits from left to right, and remain prime at each stage: 
# 3797, 797, 97 and and 7. Similarly we can work from right to left: 
# 3797, 379, 37, and 3
# Find the sum of the only eleven primes that are both 
# truncatable from left to right and right to left.
# NOTE: 2, 3, 5 and 7 are not considered to be truncatable primes
#%%
from math import ceil, sqrt
NUM_TRUNCATABLE_PRIMES = 11

def div_2(x):
    return x[-1] in ['0', '2', '4', '6', '8']

def div_3(x):
    sum_digits = x
    sum_digits = str(sum(int(digit) for digit in sum_digits))
    while len(sum_digits) > 1:
        sum_digits = str(sum(int(digit) for digit in sum_digits))
    return sum_digits in ['0', '3', '6', '9']
def div_5(x):
    return x[-1] in ['0', '5']


def isPrime(x):
   if x in [2, 3, 5, 7]:
       return True
   str_x = str(x)
   if (x <= 1) or div_2(str_x) or div_3(str_x) or div_5(str_x) or (x % 7 == 0):
      return False
   min_prime = 11
#    if len(prime_list) > 0:
#        min_prime = prime_list[-1]
   for div in range(min_prime, ceil(sqrt(x))+1):
      if x % div == 0:
         return False
   return True

def cycle_one_digit_primes(x):
    if x <= '1':
        return '2'
    elif x <= '2':
        return '3'
    elif x <= '4':
        return '5'
    elif x <= '6':
        return '7'
    else:
        return x

def possible_next_truncatable_prime_number(x):
    x0 = x[0]
    if x0 in ['1', '4', '6']:
        x = cycle_one_digit_primes(x0) + '0'*(len(x)-1)
    if x0 in ['8', '9']:
        x = str(int(x0) + 1) + '0'*(len(x) - 1)

    # first find the next number whose last digit is 
    # 3, 5, 7
    last_digit = int(x[-1])
    if 7 <= last_digit <= 9: # moving on to the next number
        # 10 - last_digits takes us to the next next multiple of 10
        # and 3 just moves it to the next possible truncatable prime
        x = str(int(x) + 10 - last_digit + 3)
    else:
        x = x[:-1] + cycle_one_digit_primes(str(last_digit))
    # refine the next number 
    last_digit = x[-1]
    while last_digit in ['0', '1', '2', '4', '5', '6', '8', '9']:
        if last_digit in ['0', '1', '2', '4', '5', '6']:
            x = x[:-1] + cycle_one_digit_primes(last_digit)
        elif last_digit in ['7', '8', '9']:
            x = str(int(x) + 10 - int(last_digit) + 3)
            last_digit = x[-1]
            x = x[:-1] + cycle_one_digit_primes(last_digit)
        last_digit = x[-1]
    return x


#%%
import time
t = time.time()
count = 0
str_NUM = '11'
result = 0
prime_list = set()
truncatable_prime_list = set()
# non_truncatable_prime_list = set()
no_of_checks = 1
while count < NUM_TRUNCATABLE_PRIMES:
    # if str_NUM[0] in not_first_and_last_digits and \
    #     str_NUM[-1] in not_first_and_last_digits:
    #     NUM += 1
    #     continue
    str_NUM = possible_next_truncatable_prime_number(str_NUM)
    remaining_digits = str_NUM[1:]
    if '5' in remaining_digits or '0' in remaining_digits or \
        ('2' in remaining_digits) or ('4' in remaining_digits) or \
        ('6' in remaining_digits) or ('8' in remaining_digits):
        continue
    # sum_digits = sum(int(digit) for digit in str_NUM)
    # if sum_digits % 3 == 0:
    if div_3(str_NUM):
        continue

    NUM = int(str_NUM)
    if NUM in truncatable_prime_list:
        result += NUM
        count += 1
        prime_list.add(NUM)
        print(f"{count} truncable primes found")
        continue
    if '4' in str_NUM or '6' in str_NUM or \
        '8' in str_NUM or '0' in str_NUM:
        # non_truncatable_prime_list.add(NUM)
        continue
    # print(f'checking the number {str_NUM}')
    no_of_checks += 1

    prime_cond = NUM in prime_list
    if not prime_cond:
        prime_cond = isPrime(NUM)
        if prime_cond:
            prime_list.add(NUM)
        else:
            # if it is not prime, go to the next iteration
            continue

    left_digit_removed = str_NUM[1:]
    right_digit_removed = str_NUM[:-1]

    # check if left truncation is prime
    left_cond = True
    while left_cond and len(left_digit_removed) >= 1:
        if left_digit_removed[0] == '0':
            left_digit_removed = left_digit_removed[1:]
            continue
        int_left_digit_removed = int(left_digit_removed)
        if int_left_digit_removed in truncatable_prime_list:
            left_cond = True
            break
        if '2' in left_digit_removed or '4' in left_digit_removed or \
            '6' in left_digit_removed or '8' in left_digit_removed or \
            '0' in left_digit_removed:
            left_cond = False
            break
        left_cond = int_left_digit_removed in prime_list
        if not left_cond:
            left_cond = isPrime(int_left_digit_removed)
            if left_cond:
                prime_list.add(int_left_digit_removed)
        left_digit_removed = left_digit_removed[1:]

    # check if right truncation is prime
    right_cond = True 
    while (left_cond and right_cond) and len(right_digit_removed) >= 1:
        int_right_digit_removed = int(right_digit_removed)
        if int_right_digit_removed in truncatable_prime_list:
            right_cond = True
            break
        right_cond = int_right_digit_removed in prime_list
        if not right_cond:
            right_cond = isPrime(int_right_digit_removed)
            if right_cond:
                prime_list.add(int_right_digit_removed)
        right_digit_removed = right_digit_removed[:-1]
    
    # combine both conditions
    truncatable_prime_cond = right_cond and left_cond
    if truncatable_prime_cond:
        result += NUM
        count += 1
        truncatable_prime_list.add(NUM)
        print(f"{count} truncable primes found")

print(f"number of checks {no_of_checks}")
print(f"The sum of all truncatble primes is {result}")
print(f"time taken {time.time() - t} seconds")
# %%
