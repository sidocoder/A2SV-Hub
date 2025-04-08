# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        visited = set()

        def dfs(node, c):
            color[node] = c
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == color[node]:
                    return False
            return True

        for i in range(n):
            if i not in visited:
                if not dfs(i, 0):
                    return False
        return True
