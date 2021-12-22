# https://leetcode.com/problems/generate-parentheses/

def generate_parenthesis(n: int, memo: dict[int, list[str]]) -> list[str]:
    if n == 0:
        return ['']
    if n == 1:
        return ['()']
    if n in memo:
        return memo[n]
    result = list()
    for i in range(n):
        middles = generate_parenthesis(i, memo)
        sides = generate_parenthesis(n - 1 - i, memo)
        for middle in middles:
            for side in sides:
                result.append(f'({middle}){side}')
    memo[n] = result
    return result


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return generate_parenthesis(n, dict())
