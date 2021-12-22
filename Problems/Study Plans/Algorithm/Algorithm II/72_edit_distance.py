# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        # If this is reached, both strings are non-empty.
        word1_len = len(word1)
        word2_len = len(word2)
        # Create a 2D array called dp and initialize it properly
        # with the number of steps that are needed to transform the
        # words into empty strings. (The 0th row and the 0th col.)
        dp = [[0 for _ in range(word2_len + 1)] for _ in range(word1_len + 1)]
        for row in range(1, word1_len + 1):
            dp[row][0] = row
        for col in range(1, word2_len + 1):
            dp[0][col] = col
        # Solve problem dynamically.
        for row in range(1, word1_len + 1):
            for col in range(1, word2_len + 1):
                top = dp[row - 1][col]
                left = dp[row][col - 1]
                diagonal_top_left = dp[row - 1][col - 1]
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = diagonal_top_left
                else:
                    dp[row][col] = min(top, left, diagonal_top_left) + 1
        return dp[-1][-1]
