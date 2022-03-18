# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_stack, covered_chars, last_idx_of_char = list(), set(), dict()
        for idx, char in enumerate(s):
            last_idx_of_char[char] = idx
        for idx, char in enumerate(s):
            if char not in covered_chars:
                while (char_stack and char_stack[-1] > char
                       and last_idx_of_char[char_stack[-1]] > idx):
                    covered_chars.remove(char_stack.pop())
                char_stack.append(char)
                covered_chars.add(char)
        return ''.join(char_stack)
