# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        char_frequencies = dict()
        for char in s:
            char_frequencies[char] = char_frequencies.get(char, 0) + 1
        char_frequencies = list(char_frequencies.items())
        char_frequencies.sort(reverse=True, key=lambda x: x[1])
        return ''.join([char * freq for char, freq in char_frequencies])
