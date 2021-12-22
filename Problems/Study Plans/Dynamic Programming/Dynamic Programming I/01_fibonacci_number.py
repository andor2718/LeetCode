# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        second_last_fib = 0
        last_fib = 1
        for _ in range(n - 1):
            second_last_fib, last_fib = last_fib, second_last_fib + last_fib
        return last_fib
