# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {'(': ')', '{': '}', '[': ']'}
        close_stack = list()
        for bracket in s:
            if bracket in open_to_close:
                close_stack.append(open_to_close[bracket])
            elif not close_stack or close_stack.pop() != bracket:
                return False
        return len(close_stack) == 0
