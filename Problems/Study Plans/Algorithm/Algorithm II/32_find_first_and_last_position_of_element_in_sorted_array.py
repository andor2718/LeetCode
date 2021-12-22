# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def get_start_idx(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = nums[middle]
        if guess == target:
            if middle == 0 or nums[middle - 1] < target:
                return middle
            else:
                high = middle - 1
        elif guess < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def get_end_idx(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = nums[middle]
        if guess == target:
            if middle == len(nums) - 1 or nums[middle + 1] > target:
                return middle
            else:
                low = middle + 1
        elif guess < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start_idx = get_start_idx(nums, target)
        if start_idx == -1:
            return [-1, -1]
        end_idx = get_end_idx(nums, target)
        return [start_idx, end_idx]
