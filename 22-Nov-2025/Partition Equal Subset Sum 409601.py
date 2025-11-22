# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2: 
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True
        
        return dp[target]

      
        
