"""
Given an string that represent a roman numeral. Convert it to integer.

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

The numeral needs to be bigger char to smaller 'VI', 'IXC' is invalid and you need to take the diffrences of the pair
"""

import functools

def roman_converter(str):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}

    return functools.reduce(
        lambda value, i: value + (-T[str[i]] if T[str[i]] < T[str[i+1]] else T[str[i]]),
        reversed(range(len(str) -1 )), T[str[-1]]
        )