# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        # BFS approach with smart branch cutting (avoiding repetitions)
        reached_amounts = set()
        level_nr = 1
        curr_level = [0]
        next_level = []
        while curr_level or next_level:
            if curr_level:
                curr_num = curr_level.pop()
                for coin in coins:
                    next_num = curr_num + coin
                    if next_num == amount:
                        return level_nr
                    elif next_num < amount:
                        if next_num not in reached_amounts:
                            reached_amounts.add(next_num)
                            next_level.append(next_num)
            else:
                curr_level, next_level = next_level, []
                level_nr += 1
        return -1
