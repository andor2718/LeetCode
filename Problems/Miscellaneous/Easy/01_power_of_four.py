# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Returns True if n is positive, a power of 2, and the set bit is
        at an odd index (one-based) from right to left.
        Returns False otherwise.
        """
        if n <= 0:
            return False
        if n & (n - 1) != 0:
            return False
        bitmask = int(b'01' * 16, 2)  # We need no more than 32 bits to check.
        return n == n & bitmask
