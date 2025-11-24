# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        OR = 0
        for x in nums:
            OR |= x
        return OR * (1 << (len(nums) - 1))