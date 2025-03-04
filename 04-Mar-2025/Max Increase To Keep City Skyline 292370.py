# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_rows = defaultdict(int)
        max_cols = defaultdict(int)
        for row in range(rows):
            for col in range(cols):
                cur_val = grid[row][col]
                max_rows[row] = max(max_rows[row],cur_val)
                max_cols[col] = max(max_cols[col],cur_val)
        result = 0
        for row in range(rows):
            for col in range(cols):
                result += min(max_rows[row], max_cols[col]) - grid[row][col]
       
        
        return result



        