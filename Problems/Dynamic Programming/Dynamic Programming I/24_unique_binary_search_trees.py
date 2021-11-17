# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        nums = [0 for _ in range(n + 1)]
        nums[0] = nums[1] = 1
        for idx in range(2, n + 1):
            nodes_without_root = idx - 1
            unique_trees = 0
            for i in range(nodes_without_root + 1):
                left_nodes = i
                right_nodes = nodes_without_root - left_nodes
                unique_trees += nums[left_nodes] * nums[right_nodes]
            nums[idx] = unique_trees
        return nums[-1]
