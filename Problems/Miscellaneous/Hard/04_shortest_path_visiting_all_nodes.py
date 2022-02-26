# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

from collections import namedtuple

Entry = namedtuple('Entry', ['node', 'bitmask'])


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        steps = 0
        if len(graph) == 1:
            return steps
        curr_entries = [Entry(node, 1 << node) for node in range(len(graph))]
        goal_bitmask = (1 << len(graph)) - 1
        seen_entries = set(curr_entries)
        while True:
            steps += 1
            next_entries = list()
            for entry in curr_entries:
                for neighbor in graph[entry.node]:
                    new_entry = Entry(neighbor, entry.bitmask | 1 << neighbor)
                    if new_entry.bitmask == goal_bitmask:
                        return steps
                    if new_entry not in seen_entries:
                        seen_entries.add(new_entry)
                        next_entries.append(new_entry)
            curr_entries = next_entries
