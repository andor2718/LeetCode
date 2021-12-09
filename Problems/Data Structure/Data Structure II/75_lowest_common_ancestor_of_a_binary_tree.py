# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_path(root: TreeNode, target: TreeNode, path: list[TreeNode]) -> bool:
    path.append(root)
    if root == target:
        return True
    if root.left:
        if get_path(root.left, target, path):
            return True
    if root.right:
        if get_path(root.right, target, path):
            return True
    path.pop()
    return False


class Solution:
    def lowestCommonAncestor(
            self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_to_p = list()
        get_path(root, p, path_to_p)
        path_to_p = set(path_to_p)
        path_to_q = list()
        get_path(root, q, path_to_q)
        for node in reversed(path_to_q):
            if node in path_to_p:
                return node
