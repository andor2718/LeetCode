# https://leetcode.com/problems/power-of-three/

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 1:
            return n == 1
        base = 3
        exponent = int(math.log(n, base))
        return 3 ** exponent == n or 3 ** (exponent + 1) == n
