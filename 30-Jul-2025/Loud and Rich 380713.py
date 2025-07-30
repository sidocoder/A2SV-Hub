# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:    
        n = len(quiet)
        graph = defaultdict(list)

        for a, b in richer:
            graph[b].append(a)

        @lru_cache(None)
        def dfs(person):
            quietest = person
            for richer_person in graph[person]:
                candidate = dfs(richer_person)
                if quiet[candidate] < quiet[quietest]:
                    quietest = candidate
            return quietest

        return [dfs(i) for i in range(n)]
