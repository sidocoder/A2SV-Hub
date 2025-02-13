# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ =  sum(nums[:k])
        max_average = summ/k

        for r in range(k, len(nums)):
            summ += nums[r]
            summ -= nums[r - k]
            max_average = max(max_average, summ/k)
        return max_average


        # right = left + (k - 1)
        # summ =  sum(nums[left:right + 1])
        # max_average = summ/k
        # while right < len(nums):
        #     right += 1
        #     if right < len(nums):
        #         summ += nums[right]
        #         summ -= nums[left]
        #         left += 1
        #         average = summ / k
        #         max_average = max(max_average, average)
        # return max_average

            
        # return max_average

        


        