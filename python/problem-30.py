# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#     1634 = 1^4 + 6^4 + 3^4 + 4^4
#     8208 = 8^4 + 2^4 + 0^4 + 8^4
#     9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


# Idea: find the largest n for which no number of that number of digits
# can be equal to the sum of the digits.
# use brute force from here but first sum the fifth power of the numbers taking
# 2, 3, 4, ..., n at a time. Check if the numbers involved all appear in the result.
# if so this number can be written as sum of the 5th power of its digit

p = range(10)
g = [(str(i), i**5) for i in p]

def InStringRemove(digits, fifth_sum):
    '''
    checks if characters in chars are in string and remove the first
    instance of its appearance.
    Otherwise it just return the string unaltered
    '''
    fifth_sum = str(fifth_sum)
    l = len(fifth_sum)
    for char in digits:
        fifth_sum = fifth_sum.replace(str(char), '', 1)
        if l == len(fifth_sum):
            return False
        l = len(fifth_sum)
    if fifth_sum == '':
        return True

def ConcatDigits(num1, num2):
    '''
    takes a pair num1 and num2 and merge the digits and also sum their fifth
    powers
    '''
    two_digits = []
    for i in range(len(num1)):
        for k in range(i, len(num2)):
            k1, v1 = num1[i]
            k2, v2 = num2[k]
            two_digits.append((k1 + k2, v1 + v2))
    return two_digits

two_digits = ConcatDigits(g, g); two_digits
three_digits = ConcatDigits(g, two_digits)
four_digits = ConcatDigits(g, three_digits)
five_digits = ConcatDigits(g, four_digits)
six_digits = ConcatDigits(g, five_digits)
# seven_digits = ConcatDigits(g, six_digits)
# seven_digits = ConcatDigits(g, six_digits)
all_nums = two_digits + three_digits + four_digits + \
    five_digits + six_digits

res = []
for num in all_nums:
    if num[1] not in res and InStringRemove(num[0], num[1]):
        res.append(num[1])

print('The sum of all numbers expressible as the sum' + \
    f'of the fifth power of its digits is {sum(res)}')
res
