# https://leetcode.com/problems/rotate-array/

def flip(nums, low_idx, high_idx):
    while low_idx < high_idx:
        nums[low_idx], nums[high_idx] = nums[high_idx], nums[low_idx]
        low_idx += 1
        high_idx -= 1


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        k = k % len(nums)
        if k == 0:
            return
        flip(nums, 0, len(nums) - 1)
        flip(nums, 0, k - 1)
        flip(nums, k, len(nums) - 1)
