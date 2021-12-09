# https://leetcode.com/problems/all-paths-from-source-to-target/

def all_paths_source_target(curr_node_idx: int, graph: list[list[int]],
                            path: list[int], result: list[list[int]]) -> None:
    path.append(curr_node_idx)
    if curr_node_idx == len(graph) - 1:  # Reached last node.
        copy_of_path = list(path)
        result.append(copy_of_path)
    else:
        for node_idx in graph[curr_node_idx]:
            all_paths_source_target(node_idx, graph, path, result)
    path.pop()


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result = list()
        path = [0]
        for node_idx in graph[0]:
            all_paths_source_target(node_idx, graph, path, result)
        return result
