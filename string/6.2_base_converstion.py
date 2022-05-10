"""
You are given a string (str ) that is an integer with its base (b1), and another base (b2).
Convert it to b2, 10 = A, 11 = B... vice versa.

Clarify:
2 <= b1
16 >= b2

An integer = 190, b = 10, is 1*10**2 + 9*10**1 + 0*10*0 = 190
An integer = 183, b = 9, is 1*9**2 + 8*9**1 + 3*9**0 = 156

Design:
The solutions is I can take the string which is b1 and convert is to base-10 then convert back to b2
"""
import functools
import string


def convert_base(num_as_str, b1, b2):
    def contruct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                contruct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_str[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_str[is_negative:], 0
    )

    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           contruct_from_base(num_as_int, b2))
