# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        # Model friends
        first_node = ListNode(1)
        last_node = first_node
        for i in range(2, n + 1):
            curr_node = ListNode(i, next=first_node, prev=last_node)
            last_node.next = curr_node
            last_node = curr_node
        first_node.prev = last_node
        # Simulate game
        curr_node = first_node
        nr_of_players = n
        k -= 1  # In every iteration, we are supposed to make k - 1 steps.
        while nr_of_players != 1:
            steps_to_make = k % nr_of_players  # No need to run in circles.
            for _ in range(steps_to_make):
                curr_node = curr_node.next
            curr_node.prev.next, curr_node.next.prev, curr_node = (
                curr_node.next, curr_node.prev, curr_node.next)
            nr_of_players -= 1
        # We have the winner
        return curr_node.val
