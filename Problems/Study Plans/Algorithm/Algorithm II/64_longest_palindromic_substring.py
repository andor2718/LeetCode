# https://leetcode.com/problems/longest-palindromic-substring/

def get_max_palindromic_radius(s: str, left: int, right: int) -> int:
    radius = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        radius += 1
        left -= 1
        right += 1
    return radius


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_substring = s[0]  # A single character is always palindromic
        for idx in range(len(s)):
            # Odd len substring
            curr_radius = get_max_palindromic_radius(s, idx - 1, idx + 1)
            if 2 * curr_radius + 1 > len(max_substring):
                max_substring = s[idx - curr_radius: idx + curr_radius + 1]
            if idx < len(s) - 1 and s[idx] == s[idx + 1]:
                # Even len substring, middle doubled
                curr_radius = get_max_palindromic_radius(s, idx - 1, idx + 2)
                if 2 * curr_radius + 2 > len(max_substring):
                    max_substring = s[idx - curr_radius: idx + curr_radius + 2]
        return max_substring
