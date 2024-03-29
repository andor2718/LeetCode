# https://leetcode.com/problems/clone-graph/

from copy import deepcopy


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        return deepcopy(node)  # No need to reinvent the wheel...
