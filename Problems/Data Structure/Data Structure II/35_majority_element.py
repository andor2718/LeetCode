# https://leetcode.com/problems/majority-element/

def get_end_idx(nums: list[int], low: int, high: int, target: int) -> int:
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
    def majorityElement(self, nums: list[int]) -> int:
        majority_threshold = len(nums) // 2
        nums.sort()
        start = 0
        while start < len(nums):
            num = nums[start]
            end = get_end_idx(nums, start, len(nums) - 1, num)
            cnt = end - start + 1
            if cnt > majority_threshold:
                return num
            else:
                start = end + 1
