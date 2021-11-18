# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 1:
            return n == 1
        return int(f'{n:b}'[1:]) == 0
