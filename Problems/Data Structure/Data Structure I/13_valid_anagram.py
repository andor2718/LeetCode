# https://leetcode.com/problems/valid-anagram/

def canConstruct(ransomNote: str, magazine: str) -> bool:
    available_chars = dict()
    for char in magazine:
        available_chars[char] = available_chars.get(char, 0) + 1
    for char in ransomNote:
        if char not in available_chars or available_chars[char] == 0:
            return False
        else:
            available_chars[char] -= 1
    return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return canConstruct(s, t)
