# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = dict()
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        return ''.join([char * cnt for char, cnt in sorted(
            char_counts.items(), reverse=True, key=lambda x: x[1])])
