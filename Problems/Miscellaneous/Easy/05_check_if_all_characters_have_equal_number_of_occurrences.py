# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_frequencies = dict()
        for char in s:
            char_frequencies[char] = char_frequencies.get(char, 0) + 1
        return len(set(char_frequencies.values())) == 1
