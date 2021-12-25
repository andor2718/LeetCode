# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = list()
        carry = 1
        for digit in reversed(digits):
            carry, curr_digit = divmod(digit + carry, 10)
            result.append(curr_digit)
        if carry:
            result.append(carry)
        result.reverse()
        return result
