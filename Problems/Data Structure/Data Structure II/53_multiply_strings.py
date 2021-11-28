# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        addends = list()
        for idx, digit2 in enumerate(num2):
            carry = 0
            digits = [0 for _ in range(len(num2) - idx - 1)]
            for digit1 in reversed(num1):
                carry, digit = divmod(int(digit1) * int(digit2) + carry, 10)
                digits.append(digit)
            if carry:
                digits.append(carry)
            digits.reverse()
            addend = digits[0]
            for digit in digits[1:]:
                addend = 10 * addend + digit
            addends.append(addend)
        return str(sum(addends))
