# https://leetcode.com/problems/number-of-digit-one/

class Solution:
    def countDigitOne(self, n: int) -> int:
        result = threshold = 0
        divisor = limit = 10
        while n // limit > 0:
            limit *= 10
        while divisor <= limit:
            div, mod = divmod(n, divisor)
            result += div * (divisor // 10)
            if mod > threshold:
                result += min(mod - threshold, divisor // 10)
            divisor, threshold = 10 * divisor, 10 * threshold + 9
        return result
