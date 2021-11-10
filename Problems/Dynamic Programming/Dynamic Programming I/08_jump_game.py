# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        reachable_flags = [False for _ in range(len(nums))]
        reachable_flags[0] = True
        for idx in range(len(nums) - 1):
            if reachable_flags[idx] and nums[idx] != 0:
                for i in range(1, nums[idx] + 1):
                    try:
                        reachable_flags[idx + i] = True
                    except IndexError:
                        pass
                if reachable_flags[-1]:
                    return True
        return False
