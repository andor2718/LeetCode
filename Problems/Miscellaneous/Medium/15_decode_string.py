# https://leetcode.com/problems/decode-string/

import enum


class States(enum.Enum):
    PARSING_CHARS = enum.auto()
    PARSING_DIGITS = enum.auto()
    LOOKING_FOR_CLOSING_BRACKET = enum.auto()


class Solution:
    def decodeString(self, s: str) -> str:
        decoded_strings = list()
        start = multiplier = open_brackets = 0
        state = States.PARSING_CHARS
        for idx in range(len(s) + 1):
            if state is States.PARSING_CHARS:
                # If we are parsing chars, three cases are possible:
                # 1. We reach the end of s;
                # 2. We find a digit;
                # 3. We find another char.
                # In cases 1. and 2., we add the chars we've seen since
                # start to decoded_strings. (Could be 0 or more.)
                # In case 3., we simply move on.
                if idx == len(s) or s[idx].isdigit():
                    decoded_strings.append(s[start: idx])
                    if idx != len(s):  # Redundant check, but nice to include.
                        start = idx
                        state = States.PARSING_DIGITS
            elif state is States.PARSING_DIGITS:
                # Two cases are possible here:
                # 1. We find another digit and move on;
                # 2: We reach a '[' char. Now we know our multiplier,
                # time to look for the matching closing bracket.
                if s[idx] == '[':
                    multiplier = int(s[start: idx])
                    start = idx + 1
                    open_brackets = 1
                    state = States.LOOKING_FOR_CLOSING_BRACKET
            else:
                # We're looking for the closing bracket, skipping over
                # everything that's nested.
                # When we find it, we can decode the bracketed
                # sequence, add it to decoded_strings multiplier times,
                # and start looking for characters.
                if s[idx] == '[':
                    open_brackets += 1
                elif s[idx] == ']':
                    open_brackets -= 1
                    if open_brackets == 0:
                        decoded_string = self.decodeString(s[start: idx])
                        decoded_strings.append(multiplier * decoded_string)
                        start = idx + 1
                        state = States.PARSING_CHARS
        return ''.join(decoded_strings)
