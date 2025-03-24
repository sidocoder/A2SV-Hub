# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchleft(nums, target):
            n = len(nums)
            left = 0
            right = n - 1
            best = -1
            while left <= right:
                mid = left + (right - left)// 2
                if nums[mid] == target:
                    best = mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return best

        def searchright(nums, target):
            
            n = len(nums)
            left = 0
            right = n - 1
            best = -1
            while left <= right:
                mid = left + (right - left)// 2
                if nums[mid] == target:
                    best = mid
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return best

        return [searchleft(nums,target),searchright(nums,target)]
        if target not in nums:
            return [-1,-1]
        # mid = (right - left) // 2