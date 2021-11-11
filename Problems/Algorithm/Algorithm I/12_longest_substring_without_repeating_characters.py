# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        window = ''
        for char in s:
            if char not in window:
                window += char
            else:
                if len(window) > max_len:
                    max_len = len(window)
                window = f'{window[window.index(char) + 1:]}{char}'
        return max(max_len, len(window))
