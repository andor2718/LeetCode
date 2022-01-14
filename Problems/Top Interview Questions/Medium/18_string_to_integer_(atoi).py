# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        # Ignore leading spaces
        idx = 0
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        # Return 0 if s is empty or contains nothing but spaces
        if idx == len(s):
            return 0
        # Determine sign
        num_is_negative = False
        if s[idx] in ['-', '+']:
            num_is_negative = s[idx] == '-'
            idx += 1
        # Calculate num
        num, min_num, max_num = 0, -2 ** 31, 2 ** 31 - 1
        while idx < len(s) and s[idx].isdigit():
            num = 10 * num + int(s[idx])
            idx += 1
            # Return clamped result if clamping is necessary
            if num_is_negative:
                if -num <= min_num:
                    return min_num
            else:
                if num >= max_num:
                    return max_num
        # Check sign and return result
        return num if not num_is_negative else -num
