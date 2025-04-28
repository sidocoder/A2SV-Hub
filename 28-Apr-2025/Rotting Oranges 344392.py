# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def inbound(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            return True
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for a in range(rows):
            for b in range(cols):
                if grid[a][b] == 1:
                    fresh += 1
                if grid[a][b] == 2:
                    queue.append((a, b, 0))

        direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        minutes = 0

        while queue:
            r, c, time = queue.popleft()
            minutes = max(minutes, time)

            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, time + 1))

        return minutes if fresh == 0 else -1
