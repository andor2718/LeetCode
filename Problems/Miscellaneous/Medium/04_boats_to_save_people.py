# https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        while left <= right:
            # NOTE: left == right may seem like a special case, but it's not.
            # Even if that person would fit in a boat twice, we increase the
            # number of boats by just one, and terminate the loop afterwards.
            if people[left] + people[right] <= limit:  # Pick both.
                left, right = left + 1, right - 1
            else:  # Pick people[right], as it's always <= limit.
                right -= 1
            boats += 1
        return boats
