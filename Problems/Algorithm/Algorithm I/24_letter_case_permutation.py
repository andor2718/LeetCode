# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        if not s:
            return ['']
        char = s[0]
        perms = self.letterCasePermutation(s[1:])
        result = list()
        for perm in perms:
            if char.isdigit():
                result.append(f'{char}{perm}')
            else:
                result.append(f'{char.lower()}{perm}')
                result.append(f'{char.upper()}{perm}')
        return result
