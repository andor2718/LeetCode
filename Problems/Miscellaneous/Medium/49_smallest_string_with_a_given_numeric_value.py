# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

from string import ascii_lowercase


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = list()
        max_val = len(ascii_lowercase)
        idx, alphabet = 1, f'_{ascii_lowercase}'
        while n != 0:
            n -= 1
            idx = max(idx, k - max_val * n)
            result.append(alphabet[idx])
            k -= idx
        return ''.join(result)
