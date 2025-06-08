# The number 3797 has an interesting property. 
# Being prime itself, it is possible to continuously 
# remove digits from left to right, and remain prime at each stage: 
# 3797, 797, 97 and and 7. Similarly we can work from right to left: 
# 3797, 379, 37, and 3
# Find the sum of the only eleven primes that are both 
# truncatable from left to right and right to left.
# NOTE: 2, 3, 5 and 7 are not considered to be truncatable primes
#%%
# digits = {
    # 'first': [2, 3, 5, 7],
first = ['2', '3', '5', '7']
# 'rest': [3, 7, 9], 
rest =  ['3', '7', '9'] 
# }
    # 3: [3, 7, 9]
# we can traverse this list starting from left to right 
# and check if its prime while counting the nunber of primes
# we have encountered and stop once we reach 11

# QUESTION
# Can we reduce the number of checks
# for example we know 3 cannot a number which is a multiple of 3
# }
#%%
from math import ceil, sqrt
NUM_TRUNCATABLE_PRIMES = 11

def isPrime(x):
   if x in [2, 3, 5, 7]:
       return True
   if (x <= 1) or (x % 2 == 0) or \
      (x %3 == 0) or (x % 5 == 0) or (x % 7 == 0):
      return False
#    for div in prime_list:
#       if x % div == 0:
#          return False
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

def next_truncatable_number(x):
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
        # x = next_truncatable_number(x) 
    return x


#%%
count = 0
str_NUM = '11'
result = 0
prime_list = set()
truncatable_prime_list = set()
no_of_checks = 1
while count < NUM_TRUNCATABLE_PRIMES:
    # if str_NUM[0] in not_first_and_last_digits and \
    #     str_NUM[-1] in not_first_and_last_digits:
    #     NUM += 1
    #     continue
    str_NUM = next_truncatable_number(str_NUM)
    print(f'checking the number {str_NUM}')
    NUM = int(str_NUM)
    no_of_checks += 1
    if NUM in truncatable_prime_list:
        result += NUM
        count += 1
        prime_list.add(NUM)
        print(f"{count} truncable primes found")
        continue
    
    prime_cond = NUM in prime_list
    if not prime_cond:
        # prime_cond = isPrime(NUM, prime_list=list(prime_list))
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
        # print(len(left_digit_removed))
        if left_digit_removed[0] == '0':
            left_digit_removed = left_digit_removed[1:]
            continue
        int_left_digit_removed = int(left_digit_removed)
        if int_left_digit_removed in truncatable_prime_list:
            left_cond = True
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
    # if isTruncatablePrime(str_NUM, 'left') and isTruncatablePrime(str_NUM, 'right'):
    if truncatable_prime_cond:
        result += NUM
        count += 1
        truncatable_prime_list.add(NUM)
        print(f"{count} truncable primes found")

print(f"number of checks {no_of_checks}")
print(f"The sum of all truncatble primes is {result}")
# %%
