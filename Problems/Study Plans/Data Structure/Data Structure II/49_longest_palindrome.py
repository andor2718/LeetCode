# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_len = 0
        char_counts = dict()
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        odd_cnt_found = False
        for cnt in char_counts.values():
            if cnt % 2 == 0:
                max_len += cnt
            else:
                odd_cnt_found = True
                max_len += cnt - 1
        if odd_cnt_found:
            max_len += 1
        return max_len
