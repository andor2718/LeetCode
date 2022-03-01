# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0]  # Number 0 has zero set bits.
        for num in range(1, n + 1):
            if num % 2 == 0:  # Then num >> 1 drops a 0, nr of 1s won't change.
                result.append(result[num // 2])
            else:  # Here num >> 1 drops a 1, so we must add 1 as compensation.
                result.append(result[num // 2] + 1)
        return result
