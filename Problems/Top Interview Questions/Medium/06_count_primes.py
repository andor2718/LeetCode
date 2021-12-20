# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        result = 1  # Count 2 in
        sqrt_of_limit = int(n ** 0.5)
        odd_num_start = 3  # First flag shall represent number 3
        odd_num_flags = [True for _ in range(odd_num_start, n, 2)]
        flags_len = len(odd_num_flags)
        for idx in range(flags_len):
            if odd_num_flags[idx]:
                prime = odd_num_start + 2 * idx
                if prime > sqrt_of_limit:
                    break  # Every listed composite number is flagged already
                start = 2 * idx * idx + 6 * idx + 3  # Index of {prime ** 2}
                for i in range(start, flags_len, prime):
                    odd_num_flags[i] = False
        for odd_num_flag in odd_num_flags:
            if odd_num_flag:
                result += 1
        return result
