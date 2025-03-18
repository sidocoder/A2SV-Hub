# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        
        prev_row = self.getRow(rowIndex - 1)
        
        row = [1]  
        for i in range(1, rowIndex):
            row.append(prev_row[i - 1] + prev_row[i])
        
        row.append(1)
        
        return row
