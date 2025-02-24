# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        freq = [0] * (n + 1)
        
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1  
        
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
        freq.pop()
        
        nums.sort(reverse=True)
        freq.sort(reverse=True)
        
        return sum(f * num for f, num in zip(freq, nums)) % MOD
