# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        curr_pos = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= curr_pos:
                curr_pos = i
        return curr_pos == 0
