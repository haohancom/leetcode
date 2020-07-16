def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashMap = {}
    for i, val in enumerate(nums):
        if val in hashMap:
            return [hashMap[val], i]
        hashMap[target - val] = i


class Solution(object):
    nums = [3, 3]
    print(twoSum(nums, 6))
