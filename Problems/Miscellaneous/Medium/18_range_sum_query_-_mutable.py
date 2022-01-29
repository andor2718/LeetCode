# https://leetcode.com/problems/range-sum-query-mutable/

# Let's use a Fenwick tree!
class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = [0]  # Dummy val -> Our Fenwick tree should start at idx 1.
        self.nums.extend(nums)
        for idx in range(1, len(self.nums)):
            parent_idx = idx + self._get_rsb(idx)
            if parent_idx < len(self.nums):
                self.nums[parent_idx] += self.nums[idx]

    def update(self, index: int, val: int) -> None:
        idx = self._get_actual_index(index)
        curr = self._sum_range(idx, idx)
        diff = val - curr
        while idx < len(self.nums):
            self.nums[idx] += diff
            idx += self._get_rsb(idx)

    def sumRange(self, left: int, right: int) -> int:
        left_idx = self._get_actual_index(left)
        right_idx = self._get_actual_index(right)
        return self._sum_range(left_idx, right_idx)

    def _get_sum(self, idx: int) -> int:
        total = 0
        while idx > 0:
            total += self.nums[idx]
            idx -= self._get_rsb(idx)
        return total

    def _sum_range(self, left: int, right: int) -> int:
        return self._get_sum(right) - self._get_sum(left - 1)

    @staticmethod
    def _get_rsb(num: int):
        return -num & num

    @staticmethod
    def _get_actual_index(index: int) -> int:
        return index + 1  # Skip dummy.
