"""
Given the non negative integer array, add 1 to the array. 

[3, 4, 6] -> [3, 4, 7]


"""


def plus_one(nums: list[int]) -> list:
    nums[-1] += 1

    for i in reversed(range(1, len(nums))):
        if nums[i] != 10:
            break
        nums[i] = 0
        nums[i-1] += 1

    if nums[0] == 10:
        nums[0] = 1
        nums.append(0)

    return nums


if __name__ == "__main__":
    print(plus_one([4, 5, 5]))
    print('break')
    print(plus_one([5, 3, 9]))
    print("break")
    print(plus_one([9, 9, 9]))
 