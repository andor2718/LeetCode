# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        digits = list()
        carry = 0
        for idx in reversed(range(max_len)):
            digit1 = int(num1[idx])
            digit2 = int(num2[idx])
            carry, curr_digit = divmod(digit1 + digit2 + carry, 10)
            digits.append(str(curr_digit))
        if carry:
            digits.append(str(carry))
        return ''.join(reversed(digits))
