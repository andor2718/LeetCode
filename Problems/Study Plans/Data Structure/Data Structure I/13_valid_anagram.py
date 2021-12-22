# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char_freq = dict()
        t_char_freq = dict()
        for s_char, t_char in zip(s, t):
            s_char_freq[s_char] = s_char_freq.get(s_char, 0) + 1
            t_char_freq[t_char] = t_char_freq.get(t_char, 0) + 1
        return s_char_freq == t_char_freq
