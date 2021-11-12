# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq = dict()
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        for idx in range(len(s)):
            char = s[idx]
            if char_freq[char] == 1:
                return idx
        return -1
