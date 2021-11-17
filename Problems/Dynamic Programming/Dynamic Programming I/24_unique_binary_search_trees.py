# https://leetcode.com/problems/unique-binary-search-trees/

def _num_trees(n: int, memo: dict[int, int]) -> int:
    if n in memo:
        return memo[n]
    n -= 1  # The root node is fixed.
    result = 0
    for i in range(n + 1):
        left_nodes = i
        right_nodes = n - i
        result += _num_trees(left_nodes, memo) * _num_trees(right_nodes, memo)
    memo[n + 1] = result  # Remember to compensate for the root!
    return result


class Solution:
    def numTrees(self, n: int) -> int:
        memo = {0: 1, 1: 1}
        return _num_trees(n, memo)
