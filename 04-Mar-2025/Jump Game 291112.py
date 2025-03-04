# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0 
        
        for i, jump in enumerate(nums):
            if i > maxReach:  
                return False
            maxReach = max(maxReach, i + jump)  
            if maxReach >= len(nums) - 1:  
                return True
        
        return False
        # for i in range(len(nums)):
        #     pos = 0
        #     while pos < len(nums):


        