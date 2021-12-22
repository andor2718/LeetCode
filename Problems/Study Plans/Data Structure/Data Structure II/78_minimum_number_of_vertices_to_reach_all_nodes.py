# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(
            self, n: int, edges: list[list[int]]) -> list[int]:
        in_degrees = [0 for _ in range(n)]
        for _, target in edges:
            in_degrees[target] += 1
        result = list()
        for vertex_idx, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                result.append(vertex_idx)
        return result
