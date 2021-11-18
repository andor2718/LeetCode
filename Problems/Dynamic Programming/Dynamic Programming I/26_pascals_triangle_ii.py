# https://leetcode.com/problems/pascals-triangle-ii/

def fact(n: int) -> int:
    if n < 0:
        raise ValueError('fact() not defined for negative values')
    if n <= 1:
        return 1
    result = 1
    for factor in range(2, n + 1):
        result *= factor
    return result


def choose(n: int, k: int) -> int:
    if 0 <= k < n:
        return fact(n) // (fact(k) * fact(n - k))
    else:
        return 0


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1 for _ in range(rowIndex + 1)]
        if rowIndex >= 2:
            for k in range(1, rowIndex):
                row[k] = choose(rowIndex, k)
        return row
