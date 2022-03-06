# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

class Solution:
    def countOrders(self, n: int) -> int:
        result, limit = 1, 10 ** 9 + 7
        # possible_sequences = math.factorial(2 * n).
        # ratio_of_valid_sequences = 1 / (2 ** n).
        # So what we need here is an efficient way to calculate
        # possible_sequences * ratio_of_valid_sequences mod limit.
        for i in range(2, 2 * n + 1):
            multiplier = i if i % 2 != 0 else i // 2
            result = (result * multiplier) % limit
        return result
