# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                dx = x1 - x2
                dy = y1 - y2
                if dx * dx + dy * dy <= r1 * r1:
                    graph[i].append(j)
        
        def dfs(u, visited):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v, visited)
        
        max_detonated = 0
        for i in range(n):
            visited = set()
            dfs(i, visited)
            max_detonated = max(max_detonated, len(visited))
        
        return max_detonated
