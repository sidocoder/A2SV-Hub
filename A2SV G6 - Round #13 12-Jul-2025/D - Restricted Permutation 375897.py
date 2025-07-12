# Problem: D - Restricted Permutation - https://codeforces.com/gym/607625/problem/D

import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1  
    b -= 1
    graph[a].append(b)
    indegree[b] += 1

heap = []
for i in range(n):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

ans = []
while heap:
    curr = heapq.heappop(heap)
    ans.append(curr)

    for nei in graph[curr]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            heapq.heappush(heap, nei)

if len(ans) < n:
    print(-1)  
else:
    print(*[x + 1 for x in ans]) 
