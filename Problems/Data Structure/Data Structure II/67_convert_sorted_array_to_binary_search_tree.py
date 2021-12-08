# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        curr_node = TreeNode(val=nums[mid])
        left_child = self.sortedArrayToBST(nums[:mid])
        right_child = self.sortedArrayToBST(nums[mid + 1:])
        curr_node.left = left_child
        curr_node.right = right_child
        return curr_node
