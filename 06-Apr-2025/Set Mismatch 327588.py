# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = -1
        total = 0

        for num in nums:
            total += num
            if num in seen:
                duplicate = num
            seen.add(num)
        
        expected_sum = n * (n + 1) // 2
        missing = expected_sum - (total - duplicate)
        return [duplicate, missing]

        