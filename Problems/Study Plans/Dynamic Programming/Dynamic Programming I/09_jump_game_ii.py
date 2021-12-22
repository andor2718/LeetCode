# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: list[int]) -> int:
        curr_pos = 0
        best_jump_pos = 0
        jumps = 0
        for i in range(len(nums) - 1):
            best_jump_pos = max(best_jump_pos, i + nums[i])
            if i == curr_pos:
                curr_pos = best_jump_pos
                jumps += 1
        return jumps
