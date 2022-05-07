"""

Given an array (unsorted) return a new array with the relation A[0] < A[1] > A[2] < A[3] > A[4]

You just need to loop (i) throught the array, when (i) is even then you need to swap your array in this A[i] < A[i + 1], 
when (i) is odd, then A[i] > A[i+1]

Design:

def alteration(A):
    for loop (i):
        A[i:i+2] = sorted(A[i:i+2], reverse = bool(i%2))
"""
import unittest


def alternation(nums):
    for i in range(len(nums)):
        nums[i: i+2] = sorted(nums[i:i+2], reverse=bool(i % 2))
    return nums


class TestAlternationMethod(unittest.TestCase):
    def setUp(self) -> None:
        self.arr1 = [2, 7, 3, 1, 6, 0, 1]

    def test_arr1(self):
        self.assertEqual(alternation(self.arr1), [2, 7, 1, 6, 0, 3, 1], "Function works")


if __name__ == "__main__":
    unittest.main()
