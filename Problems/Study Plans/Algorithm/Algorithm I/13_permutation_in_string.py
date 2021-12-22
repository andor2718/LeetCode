# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_stat = dict()
        for char in s1:
            s1_stat[char] = s1_stat.get(char, 0) + 1
        s2_substring_stat = dict()
        for char in s2[:len(s1)]:
            s2_substring_stat[char] = s2_substring_stat.get(char, 0) + 1
        if s1_stat == s2_substring_stat:
            return True
        for idx in range(len(s1), len(s2)):
            s2_substring_stat[s2[idx - len(s1)]] -= 1
            if s2_substring_stat[s2[idx - len(s1)]] == 0:
                s2_substring_stat.pop(s2[idx - len(s1)])
            s2_substring_stat[s2[idx]] = s2_substring_stat.get(s2[idx], 0) + 1
            if s1_stat == s2_substring_stat:
                return True
        return False
