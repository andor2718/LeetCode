# https://leetcode.com/problems/min-cost-to-connect-all-points/

class DSU:
    def __init__(self, item_cnt: int):
        self.entries = [-1 for _ in range(item_cnt)]

    def _find(self, idx: int) -> int:
        path = list()
        while self.entries[idx] >= 0:
            path.append(idx)
            idx = self.entries[idx]
        representative = idx
        for idx in path:  # Path compression
            self.entries[idx] = representative
        return representative

    def are_in_same_set(self, item_1: int, item_2: int) -> bool:
        representative_1 = self._find(item_1)
        representative_2 = self._find(item_2)
        return representative_1 == representative_2

    def union(self, item_1: int, item_2: int) -> None:
        if self.are_in_same_set(item_1, item_2):
            return
        representative_1 = self._find(item_1)
        representative_2 = self._find(item_2)
        size_1 = -self.entries[representative_1]
        size_2 = -self.entries[representative_2]
        new_size = size_1 + size_2
        if size_1 <= size_2:  # Merge set_1 into set_2
            self.entries[representative_2] = -new_size
            self.entries[representative_1] = representative_2
        else:  # Merge set_2 into set_1
            self.entries[representative_1] = -new_size
            self.entries[representative_2] = representative_1


class Edge:
    def __init__(self, source: int, target: int, cost: int):
        self.source = source
        self.target = target
        self.cost = cost

    def __lt__(self, other) -> bool:
        return self.cost < other.cost


def get_edges_with_manhattan_costs(
        points: list[list[int]]) -> list[Edge]:
    edges = list()
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            x_i, y_i = points[i][0], points[i][1]
            x_j, y_j = points[j][0], points[j][1]
            cost = abs(x_i - x_j) + abs(y_i - y_j)
            edges.append(Edge(i, j, cost))
    return edges


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        if len(points) <= 1:
            return 0
        # Let's use Kruskal's algorithm!
        # Make a complete graph where points[idx] is represented by number idx
        # Remember the cost of every edge and sort them by cost in desc order,
        # so we can pop the next yet unseen edge with min cost efficiently
        edges = get_edges_with_manhattan_costs(points)
        edges.sort(reverse=True)
        # For a graph with N nodes, we need N-1 edges to create a spanning tree
        edges_needed = len(points) - 1
        total_cost = 0
        dsu = DSU(len(points))  # Detect potential cycles efficiently with DSU
        # A complete graph has N**(N-2) different spanning trees
        # At least one of them is of min cost, so the loop will
        # certainly terminate before we run out of edges
        while edges_needed != 0:
            curr_edge = edges.pop()  # Next yet unconsidered edge with min cost
            # Include current edge if it does not create a cycle
            if not dsu.are_in_same_set(curr_edge.source, curr_edge.target):
                dsu.union(curr_edge.source, curr_edge.target)
                total_cost += curr_edge.cost
                edges_needed -= 1
        return total_cost
