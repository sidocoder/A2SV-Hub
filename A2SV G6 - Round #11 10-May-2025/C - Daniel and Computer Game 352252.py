# Problem: C - Daniel and Computer Game - https://codeforces.com/gym/604781/problem/C

from collections import deque

n, k = map(int, input().split())
L = input()
R = input()
walls = [L, R]
visited = [[False] * n for _ in range(2)]
q = deque()
q.append((0, 0, 0))
visited[0][0] = True
result = "NO"

while q:
    wall, pos, t = q.popleft()
    if pos < t:
        continue
    if pos + 1 < n and walls[wall][pos + 1] == '-' and not visited[wall][pos + 1]:
        visited[wall][pos + 1] = True
        q.append((wall, pos + 1, t + 1))
    if pos - 1 >= 0 and walls[wall][pos - 1] == '-' and not visited[wall][pos - 1]:
        if pos - 1 >= t + 1:
            visited[wall][pos - 1] = True
            q.append((wall, pos - 1, t + 1))
    new_pos = pos + k
    new_wall = 1 - wall
    if new_pos >= n:
        result = "YES"
        break
    if new_pos < n and walls[new_wall][new_pos] == '-' and not visited[new_wall][new_pos]:
        if new_pos >= t + 1:
            visited[new_wall][new_pos] = True
            q.append((new_wall, new_pos, t + 1))

print(result)
