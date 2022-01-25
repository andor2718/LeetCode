# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum, curr_nodes = root.val, [root]
        best_level = curr_level = 1
        while curr_nodes:
            next_nodes = list()
            curr_sum = sum([node.val for node in curr_nodes])
            if curr_sum > max_sum:
                max_sum, best_level = curr_sum, curr_level
            for node in curr_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            curr_nodes, curr_level = next_nodes, curr_level + 1
        return best_level
