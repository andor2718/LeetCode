# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return ['']
    digit_to_chars = ({'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                       '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'})
    result = list()
    continuations = letter_combinations(digits[1:])
    for char in digit_to_chars[digits[0]]:
        for continuation in continuations:
            result.append(f'{char}{continuation}')
    return result


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        return letter_combinations(digits)
