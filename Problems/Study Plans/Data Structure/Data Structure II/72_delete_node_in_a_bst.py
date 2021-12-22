# https://leetcode.com/problems/delete-node-in-a-bst/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pop_max_left(root: TreeNode) -> int:
    last_node = root
    turned_left = True
    curr_node = last_node.left
    while curr_node.right:
        last_node = curr_node
        turned_left = False
        curr_node = curr_node.right
    curr_val = curr_node.val
    if not curr_node.left:
        if turned_left:
            last_node.left = None
        else:
            last_node.right = None
    else:
        if turned_left:
            last_node.left = curr_node.left
        else:
            last_node.right = curr_node.left
    return curr_val


class Solution:
    def deleteNode(
            self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        sentinel = TreeNode(left=root)
        last_node = sentinel
        turned_left = True
        curr_node = root
        while True:
            if curr_node.val == key:
                if not curr_node.left and not curr_node.right:
                    if turned_left:
                        last_node.left = None
                    else:
                        last_node.right = None
                elif not curr_node.left:
                    if turned_left:
                        last_node.left = curr_node.right
                    else:
                        last_node.right = curr_node.right
                elif not curr_node.right:
                    if turned_left:
                        last_node.left = curr_node.left
                    else:
                        last_node.right = curr_node.left
                else:
                    replacement_val = pop_max_left(curr_node)
                    curr_node.val = replacement_val
                break
            else:
                if curr_node.val < key:
                    if not curr_node.right:
                        break
                    else:
                        last_node = curr_node
                        turned_left = False
                        curr_node = curr_node.right
                else:
                    if not curr_node.left:
                        break
                    else:
                        last_node = curr_node
                        turned_left = True
                        curr_node = curr_node.left
        return sentinel.left
