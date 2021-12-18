# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        min_len = min(map(len, strs))
        for char_idx in range(min_len):
            for str_idx in range(1, len(strs)):
                if strs[str_idx - 1][char_idx] != strs[str_idx][char_idx]:
                    return strs[0][:char_idx]
        return strs[0][:min_len]
