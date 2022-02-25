# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        digits1 = list(map(int, version1.split('.')))
        digits2 = list(map(int, version2.split('.')))
        limit = max(len(digits1), len(digits2))
        for idx in range(limit):
            digit1 = digits1[idx] if idx < len(digits1) else 0
            digit2 = digits2[idx] if idx < len(digits2) else 0
            if digit1 < digit2:
                return -1
            elif digit1 > digit2:
                return 1
        return 0
