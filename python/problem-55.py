"""
If we take 47, reverse and add: 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example:

349 + 943 = 1292
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, 
never produce a palindrome. A number that never forms a palindrome through the 
reverse and add process is called a Lychrel number.

Due to the theoretical nature of these numbers, and for the purpose of this 
problem, we shall assume that a number is Lychrel until proven otherwise.

In addition, you are given that for every number below ten-thousand, it will either:
(i) become a palindrome in less than fifty iterations, or
(ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.

In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
4668731596684224866951378664 (53 iterations, 28 digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

Question:
How many Lychrel numbers are there below ten-thousand?
"""
#%%
from utilities import is_palindromic

N = 10_000
max_lychrel = N - 1
Lychrel_track = set()
not_Lychrel_track = set()
Lychrel_counter = max_lychrel
sequence_tracker = dict()

while max_lychrel > 0:
    iterations = 0
    x = max_lychrel
    sequence = [x]
    while iterations <= 50:
        x = int(int(str(x)) + int(str(x)[::-1]))
        sequence.append(x)
        iterations += 1
        if x in Lychrel_track or is_palindromic(x):
            Lychrel_counter -= 1
            # Lychrel_track.add(x)
            Lychrel_track.add(max_lychrel)
            break
        elif x in not_Lychrel_track:
            not_Lychrel_track.add(max_lychrel)
            break
    sequence_tracker[max_lychrel] = sequence
    if iterations > 50:
        not_Lychrel_track.add(max_lychrel)
    max_lychrel -= 1

print(f"The number of Lychrel numbers less than or equal {N} is {Lychrel_counter}")







