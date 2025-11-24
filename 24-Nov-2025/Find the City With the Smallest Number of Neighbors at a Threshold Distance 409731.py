# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        def dijkstra(start):
            dist = [10**15] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]: 
                    continue
                for nei, w in g[node]:
                    nd = d + w
                    if nd < dist[nei]:
                        dist[nei] = nd
                        heapq.heappush(pq, (nd, nei))
            return dist

        best = float('inf')
        ans = -1

        for i in range(n):
            dist = dijkstra(i)
            count = sum(1 for d in dist if 0 < d <= distanceThreshold)
            if count <= best:
                best = count
                ans = i
        
        return ans