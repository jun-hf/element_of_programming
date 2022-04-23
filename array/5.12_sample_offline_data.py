"""
Given an array with distinct elements and a size,
return a subset of the given size of the array. 

All subsets should be equally likely. 
Return the result in input array itself.

Given:
1 array (nums) - all elements is distinct, and is number
1 number (size) 

Result:
You want to return a subset of the array (numns) of size k, this subset need to be equally probability for every subset of size k
and you want to return the array nums, just that the nums[0:k] is the subset you are returning
Design:
[3, 1, 5, 9]

I can just have a for loop i, that iterate until k:
    generate a random number from i to len(nums), which this random number will be your random index
    then you swap it with index i


Math induction can prove that this method is equally likely for k size subset for array A = by proving that is equally likely for k-1 size of subset.
"""
import random


def generate_subset_size_k(k, nums):
    for i in range(k):
        random_index = random.randint(i, len(nums) - 1)
        nums[i], nums[random_index] = nums[random_index], nums[i]


num = [3, 1, 5, 9]
generate_subset_size_k(4, num)
print(num)