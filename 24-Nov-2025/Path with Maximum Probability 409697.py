# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = [[] for _ in range(n)]
        for (u, v), p in zip(edges, succProb):
            g[u].append((v, p))
            g[v].append((u, p))

        pq = [(-1.0, start_node)]
        best = [0.0] * n
        best[start_node] = 1.0

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob
            if node == end_node:
                return prob
            if prob < best[node]:
                continue
            for nei, p in g[node]:
                newp = prob * p
                if newp > best[nei]:
                    best[nei] = newp
                    heapq.heappush(pq, (-newp, nei))
        
        return 0.0
        