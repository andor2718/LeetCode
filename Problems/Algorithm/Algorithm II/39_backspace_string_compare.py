# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = list()
        t_stack = list()
        for stack, string in [(s_stack, s), (t_stack, t)]:
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
        return s_stack == t_stack
