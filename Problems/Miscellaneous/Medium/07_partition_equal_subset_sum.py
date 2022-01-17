# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        # Do some basic checks.
        if total % 2 == 1:
            return False
        target = total // 2
        for num in nums:
            if num > target:
                return False
        # Maximize subset sum taking the "Knapsack Problem" approach.
        # The value of every number is also the number's weight,
        # and the maximal capacity of the knapsack is half of the sum.
        zeroed_row = [0 for _ in range(target + 1)]
        last_row = list(zeroed_row)
        for num in nums:
            curr_row = list(zeroed_row)
            for i in range(1, len(curr_row)):
                if num > i:
                    curr_row[i] = last_row[i]
                else:
                    curr_row[i] = max(last_row[i], num + last_row[i - num])
            last_row = curr_row
        # Check if maximum value in knapsack equals to target.
        return last_row[-1] == target
