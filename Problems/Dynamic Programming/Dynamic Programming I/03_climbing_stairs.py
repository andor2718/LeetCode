# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        low_stair = 1
        mid_stair = 2
        top_stair = low_stair + mid_stair
        for _ in range(n - 3):
            low_stair, mid_stair = mid_stair, top_stair
            top_stair = low_stair + mid_stair
        return top_stair
