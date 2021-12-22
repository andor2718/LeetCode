# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
        for row in range(len(text2)):
            for col in range(len(text1)):
                if text2[row] == text1[col]:
                    diagonal_top_left = (
                        dp[row - 1][col - 1] if row > 0 and col > 0 else 0)
                    dp[row][col] = diagonal_top_left + 1
                else:
                    top = dp[row - 1][col] if row > 0 else 0
                    left = dp[row][col - 1] if col > 0 else 0
                    dp[row][col] = max(top, left)
        return dp[-1][-1]
