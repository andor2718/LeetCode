# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trusted_by = [[] for _ in range(n + 1)]  # We'll ignore the 0th element
        for truster, trusted in trust:
            trusted_by[trusted].append(truster)
        judge_candidate = None
        # Find the only candidate, if exists
        for trusted, trusting_people in enumerate(trusted_by[1:], start=1):
            if len(trusting_people) == n - 1:
                if judge_candidate is None:
                    judge_candidate = trusted
                else:
                    return -1
        if judge_candidate is None:  # No candidate found
            return -1
        else:  # Check if candidate trusts anybody
            for truster, _ in trust:
                if truster == judge_candidate:
                    return -1
            return judge_candidate
