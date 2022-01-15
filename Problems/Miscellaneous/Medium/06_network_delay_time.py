# https://leetcode.com/problems/network-delay-time/

from typing import Union


class Graph:
    def __init__(self, node_cnt: int, weighted_edges: list[list[int]]):
        self._neighbors_and_weights = {
            node: list() for node in range(1, node_cnt + 1)}
        for source, target, weight in weighted_edges:
            self._neighbors_and_weights[source].append((target, weight))

    def get_max_dist(self, source: int) -> Union[int, float]:
        # Let's utilize Dijkstra's algorithm!
        inf = float('inf')
        distances = {node: inf for node in self._neighbors_and_weights.keys()}
        distances[source] = 0
        nodes_to_process = set(self._neighbors_and_weights.keys())
        while nodes_to_process:
            curr_node = min(nodes_to_process, key=lambda x: distances[x])
            nodes_to_process.remove(curr_node)
            curr_dist = distances[curr_node]
            if curr_dist == inf:  # Graph is not connected
                return inf
            for node, weight in self._neighbors_and_weights[curr_node]:
                if node in nodes_to_process:
                    distances[node] = min(distances[node], curr_dist + weight)
        return max(distances.values())


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = Graph(n, times)
        max_dist = graph.get_max_dist(k)
        return max_dist if max_dist != float('inf') else -1
