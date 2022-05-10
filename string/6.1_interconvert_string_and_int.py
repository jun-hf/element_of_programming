"""
Given a string that represents an interger, convert it to int type, vice versa.

Assumptions:
Not a float
Can be negative or positive

234 to '234'
Design:
- int to string

def int_to_str():
    handdle negative sign
    by putting a bool for negative sign
        then make the int to positive so that i dont have to worry about is when converting my iont
    
    s= [] # we want convert our each int to str then append to this list

    # method to convert each int example: 478
    # we need to split each int by modulos your int, 478 % 10, you will get 8, convert your 8 and append to s,
    # then you need to divide your int to 47, then continue the previous process
    while loop:
        above method
    
    handle your negative

    return string by joining the elements in s

def str_to_int():
    the inituition:
        315, you have a sum = 0, iterate over the string from the front,
        first: 0(sum) + 3 = 3
        second: (3) * 10 + 1 = 31
        third: 31 * 10 + 5 = 315
"""
import unittest
import functools
import string


def int_to_str(num):
    is_negative = False

    if num < 0:
        num, is_negative = -num, True

    s = []
    while True:
        s.append(chr(48 + num % 10))
        num //= 10

        if num == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


def str_to_int(str):
    return (-1 if str[0] == "-" else 1) * functools.reduce(
        lambda sum, c: sum * 10 +
        string.digits.index(c), str[str[0] in '-+':], 0
    )


class TestInt_to_StrMethod(unittest.TestCase):
    def setUp(self):
        self.int1 = 909
        self.int2 = -982

    def test_int(self):
        self.assertEqual(int_to_str(self.int1), '909')
        self.assertEqual(int_to_str(self.int2), '-982')


if __name__ == '__main__':
    unittest.main()
