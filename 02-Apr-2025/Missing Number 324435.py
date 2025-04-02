# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        set1 = set()
        set2 = set()
        ans = 0
        for num in nums:
            set1.add(num)
        for i in range(n + 1):
            set2.add(i)
        defference = set2 - set1
        for value in defference:
            ans += value
        return ans