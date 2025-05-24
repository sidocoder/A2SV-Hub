# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        street_dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        dir_to_street = {
            (0, 1): [1, 4, 6],
            (0, -1): [1, 3, 5],
            (1, 0): [2, 3, 4],
            (-1, 0): [2, 5, 6],
        }

        for i in range(m):
            for j in range(n):
                for dx, dy in street_dirs[grid[i][j]]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] in dir_to_street[(-dx, -dy)]:
                            uf.union(i * n + j, ni * n + nj)

        return uf.connected(0, m * n - 1)
        