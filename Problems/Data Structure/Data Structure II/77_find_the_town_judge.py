# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_counts = [0 for _ in range(n + 1)]  # We'll ignore the 0th entry.
        for _, trusted in trust:
            trust_counts[trusted] += 1
        judge_candidate = None
        # Find the only candidate, if exists
        for trusted, trust_count in enumerate(trust_counts[1:], start=1):
            if trust_count == n - 1:
                if judge_candidate is None:
                    judge_candidate = trusted
                else:
                    return -1
        if judge_candidate is None:  # No candidate found.
            return -1
        else:  # Check if candidate trusts anybody.
            for truster, _ in trust:
                if truster == judge_candidate:
                    return -1
            return judge_candidate
