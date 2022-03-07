# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

from __future__ import annotations
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Walker:
    def __init__(self, node: TreeNode,
                 prev: Optional[Walker] = None, direction: str = ''):
        self.node = node
        self.prev = prev
        self.direction = direction


def get_parent_lut(root: TreeNode) -> dict[int, TreeNode]:
    parent_lut = dict()
    nodes = [root]
    while nodes:
        next_nodes = list()
        for node in nodes:
            for child in [node.left, node.right]:
                if child:
                    parent_lut[child.val] = node
                    next_nodes.append(child)
        nodes = next_nodes
    return parent_lut


def get_start_node(node: TreeNode, start_value: int) -> TreeNode:
    nodes = [node]
    while True:
        next_nodes = list()
        for node in nodes:
            if node.val == start_value:
                return node
            for child in [node.left, node.right]:
                if child:
                    next_nodes.append(child)
        nodes = next_nodes


def get_dest_walker(start_node: TreeNode, dest_value: int,
                    parent_lut: dict[int, TreeNode]) -> Walker:
    walkers = [Walker(start_node)]
    seen_vals = set()
    while True:
        next_walkers = list()
        for walker in walkers:
            if walker.node.val == dest_value:
                return walker
            seen_vals.add(walker.node.val)
            if walker.node.left and walker.node.left.val not in seen_vals:
                next_walkers.append(Walker(walker.node.left, walker, 'L'))
            if walker.node.right and walker.node.right.val not in seen_vals:
                next_walkers.append(Walker(walker.node.right, walker, 'R'))
            if walker.node.val in parent_lut:
                parent = parent_lut[walker.node.val]
                if parent.val not in seen_vals:
                    next_walkers.append(Walker(parent, walker, 'U'))
        walkers = next_walkers


class Solution:
    def getDirections(
            self, root: TreeNode, startValue: int, destValue: int) -> str:
        parent_lut = get_parent_lut(root)
        start_node = get_start_node(root, startValue)
        walker = get_dest_walker(start_node, destValue, parent_lut)
        directions = list()
        while walker:
            directions.append(walker.direction)
            walker = walker.prev
        return ''.join(reversed(directions))
