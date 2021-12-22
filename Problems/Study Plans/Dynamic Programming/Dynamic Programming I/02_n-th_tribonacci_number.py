# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        second_last_num, last_num, curr_num = 0, 1, 1
        for _ in range(n - 2):
            next_num = second_last_num + last_num + curr_num
            second_last_num, last_num, curr_num = last_num, curr_num, next_num
        return curr_num
