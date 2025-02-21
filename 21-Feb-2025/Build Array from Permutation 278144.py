# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans