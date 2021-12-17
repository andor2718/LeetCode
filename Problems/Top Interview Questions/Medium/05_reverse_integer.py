# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        num = int((str(abs(x)))[::-1])
        if x < 0:
            num = -num
        if num < -2 ** 31 or num >= 2 ** 31:
            num = 0
        return num
