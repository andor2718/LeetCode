# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
        runner_idx = 0
        for idx in range(len(nums) - zero_cnt):
            while nums[runner_idx] == 0:
                runner_idx += 1
            nums[idx] = nums[runner_idx]
            runner_idx += 1
        for idx in range(len(nums) - zero_cnt, len(nums)):
            nums[idx] = 0
