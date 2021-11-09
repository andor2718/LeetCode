# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        char_frequencies = dict()
        for char in s:
            char_frequencies[char] = char_frequencies.get(char, 0) + 1
        frequency_char_pairs = list()
        for char, freq in char_frequencies.items():
            frequency_char_pairs.append((freq, char))
        frequency_char_pairs.sort(reverse=True)
        return ''.join([char * freq for freq, char in frequency_char_pairs])
