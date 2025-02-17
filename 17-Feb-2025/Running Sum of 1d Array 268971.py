# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
    
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            result.append(sum)
        return result
        