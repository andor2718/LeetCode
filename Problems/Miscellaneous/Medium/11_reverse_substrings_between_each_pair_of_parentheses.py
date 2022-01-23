# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        # We'll use a list of lists to solve the problem.
        # The first list will accumulate the characters in good order,
        # and the lists after it will act like stacks, making it easy
        # to reverse the characters between brackets.
        char_lists = [[]]
        for char in s:
            if char == '(':
                char_lists.append(list())
            elif char == ')':
                # We want to use the last list as a stack -> reverse it!
                last_chars_reversed = reversed(char_lists.pop())
                char_lists[-1].extend(last_chars_reversed)
            else:
                char_lists[-1].append(char)
        return ''.join(char_lists[0])
