# https://leetcode.com/problems/combinations/

class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.leaves = list()

    def __repr__(self):
        return f'Node: {self.val}'

    def grow(self, n: int) -> None:
        if self.val == n:
            return
        if not self.leaves:
            self.leaves = [Node(i) for i in range(self.val + 1, n + 1)]
        else:
            for node in self.leaves:
                node.grow(n)

    def combinations(self, depth: int) -> list[list[int]]:
        if depth == 0:
            return [[self.val]]
        combinations = list()
        for node in self.leaves:
            for combination in node.combinations(depth - 1):
                if self.val == 0:
                    combinations.append(combination)
                else:
                    combinations.append([self.val] + combination)
        return combinations


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        root = Node()
        for _ in range(k):
            root.grow(n)
        return root.combinations(k)
