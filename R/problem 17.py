# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:27:54 2017

@author: Fadera
"""

#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
#3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were
#written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
#23 letters and 115 (one hundred and fifteen)
#contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import inflect as m
def sum_of_words(fr, to, by=1):
    z = m.engine()
    d = []
    i = fr
    while i <= to:
        d.append(z.number_to_words(i))
        i+=by
    s = 0
    for j in d:
        for i in str(j):
           if not (i == " " or i == "-"):
               s+=1
    return(s)
    


