# https://leetcode.com/problems/course-schedule/

class Graph:
    def __init__(self, node_cnt: int, edges: list[list[int]]):
        self.adj_lists = {node: list() for node in range(node_cnt)}
        for source, target in edges:
            self.adj_lists[source].append(target)

    def _find_cycle(self, source: int, node_visited: list[bool],
                    node_in_path: list[bool]) -> bool:
        node_visited[source] = True
        node_in_path[source] = True
        for node in self.adj_lists[source]:
            if node_in_path[node]:
                return True
            if not node_visited[node]:
                if self._find_cycle(node, node_visited, node_in_path):
                    return True
        node_in_path[source] = False  # Backtrack
        return False

    def contains_cycle(self) -> bool:
        node_visited = [False for _ in range(len(self.adj_lists))]
        node_in_path = [False for _ in range(len(self.adj_lists))]
        for node in self.adj_lists.keys():
            if not node_visited[node]:
                if self._find_cycle(node, node_visited, node_in_path):
                    return True
        return False


class Solution:
    def canFinish(
            self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = Graph(numCourses, prerequisites)
        return not graph.contains_cycle()
