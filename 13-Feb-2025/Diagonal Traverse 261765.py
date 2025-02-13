# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        i, j = 0, 0
        direction = 1  
        
        for _ in range(m * n):
            result.append(mat[i][j])
            
            if direction == 1:
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1
            
            
            if j >= n:  
                i += 2
                j = n - 1
                direction = -1
            if i >= m:  
                j += 2
                i = m - 1
                direction = 1
            if i < 0:  
                i = 0
                direction = -1
            if j < 0:  
                j = 0
                direction = 1
                
        return result
