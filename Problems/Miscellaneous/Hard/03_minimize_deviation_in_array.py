# https://leetcode.com/problems/minimize-deviation-in-array/

import heapq


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        # Preprocess: Start with all even numbers, keep track of the
        # smallest number in the list, build a max heap and find the
        # current diff between the smallest and the largest numbers.
        curr_min = float('inf')
        for idx in range(len(nums)):
            if nums[idx] % 2 != 0:
                nums[idx] *= 2
            curr_min = min(curr_min, nums[idx])
            nums[idx] *= -1  # We'll need a max heap.
        heapq.heapify(nums)
        min_diff = -nums[0] - curr_min
        # Preprocess done. Now we have a chance to find a smaller diff
        # as long as the largest number in the heap is even. We remove
        # that number, get the half of it, and push the new number back.
        # When the largest number is odd, we can't make it any smaller,
        # so the only way to find a smaller diff would be doubling the
        # smallest item in the list. If it's even, that's not possible,
        # and if it's odd, the double of it was considered already,
        # since in the beginning we started with all even numbers.
        while (curr_max := -nums[0]) % 2 == 0:
            half_of_curr_max = curr_max // 2
            heapq.heapreplace(nums, -half_of_curr_max)
            curr_min = min(curr_min, half_of_curr_max)
            curr_diff = -nums[0] - curr_min
            min_diff = min(min_diff, curr_diff)
        return min_diff
