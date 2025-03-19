# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        def backtrack(curr,level):
            if level > n + 1:
                return
            if len(curr) == k:
                comb.append(curr)
                return
            backtrack(curr, level+1)
            backtrack(curr + [level], level + 1)
        backtrack([], 1)
        return comb
        