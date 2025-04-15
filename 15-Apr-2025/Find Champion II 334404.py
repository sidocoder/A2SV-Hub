# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        indegree = [0] * n
        for edge in edges:
            indegree[edge[1]] += 1

        champ = -1
        champ_count = 0

        for i in range(n):
            if indegree[i] == 0:
                champ_count += 1
                champ = i

        return champ if champ_count == 1 else -1