# https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        idx = 0
        while idx < len(s):
            if s[idx: idx + 2] == '()':
                stack[-1] += 1
                idx += 2
            else:
                if s[idx] == '(':
                    stack.append(0)
                else:  # s[idx] == ')'
                    curr_score = stack.pop()
                    stack[-1] += 2 * curr_score
                idx += 1
        return stack[-1]
