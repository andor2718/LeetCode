# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()  # Lazy solution :P
        low = 0
        high = len(s) - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low, high = low + 1, high - 1
