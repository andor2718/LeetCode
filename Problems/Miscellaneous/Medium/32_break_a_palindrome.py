# https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        mid = len(palindrome) // 2
        for idx in range(mid):
            if palindrome[idx] != 'a':
                return f"{palindrome[:idx]}{'a'}{palindrome[idx + 1:]}"
        return f"{palindrome[:-1]}{'b'}"
