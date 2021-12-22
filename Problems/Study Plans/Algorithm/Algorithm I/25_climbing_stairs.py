# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        second_to_last_staircase = 1
        last_staircase = 2
        for _ in range(3, n + 1):
            curr_staircase = last_staircase + second_to_last_staircase
            second_to_last_staircase = last_staircase
            last_staircase = curr_staircase
        return last_staircase
