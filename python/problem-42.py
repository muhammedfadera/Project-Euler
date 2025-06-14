"""
The n-th term of the sequence of triangle numbers is given by:

t_n = 1/2 * n * (n + 1)

So the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values, we form a word value. For example, the word value 
for SKY is:

19 + 11 + 25 = 55 = t_10

If the word value is a triangle number, then we shall call the word a triangle word.

Using 0042_words.txt, a 16K text file containing nearly two thousand common 
English words, how many are triangle words?
"""
#%%
# approach
# iterator through the entire file as a whole
# while computing the letter positions. Between
# a "," and another ",", check if the number you have is triangular
# for checking if the number is triangular, at any point during the 
# iteration you should should have list of triangular numbers which are
# at least bigger than the current value of a word

word_seperator = "\",\""
with open("0042_words.txt", "r") as f:
    words = f.readline()
    # remove the first and last commas
    words = words[1:-1].replace(word_seperator, ",")
#%%
from math import ceil
def is_triangle_number(x):
    sqrt_t_n = (1 + 8*x)**0.5
    if ceil(sqrt_t_n) - sqrt_t_n == 0:
        return True
    return False

#%%
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_values = {letter:LETTERS.index(letter)+1 for letter in LETTERS}

curr_triangle_number = 0
counter = 0
for letter in words:
    if letter == ",":
        if is_triangle_number(curr_triangle_number):
            counter += 1
        curr_triangle_number = 0
    else:
        curr_triangle_number += letter_values[letter]

print(f"The total number of triangle letters in the word list is {counter}")