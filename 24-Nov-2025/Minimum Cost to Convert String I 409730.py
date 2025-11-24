# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**18
        dist = [[INF]*26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
        
        for o, c, w in zip(original, changed, cost):
            x, y = ord(o)-97, ord(c)-97
            dist[x][y] = min(dist[x][y], w)
        
        for k in range(26):
            for i in range(26):
                if dist[i][k] == INF: continue
                for j in range(26):
                    if dist[k][j] == INF: continue
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        ans = 0
        for s, t in zip(source, target):
            if s == t: 
                continue
            x, y = ord(s)-97, ord(t)-97
            if dist[x][y] == INF:
                return -1
            ans += dist[x][y]
        
        return ans
        