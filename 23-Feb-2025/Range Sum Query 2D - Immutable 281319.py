# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        
        self.prefix_sum = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.prefix_sum[i][j] = matrix[i - 1][j - 1] + self.prefix_sum[i - 1][j] + self.prefix_sum[i][j - 1] - self.prefix_sum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix_sum[row2 + 1][col2 + 1] 
                - self.prefix_sum[row1][col2 + 1] 
                - self.prefix_sum[row2 + 1][col1] 
                + self.prefix_sum[row1][col1])

# Example usage:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1, col1, row2, col2)
