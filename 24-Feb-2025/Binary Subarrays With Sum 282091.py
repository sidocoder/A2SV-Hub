# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1 
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            count += prefix_count[prefix_sum - goal] 
            prefix_count[prefix_sum] += 1 
        
        return count
