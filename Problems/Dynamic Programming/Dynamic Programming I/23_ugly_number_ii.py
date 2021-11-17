# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0 for _ in range(n)]
        ugly_numbers[0] = 1
        fact_2_idx = fact_3_idx = fact_5_idx = 0
        for idx in range(1, n):
            fact_2_candidate = ugly_numbers[fact_2_idx] * 2
            fact_3_candidate = ugly_numbers[fact_3_idx] * 3
            fact_5_candidate = ugly_numbers[fact_5_idx] * 5
            curr_ugly_num = min(
                fact_2_candidate, fact_3_candidate, fact_5_candidate)
            ugly_numbers[idx] = curr_ugly_num
            if curr_ugly_num == fact_2_candidate:
                fact_2_idx += 1
            if curr_ugly_num == fact_3_candidate:
                fact_3_idx += 1
            if curr_ugly_num == fact_5_candidate:
                fact_5_idx += 1
        return ugly_numbers[-1]
