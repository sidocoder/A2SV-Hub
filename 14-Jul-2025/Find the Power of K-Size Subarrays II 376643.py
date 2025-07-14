# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        num = []
        vec = []
        num.append(1)
        a = 1
        
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                a += 1
                num.append(a)
            else:
                a = 1
                num.append(a)

        for i in range(len(nums) - k + 1):
            if (num[i + k - 1] - num[i] + 1) == k:
                vec.append(nums[i + k - 1])
            else:
                vec.append(-1)
        return vec