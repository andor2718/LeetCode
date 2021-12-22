# https://leetcode.com/problems/valid-parentheses/

def bracket_pair_matches(open_bracket, close_bracket):
    if open_bracket == '(':
        return close_bracket == ')'
    elif open_bracket == '[':
        return close_bracket == ']'
    else:
        return close_bracket == '}'


def is_opener_bracket(bracket):
    return bracket in {'(', '[', '{'}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for bracket in s:
            if is_opener_bracket(bracket):
                stack.append(bracket)
            else:
                close_bracket = bracket
                try:
                    open_bracket = stack.pop()
                    if not bracket_pair_matches(open_bracket, close_bracket):
                        return False
                except IndexError:
                    return False
        return len(stack) == 0
