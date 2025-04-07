# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # k = 0
        # for l, r, v in queries:
        #     for i in range(l, r + 1):
        #         nums[i] -= v
        #         k += 1
        #     if all(num <= 0 for num in nums):
        #         return k
        # return -1
        def canAchieveZeroArray(k: int) -> bool:
            temp = nums[:]
            delta = [0] * (len(nums) + 1)

            for i in range(k):
                l, r, val = queries[i]
                delta[l] -= val
                if r + 1 < len(nums):
                    delta[r + 1] += val

            current_decrement = 0
            for i in range(len(nums)):
                current_decrement += delta[i]
                temp[i] += current_decrement
                if temp[i] > 0:
                    return False
            return True
        
        left, right = 0, len(queries)
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if canAchieveZeroArray(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
