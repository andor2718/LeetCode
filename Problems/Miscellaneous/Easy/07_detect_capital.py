# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in {word.upper(), word.lower(), word.capitalize()}
