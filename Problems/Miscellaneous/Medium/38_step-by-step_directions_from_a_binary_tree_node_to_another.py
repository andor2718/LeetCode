# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
            self, root: TreeNode, startValue: int, destValue: int) -> str:
        # Find start and dest nodes and their depths. Make a parent LUT.
        start_node = dest_node = None
        curr_depth = start_depth = dest_depth = 0
        parent_lut = dict()
        nodes = [root]
        while nodes:
            next_nodes = list()
            for node in nodes:
                if node.val == startValue:
                    start_node, start_depth = node, curr_depth
                elif node.val == destValue:
                    dest_node, dest_depth = node, curr_depth
                if start_node is not None and dest_node is not None:
                    break  # We got all we need.
                for child in [node.left, node.right]:
                    if child:
                        parent_lut[child.val] = node
                        next_nodes.append(child)
            nodes = next_nodes
            curr_depth += 1
        # Find the lowest common ancestor of start node and dest node.
        start_runner, dest_runner = start_node, dest_node
        while start_depth != dest_depth:
            if start_depth < dest_depth:
                dest_runner = parent_lut[dest_runner.val]
                dest_depth -= 1
            else:
                start_runner = parent_lut[start_runner.val]
                start_depth -= 1
        while start_runner != dest_runner:
            start_runner = parent_lut[start_runner.val]
            dest_runner = parent_lut[dest_runner.val]
        lca_node = start_runner
        # Collect directions from start to lca.
        start_to_lca_directions = list()
        curr_node = start_node
        while curr_node != lca_node:
            start_to_lca_directions.append('U')
            curr_node = parent_lut[curr_node.val]
        # Collect directions from lca to dest.
        lca_to_dest_directions = list()
        curr_node = dest_node
        while curr_node != lca_node:
            parent = parent_lut[curr_node.val]
            direction = 'L' if curr_node == parent.left else 'R'
            lca_to_dest_directions.append(direction)
            curr_node = parent
        lca_to_dest_directions.reverse()
        # Generate result.
        return ''.join(start_to_lca_directions + lca_to_dest_directions)
