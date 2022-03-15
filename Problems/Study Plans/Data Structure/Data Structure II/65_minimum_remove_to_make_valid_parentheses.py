# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        unclosed_open_parentheses_indexes = list()
        for idx, char in enumerate(s):
            if char == '(':
                unclosed_open_parentheses_indexes.append(idx)
            elif char == ')':
                if unclosed_open_parentheses_indexes:
                    unclosed_open_parentheses_indexes.pop()
                else:
                    indexes_to_remove.add(idx)
        indexes_to_remove.update(unclosed_open_parentheses_indexes)
        result = list()
        for idx, char in enumerate(s):
            if idx not in indexes_to_remove:
                result.append(char)
        return ''.join(result)
