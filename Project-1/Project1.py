#Project1 Danielle Neal
#My Attempt at Free Project 7-1 from the Textbook

#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

#%%
from random import choice

subjects = ['DOG', 'CAT', 'ME', 'YOU', 'US', 'PEAR',
            'ARM', 'LEG', 'SCHOOL', 'HOUSE', 'BROTHER', 'APPLE', 'WEEK',
            'STORE', 'TOWN', 'COWORKER']
predicates = ['BEST', 'QUIET', 'TALL', 'SHORT', 'HIGH', 'LOW',
              'LOUD', 'YOUNG', 'MAD', 'JOYOUS', 'MOURNFUL', 'HEAVY', 'EXPENSIVE',
              'BIG', 'GOOGLE', 'ANTIQUE']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' MEANWHILE ', ' SINCE ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A APPLE':
        text = 'AN APPLE'
    if text == 'A ARM':
        text == 'AN ARM'
    if text == 'A US':
        text == 'AN US'
    return text + ' IS '



print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')
