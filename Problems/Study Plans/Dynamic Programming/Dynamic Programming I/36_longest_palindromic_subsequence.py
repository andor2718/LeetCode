# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for row in range(len(s)):
            for col in range(len(s)):
                # Find len of longest common subsequence of s and reversed(s).
                if s[row] == s[-1 - col]:
                    diagonal_top_left = (
                        dp[row - 1][col - 1] if row > 0 and col > 0 else 0)
                    dp[row][col] = diagonal_top_left + 1
                else:
                    top = dp[row - 1][col] if row > 0 else 0
                    left = dp[row][col - 1] if col > 0 else 0
                    dp[row][col] = max(top, left)
        return dp[-1][-1]
