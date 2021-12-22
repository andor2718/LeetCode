# https://leetcode.com/problems/3sum/

def find(nums: list[int], left: int, right: int, target: int) -> bool:
    while left <= right:
        mid = (left + right) // 2
        guess = nums[mid]
        if guess == target:
            return True
        elif guess < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        triplets = set()
        result = list()
        left = 0
        while left < len(nums) and nums[left] <= 0:
            right = len(nums) - 1
            needed = - nums[left] - nums[right]
            while left < right:
                if nums[left] <= needed <= nums[right]:
                    triplet = (nums[left], needed, nums[right])
                    if triplet not in triplets:
                        if find(nums, left + 1, right - 1, needed):
                            triplets.add(triplet)
                            result.append(list(triplet))
                right -= 1
                needed = - nums[left] - nums[right]
            val = nums[left]
            while left < len(nums) and nums[left] == val:
                left += 1
        return result
