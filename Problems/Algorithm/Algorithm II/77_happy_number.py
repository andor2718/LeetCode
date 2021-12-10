# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = {n}
        while n != 1:
            total = 0
            while n > 0:
                n, last_digit = divmod(n, 10)
                total += last_digit * last_digit
            n = total
            if n in seen_nums:
                return False
            else:
                seen_nums.add(n)
        return True
