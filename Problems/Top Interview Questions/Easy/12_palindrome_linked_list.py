# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def _reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:  # There's only one node, so it's a palindrome.
            return True
        sentinel = ListNode(next=head)
        slow = fast = sentinel
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        # Now slow is right before the middle. Let's reverse the list after it!
        reversed_head = _reverse(slow.next)
        slow.next = None  # Cut linked list here!
        # Compare nodes from left and right ends, move inwards until left ends.
        # NOTE: len(left) could be len(right) or len(right) - 1.
        # In the latter case it's safe to ignore right's last node, the middle.
        left, right = head, reversed_head
        while left:
            if left.val != right.val:
                return False
            else:
                left, right = left.next, right.next
        return True
