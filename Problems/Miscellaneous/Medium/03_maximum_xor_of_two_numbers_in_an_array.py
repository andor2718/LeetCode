# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

import math


def get_bit_count(num: int) -> int:
    return 1 if num == 0 else int(math.log2(num)) + 1


def get_bits_with_leading_zeroes(num: int, width: int) -> str:
    return f'{num:b}'.zfill(width)


class Trie:
    class Node:
        def __init__(self):
            self.zero = None
            self.one = None

    def __init__(self, depth: int):
        self.root = self.Node()
        self.depth = depth

    def insert(self, num: int) -> None:
        bits = get_bits_with_leading_zeroes(num, self.depth)
        act_node = self.root
        for bit in bits:
            if bit == '0':
                if act_node.zero is None:
                    act_node.zero = self.Node()
                act_node = act_node.zero
            else:  # bit == '1'
                if act_node.one is None:
                    act_node.one = self.Node()
                act_node = act_node.one

    def get_max_xor(self, num: int) -> int:
        bits = get_bits_with_leading_zeroes(num, self.depth)
        act_node = self.root
        max_xor_pair_bits = list()
        for bit in bits:
            if bit == '0':
                if act_node.one is not None:
                    max_xor_pair_bits.append('1')
                    act_node = act_node.one
                else:
                    max_xor_pair_bits.append('0')
                    act_node = act_node.zero
            else:  # bit == '1'
                if act_node.zero is not None:
                    max_xor_pair_bits.append('0')
                    act_node = act_node.zero
                else:
                    max_xor_pair_bits.append('1')
                    act_node = act_node.one
        max_xor_pair = int(''.join(max_xor_pair_bits), 2)
        return num ^ max_xor_pair


class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        nums = set(nums)  # Remove duplicates
        max_bit_len = max(map(get_bit_count, nums))
        trie = Trie(depth=max_bit_len)
        for num in nums:
            trie.insert(num)
        max_xor = 0  # Any number with itself
        for num in nums:
            max_xor = max(max_xor, trie.get_max_xor(num))
        return max_xor
