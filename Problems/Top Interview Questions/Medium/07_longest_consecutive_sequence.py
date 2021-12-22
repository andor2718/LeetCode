# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = list(set(nums))  # Repeated elements add no value
        idx_processed_flags = [False for _ in range(len(nums))]
        num_to_idx = {num: idx for idx, num in enumerate(nums)}
        max_cons_seq_len = 0
        for idx in range(len(nums)):
            if idx_processed_flags[idx]:
                continue  # Num already processed
            # Process num
            curr_seq_len = 1
            idx_processed_flags[idx] = True
            # Process consecutive numbers after num
            next_num = nums[idx] + 1
            while next_num in num_to_idx:
                curr_seq_len += 1
                idx_processed_flags[num_to_idx[next_num]] = True
                next_num += 1
            # Process consecutive numbers before num
            prev_num = nums[idx] - 1
            while prev_num in num_to_idx:
                curr_seq_len += 1
                idx_processed_flags[num_to_idx[prev_num]] = True
                prev_num -= 1
            # Update max
            max_cons_seq_len = max(max_cons_seq_len, curr_seq_len)
        return max_cons_seq_len
