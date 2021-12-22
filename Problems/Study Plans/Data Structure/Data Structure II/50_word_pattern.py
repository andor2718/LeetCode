# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        char_to_word = dict()
        reserved_words = set()
        idx = 0
        while idx < len(pattern):  # Or len(s), since they are equal.
            char, word = pattern[idx], s[idx]
            if char not in char_to_word:
                if word not in reserved_words:
                    char_to_word[char] = word
                    reserved_words.add(word)
                else:
                    return False
            else:
                if char_to_word[char] != word:
                    return False
            idx += 1
        return True
