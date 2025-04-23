# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

from collections import deque, defaultdict

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        reversed_graph = defaultdict(list)
        indegree = [0] * n

        for u in range(n):
            for v in graph[u]:
                reversed_graph[v].append(u)
                indegree[u] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])
        safe_nodes = []

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reversed_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(safe_nodes)
