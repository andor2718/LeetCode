# https://leetcode.com/problems/unique-paths/

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Alternatively, we could also return math.comb(m + n - 2, n - 1).
        return math.comb(m + n - 2, m - 1)
