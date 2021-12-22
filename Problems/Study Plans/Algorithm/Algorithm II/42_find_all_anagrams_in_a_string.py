# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = list()
        if len(s) < len(p):
            return result
        p_letter_stat = dict()
        for char in p:
            p_letter_stat[char] = p_letter_stat.get(char, 0) + 1
        sliding_window_stat = dict()
        for i in range(len(p)):
            sliding_window_stat[s[i]] = sliding_window_stat.get(s[i], 0) + 1
        if p_letter_stat == sliding_window_stat:
            result.append(0)
        for i in range(len(p), len(s)):
            sliding_window_stat[s[i]] = sliding_window_stat.get(s[i], 0) + 1
            sliding_window_stat[s[i - len(p)]] -= 1
            if sliding_window_stat[s[i - len(p)]] == 0:
                sliding_window_stat.pop(s[i - len(p)])
            if p_letter_stat == sliding_window_stat:
                result.append(i - len(p) + 1)
        return result
