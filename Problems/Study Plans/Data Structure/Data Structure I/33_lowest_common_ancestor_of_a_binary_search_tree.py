# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(
        root: TreeNode, smaller: TreeNode, bigger: TreeNode) -> TreeNode:
    if smaller.val > root.val:
        return lowest_common_ancestor(root.right, smaller, bigger)
    elif bigger.val < root.val:
        return lowest_common_ancestor(root.left, smaller, bigger)
    else:
        return root


class Solution:
    def lowestCommonAncestor(
            self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smaller = p if p.val < q.val else q
        bigger = p if p.val > q.val else q
        return lowest_common_ancestor(root, smaller, bigger)
