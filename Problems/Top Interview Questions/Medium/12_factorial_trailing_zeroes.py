# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # The number of trailing zeroes is the number of 10 factors.
        # 10 = 2 * 5, and if (5 ** i) is a factor of n, then (2 ** i)
        # is also it's factor, since the latter is always
        # smaller than the former (i >= 1).
        # So we just need to count the multiples of (5 ** i).
        pow_of_five = 5  # Start with 5 ** 1 = 5 (i = 1).
        result = 0
        while pow_of_five <= n:  # If pow_of_five > n, it can't be n's factor.
            # Every multiple of (5 ** i) will get counted i times, as supposed.
            result += n // pow_of_five
            pow_of_five *= 5
        return result
