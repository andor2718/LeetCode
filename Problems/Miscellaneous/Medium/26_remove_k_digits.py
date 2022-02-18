# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:  # Redundant check, but a nice shortcut.
            return '0'
        non_decreasing_digits = ['0']
        for curr_digit in num:
            while k != 0 and non_decreasing_digits[-1] > curr_digit:
                non_decreasing_digits.pop()
                k -= 1
            non_decreasing_digits.append(curr_digit)
        while k != 0:
            non_decreasing_digits.pop()
            k -= 1
        return str(int(''.join(non_decreasing_digits)))
