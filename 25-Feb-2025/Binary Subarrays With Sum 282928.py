# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def subarray_sum(x):
            if x < 0:
                return 0
            count = 0
            left = 0
            summ = 0
            for right in range(len(nums)):
                summ += nums[right]
                while summ > x:
                    summ -= nums[left]
                    left += 1
                count += (right - left + 1)
            return count
        return subarray_sum(goal) - subarray_sum(goal - 1)


