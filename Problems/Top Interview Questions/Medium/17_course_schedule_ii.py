# https://leetcode.com/problems/course-schedule-ii/

from collections import deque


class Graph:
    def __init__(self, node_cnt: int):
        self.adj_lists = {node: list() for node in range(node_cnt)}

    def add_edge(self, source: int, target: int) -> None:
        self.adj_lists[source].append(target)

    def get_topological_ordering(self) -> list[int]:
        result = list()
        available_nodes = deque()
        # Calculate in-degree of every node
        in_degrees = [0 for _ in range(len(self.adj_lists))]
        for adj_list in self.adj_lists.values():
            for node in adj_list:
                in_degrees[node] += 1
        # Start with independent nodes
        for node, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                available_nodes.append(node)
        # Process every available node from the queue, one at a time
        while available_nodes:
            curr_node = available_nodes.popleft()
            result.append(curr_node)
            # Virtually delete processed node and update available nodes
            for node in self.adj_lists[curr_node]:
                in_degrees[node] -= 1
                if in_degrees[node] == 0:
                    available_nodes.append(node)
        # There's a topological ordering <=> we could process every node
        return result if len(result) == len(self.adj_lists) else list()


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: list[list[int]]) -> list[int]:
        graph = Graph(numCourses)
        for target, source in prerequisites:  # Flip edges
            graph.add_edge(source, target)
        return graph.get_topological_ordering()
