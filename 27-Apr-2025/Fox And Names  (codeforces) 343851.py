# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import deque

n = int(input())
names = []
for _ in range(n):
    names.append(input().strip())

graph = [[] for _ in range(26)]
indegree = [0] * 26

for i in range(n-1):
    s, t = names[i], names[i+1]
    minlen = min(len(s), len(t))
    found = False
    for j in range(minlen):
        if s[j] != t[j]:
            u = ord(s[j]) - ord('a')
            v = ord(t[j]) - ord('a')
            graph[u].append(v)
            indegree[v] += 1
            found = True
            break
    if not found and len(s) > len(t):
        print("Impossible")
        exit()

q = deque()
for i in range(26):
    if indegree[i] == 0:
        q.append(i)

res = []
while q:
    u = q.popleft()
    res.append(u)
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

if len(res) != 26:
    print("Impossible")
else:
    ans = ''.join(chr(x + ord('a')) for x in res)
    print(ans)
