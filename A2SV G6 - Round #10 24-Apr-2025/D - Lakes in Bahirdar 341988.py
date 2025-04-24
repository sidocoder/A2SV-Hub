# Problem: D - Lakes in Bahirdar - https://codeforces.com/gym/602812/problem/D

import sys
import threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, m, k = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    lakes = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def inbound(r, c):
        return 0 <= r < n and 0 <= c < m

    def dfs(i, j, cells):
        visited[i][j] = True
        cells.append((i, j))
        is_border = i == 0 or j == 0 or i == n - 1 or j == m - 1
        for x, y in directions:
            nr, nc = i + x, j + y
            if inbound(nr, nc) and not visited[nr][nc] and grid[nr][nc] == ".":
                result = dfs(nr, nc, cells)
                is_border = is_border or result
        return is_border

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == ".":
                cells = []
                touch_border = dfs(i, j, cells)
                if not touch_border:
                    lakes.append(cells)

    lakes.sort(key=len)
    cells_to_fill = 0
    lakes_to_fill = len(lakes) - k
    for i in range(lakes_to_fill):
        for x, y in lakes[i]:
            grid[x][y] = "*"
            cells_to_fill += 1

    print(cells_to_fill)
    for row in grid:
        print("".join(row))


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
