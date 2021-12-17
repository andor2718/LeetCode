# https://leetcode.com/problems/excel-sheet-column-number/

import string


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        char_to_num = dict()
        for num, char in enumerate(string.ascii_uppercase, start=1):
            char_to_num[char] = num
        base = len(string.ascii_uppercase)
        result = 0
        for exponent, char in enumerate(reversed(columnTitle)):
            result += char_to_num[char] * base ** exponent
        return result
