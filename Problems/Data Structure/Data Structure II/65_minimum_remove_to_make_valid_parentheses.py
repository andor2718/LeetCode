# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = list()
        unclosed_open_parentheses_indexes = list()
        for idx, char in enumerate(s):
            if char == '(':
                unclosed_open_parentheses_indexes.append(idx)
            elif char == ')':
                if not unclosed_open_parentheses_indexes:
                    indexes_to_remove.append(idx)
                else:
                    unclosed_open_parentheses_indexes.pop()
        for idx in unclosed_open_parentheses_indexes:
            indexes_to_remove.append(idx)
        # NOTE: Our construction ensures that indexes_to_remove is sorted!
        for idx in reversed(indexes_to_remove):
            s = f'{s[:idx]}{s[idx + 1:]}'
        return s
