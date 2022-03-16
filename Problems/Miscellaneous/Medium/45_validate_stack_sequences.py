# https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(
            self, pushed: list[int], popped: list[int]) -> bool:
        length = len(pushed)  # len(pushed) == len(popped).
        stack = list()
        push_idx = pop_idx = 0
        while push_idx < length or pop_idx < length:
            if stack and pop_idx < length and popped[pop_idx] == stack[-1]:
                stack.pop()
                pop_idx += 1
            elif push_idx < length:
                stack.append(pushed[push_idx])
                push_idx += 1
            else:
                return False
        return True
