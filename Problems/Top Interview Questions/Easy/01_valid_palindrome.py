# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char.lower() for char in s if char.isalnum()])
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left, right = left + 1, right - 1
        return True
