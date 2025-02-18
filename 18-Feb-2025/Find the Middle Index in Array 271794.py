# Problem: Find the Middle Index in Array - https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(1,n+1):
            prefix[i] = nums[i-1] + prefix[i-1]
        
        for j in range(1,n+1):
            if prefix[-1]-prefix[j] == prefix[j-1]:
                return j-1
        else:
            return -1