"""
Given an sorted array, delete the dupplicates. 

Input:
[2,2,2,4,7,8,13,13,13,19]

[2,4,7, ]

Return:
[2,4,7,8,13,19]

Design: 
Is the sorted array, this means that duplicates is continuous, due to this we know that duplicates will be continuous

def delete_dup(nums):
    empyt_slot = 1
    loop array (i) is should start at 1:
        if nums[i] != nums[empty_slot -1]:
            nums[empyt_slot] = nums[i]
            empyt_slot += 1
    
    return nums


"""
import unittest


def delete_dup(nums):
    empty_slot = 1
    for i in range(1, len(nums)):
        if nums[empty_slot - 1] != nums[i]:
            nums[empty_slot] = nums[i]
            empty_slot += 1

    return nums[:empty_slot]


class TestDelete_DupMethod(unittest.TestCase):
    def setUp(self):
        self.arr1 = [2,2,2,4,7,8,13,13,13,19]
    
    def test_arr1(self):
        self.assertEqual(delete_dup(self.arr1), [2,4,7,8,13,19])


if __name__ == "__main__":
    unittest.main()