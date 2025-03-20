# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def backtrack(curr,level):
            if level >= len(nums):
                subset.append(curr[:])
                return
            
            
            backtrack(curr, level+1)
            curr.append(nums[level])
            backtrack( curr, level + 1)
            curr.pop()

        backtrack([], 0)
        return subset
