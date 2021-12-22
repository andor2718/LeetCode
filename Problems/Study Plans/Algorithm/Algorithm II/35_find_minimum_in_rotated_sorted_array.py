# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def find_offset(nums: list[int]) -> int:
    if len(nums) <= 1:
        return 0
    low = 0
    high = len(nums) - 1
    while low <= high:  # If no rotation, high will eventually become 0.
        if high == 0 or nums[high - 1] > nums[high]:
            return high
        middle = (low + high) // 2
        if nums[middle] > nums[high]:
            low = middle + 1
        else:
            high = middle


class Solution:
    def findMin(self, nums: list[int]) -> int:
        return nums[find_offset(nums)]
