# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        def get_next(num: int) -> int:
            return nums[num]

        # "Detect start of cycle in a linked list" approach
        head = 0
        slow = get_next(head)
        fast = get_next(slow)
        while slow != fast:
            slow, fast = get_next(slow), get_next(get_next(fast))
        slow = head
        while slow != fast:
            slow, fast = get_next(slow), get_next(fast)  # Fast is slowed down
        return slow
