# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        char_to_idx = dict()
        word_to_idx = dict()
        idx = 0
        while idx < len(pattern):  # Or len(s), since they are equal.
            char, word = pattern[idx], s[idx]
            char_to_idx[char] = char_to_idx.get(char, []) + [idx]
            word_to_idx[word] = word_to_idx.get(word, []) + [idx]
            idx += 1
        return list(char_to_idx.values()) == list(word_to_idx.values())
