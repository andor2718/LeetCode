# https://leetcode.com/problems/find-the-difference/

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_letter_counts = Counter(s)
        t_letter_counts = Counter(t)
        for letter, count in t_letter_counts.items():
            if s_letter_counts.get(letter, 0) != count:
                return letter
