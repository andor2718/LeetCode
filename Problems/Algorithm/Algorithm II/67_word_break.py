# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        index_reachability_flags = [False for _ in range(len(s) + 1)]
        index_reachability_flags[0] = True
        for idx in range(len(s)):
            if not index_reachability_flags[idx]:
                continue
            for word in wordDict:
                if s.startswith(word, idx):
                    index_reachability_flags[idx + len(word)] = True
        return index_reachability_flags[-1]
