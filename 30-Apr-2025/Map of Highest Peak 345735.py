# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        ans = [[-1 for _ in range(cols)] for _ in range(rows)]

        queue = deque()
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    queue.append((i,j))
                    ans[i][j] = 0
        
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
         
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and ans[nr][nc] == -1:
                    ans[nr][nc] = ans[r][c] + 1
                    queue.append((nr, nc))

        return ans

                    
            




        



