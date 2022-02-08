# https://leetcode.com/problems/add-digits/

class Solution:
    # NOTE: Source of the direct formula:
    # https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        base = 10
        return 1 + (num - 1) % (base - 1)
