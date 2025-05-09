# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        @cache

        def dfs(i,j):
            res = 1
            for x,y in directions:
                nr = i + x
                nc = j + y
                if 0 <= nr < n and 0 <= nc < m and matrix[i][j] < matrix[nr][nc]:
                    res = max(res, 1 + dfs(nr,nc))
            return res
        
        height = 1
        for i in range(n):
            for j in range(m):
                height = max(height,dfs(i,j))
        return height 


        