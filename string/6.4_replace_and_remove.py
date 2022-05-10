"""
Given an array of char string, ['a', 'b', 'j', 'l']
return an new array new array, that replace a with two d and remove all b

Design:
Bruete-force method: 
a new array = []
What I can do is to loop throught the whole array and if char is is a then we append the new array with two d and continue,
this algorithms will use O(n) additional space,

Case when array have no a, just b
you do a forward iteration, and just delete b, you are not using any additionbal space

Case when array have no b, just a
You use no additonal space in that you just create a new array with the lenght of the old array plus the number of a in the old array,
then you do a backwards iterations


['a', 'b', 'j', 'l']
  ls
           |

['s','s','f','f','a','a','', '']
                      ls
"""


def replace_and_remove(nums):
    no_b, a_count = 0, 0
    for i in range(len(nums)):
        if nums[i] != 'b':
            nums[no_b] = nums[i]
            no_b += 1
        if nums[i] == 'a':
            a_count += 1
    
    curr_index, write_idx = no_b -1 , a_count -1 + no_b

    while curr_index >= 0:
        if nums[curr_index] == 'a':
            nums[write_idx -1: write_idx +1 ] = 'dd'
            write_idx -= 2
        else:
            nums[write_idx] = nums[curr_index]
            write_idx -= 1
        curr_index -= 1