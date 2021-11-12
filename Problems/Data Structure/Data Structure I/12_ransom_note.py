# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available_chars = dict()
        for char in magazine:
            available_chars[char] = available_chars.get(char, 0) + 1
        for char in ransomNote:
            if char not in available_chars or available_chars[char] == 0:
                return False
            else:
                available_chars[char] -= 1
        return True
