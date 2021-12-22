# https://leetcode.com/problems/pascals-triangle/

import math


class Solution:
    def generate(self, nrRows: int) -> list[list[int]]:
        return [[math.comb(n, k) for k in range(n + 1)] for n in range(nrRows)]
