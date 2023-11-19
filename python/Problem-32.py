
'''
We shall say that an n-digit number is pandigital if it makes use of all the
 digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
 5 pandigital.The product 7254 is unusual, as the identity, 39 × 186 = 7254,
 containing multiplicand, multiplier, and product is 1 through 9 pandigital.

 Find the sum of all products whose multiplicand/multiplier/product identity
 can be written as a 1 through 9 pandigital.
 HINT: Some products can be obtained in more than
       one way so be sure to only include it once in your sum.

'''

#--------------------------- APPROACH -------------------------------------------#
# 1. We are seeking for three numbers X, Y and Z so that X times Y = Z. We first note this excludes
#    the possibility of the number of digits Z to be 1, 2 or 3 - e.g for Z to be 3 digit, both X
#    and Y must be 3 digit. However, the product of the two smallest 3 digit numbers is 100 * 100
#    which is not 3 digit number. 
# 2. The number of digits in Z is no more than 4 since (considering that there are only six digits
#    left for this possibility)
#   a. the product of 2 three digit number (at least those of interest to us) is at least a four
#      digit number (as above),
#   b. the product of 2 digit number and 4 digit number is at least 5 digits
# 3. Hence the only possibilities we have is Z4 = X2 times Y3 or Z4 = X1 times Y4 where the numbers 
#    after the letters signifies the number of digits. 
# 4. So the largest value of Z is 9999.
# 5. So a first step here would be to include all numbers starting from 9999 that
#   a. do not contain any 0,
#   b. do not repeat numbers from 1 to 9 two or more times.
#   c. is not prime.
#   as the set of all possible values of Z. 

#%%
def rep_digits(str_num):
      '''
      Returns true is str_num has digit that is repeated more than onces. It checks
      if the number of unique numbers is equal to the number of digits in the input
      '''
      unique_str = ''
      l = 0
      for i in str_num:
            if i not in unique_str:
                  unique_str += i
                  l += 1
      return len(str_num) != l

def intersest(x, y):
      '''
      returns false if there are digits in x that are in y or vice verse
      '''
      x = str(x)
      y = str(y)
      # picks x to be the one with more digits
      if len(y) > len(x):
            temp = x
            x = y
            y = temp
      for i in x:
            if i in y:
                  return True
      return False

def all_digits_1_to_9(x, y, z):
      '''
      checks if the combination of x, y and z contains all digits from 1 to 9 onces
      '''
      xyz = str(x) + str(y) + str(z)
      if len(xyz) != 9:
            return False
      for i in range(1, 10):
            if str(i) not in xyz:
                  return False
      return True

#%% ----------------------------- X -------------------------------------------
# X can only be a two or one digit number
# Two digits X must be paired with a three digit of Y
# and 1 digit X must be paired with 4 digit Y
MIN_X = 9
MAX_X = 99
TEST_X = 39

X2 = []

for num in range(MAX_X, MIN_X, -1):
      str_num = str(num)
      if num not in Z and ('0' in str_num or rep_digits(str_num)):
            next
      else:
            X2.append(int(str_num))
# one digit X to be paired with 4 digit Y
X1 = range(1, 10)


# print(f"The number of possibilities for X is no more than {len(X2) + len(X1)}")
# if TEST_X in X:
#       print(f"{TEST_X} is in X")

#%%
#----------------------------- Y ---------------------------------------#
# Y must be a three digit or four digits since the product of two two digit 
# number is atmost a 4 digit number and the product of a 1 digit number and 
# 4 digit number could be 4 digits

# 3 digit Ys to be paired with 2 digit X
MIN_Y = 99
MAX_Y = 999
TEST_Y = 186

Y3 = []

for num in range(MAX_Y, MIN_Y, -1):
      str_num = str(num)
      if ('0' in str_num or rep_digits(str_num)):
            next
      else:
            Y3.append(int(str_num))
# four digit Ys to be paired with 1 digit X
MIN_Y = 999
MAX_Y = 9999
# MAX_Y = MAX_Z

Y4 = []

for num in range(MAX_Y, MIN_Y, -1):
      str_num = str(num)
      if num not in Z and ('0' in str_num or rep_digits(str_num)):
            next
      else:
            Y4.append(int(str_num))



# print(f"The number of possibilities for Y is no more than {len(Y3) + len(Y4)}")
# if TEST_Y in Y:
#       print(f"{TEST_Y} is in Y")


#---------------- ANSWER ! -----------------------------
#%%
output = 0
count = 0
ans = {}
for x in X2:
      for y in Y3:
            if not intersest(x, y):
                  prod = x*y
                  cond1 = prod not in ans.keys()
                  cond2 = all_digits_1_to_9(x, y, prod)
                  if cond2 and cond1:
                        output += prod
                        count += 1
                        ans[prod] = [[x, y]]
                  if not cond1 and cond2:
                        ans[prod].append([x, y])
                  


for x in X1:
      for y in Y4:
            if not intersest(x, y):
                  prod = x*y
                  cond1 = prod not in ans.keys()
                  cond2 = all_digits_1_to_9(x, y, prod)
                  if cond2 and cond1:
                        output += prod
                        count += 1
                        ans[prod] = [[x, y]]
                  if not cond1 and cond2:
                        ans[prod].append([x, y])

print(f"The sum of all pandigital products is {output}")
# %%
