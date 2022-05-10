"""
In a spreadsheet A = 1, AA = 27, ZZ = 702

Design a fucntion that return the interger id for when given a string 

You can treat this as the string to int converter problem. A is 1, and Z = 26
"""
import functools


def convert(str):
    return functools.reduce(
        lambda result, c: result*26 + ord(c) - ord('A') + 1,
        str, 0)


