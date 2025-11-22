# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums: 
            return 0
        
        arr = [nums.pop(0)]  
        
        for n in nums:
            if n > arr[-1]:  
                arr.append(n)
            else:  
                arr[bisect_left(arr, n)] = n

        return len(arr)  
