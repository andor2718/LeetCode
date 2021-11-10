# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: list[int]) -> int:
        distances = [float('inf') for _ in range(len(nums))]
        distances[-1] = 0
        for i in reversed(range(len(nums) - 1)):
            max_jump = nums[i]
            if max_jump != 0:
                distances[i] = 1 + min(distances[i + 1: i + max_jump + 1])
        return int(distances[0])
