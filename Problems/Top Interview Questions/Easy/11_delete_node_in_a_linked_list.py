# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr_node = node
        next_node = curr_node.next
        while next_node.next:
            curr_node.val = next_node.val
            curr_node, next_node = next_node, next_node.next
        curr_node.val = next_node.val
        curr_node.next = None
