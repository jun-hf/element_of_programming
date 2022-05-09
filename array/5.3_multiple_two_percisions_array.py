"""
Given two array [3, 3] and [1, 0] return the array as a multiple of the input array

"""


def multiple_array(nums1, nums2):
    if nums1[0] == 0 or nums2[0] == 0:
        return [0]
    
    sign = -1 if nums1[0] * nums2[0] < 0 else 1
    nums1[0], nums2[0] = abs(nums1[0]), abs(nums2[0])

    result = [0] * (len(nums1) + len(nums2))

    for i in reversed(range(nums1)):
        for j in reversed(range(nums2)):
            result[i +  j + 1] += nums2[j] * nums1[i]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1 ] =  result[i +  j + 1] % 10

    # result = result[next(x for i, x in )]


if __name__ == "__main__":
    print(multiple_array([0], [2, 3, 8]))
