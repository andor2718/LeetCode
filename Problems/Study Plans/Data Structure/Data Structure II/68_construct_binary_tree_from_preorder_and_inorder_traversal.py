# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def val_on_left(
        reference: int, val: int, val_to_inorder_idx: dict[int, int]) -> bool:
    return val_to_inorder_idx[val] < val_to_inorder_idx[reference]


def insert_val(
        root: TreeNode, val: int, val_to_inorder_idx: dict[int, int]) -> None:
    new_node = TreeNode(val=val)
    curr = root
    while True:
        if val_on_left(curr.val, val, val_to_inorder_idx):
            if curr.left:
                curr = curr.left
            else:
                curr.left = new_node
                return
        else:
            if curr.right:
                curr = curr.right
            else:
                curr.right = new_node
                return


class Solution:
    def buildTree(
            self, preorder: list[int], inorder: list[int]
    ) -> Optional[TreeNode]:
        val_to_inorder_idx = dict()
        for idx, val in enumerate(inorder):
            val_to_inorder_idx[val] = idx
        root = TreeNode(val=preorder[0])
        for val in preorder[1:]:
            insert_val(root, val, val_to_inorder_idx)
        return root
