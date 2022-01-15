# https://leetcode.com/problems/network-delay-time/

class Graph:
    def __init__(self, node_cnt: int, edges_with_dists: list[list[int]]):
        self._neighbors_and_dists = {
            node: list() for node in range(1, node_cnt + 1)}
        for source, target, dist in edges_with_dists:
            self._neighbors_and_dists[source].append((target, dist))

    def get_max_dist(self, source: int) -> int:
        # Let's utilize Dijkstra's algorithm!
        inf = float('inf')
        dists_from_source = {
            node: inf for node in self._neighbors_and_dists.keys()}
        dists_from_source[source] = 0
        nodes_to_process = set(self._neighbors_and_dists.keys())
        while nodes_to_process:
            curr_node = min(nodes_to_process, key=dists_from_source.get)
            nodes_to_process.remove(curr_node)
            curr_dist_from_source = dists_from_source[curr_node]
            if curr_dist_from_source == inf:  # Graph is not connected
                return -1
            for node, dist in self._neighbors_and_dists[curr_node]:
                if node in nodes_to_process:
                    dists_from_source[node] = min(
                        dists_from_source[node], curr_dist_from_source + dist)
        return max(dists_from_source.values())


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = Graph(n, times)
        return graph.get_max_dist(k)
