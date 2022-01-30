# https://leetcode.com/problems/count-largest-group/

def get_digit_sum(num: int) -> int:
    total = 0
    while num > 0:
        num, digit = divmod(num, 10)
        total += digit
    return total


class Solution:
    def countLargestGroup(self, n: int) -> int:
        max_group_size = 0
        digit_sum_to_group_size = dict()
        for i in range(1, n + 1):
            digit_sum = get_digit_sum(i)
            digit_sum_to_group_size[digit_sum] = (
                    digit_sum_to_group_size.get(digit_sum, 0) + 1)
            if digit_sum_to_group_size[digit_sum] > max_group_size:
                max_group_size = digit_sum_to_group_size[digit_sum]
        groups_with_max_group_size = 0
        for group_size in digit_sum_to_group_size.values():
            if group_size == max_group_size:
                groups_with_max_group_size += 1
        return groups_with_max_group_size
