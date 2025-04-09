# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # ans = []
        # for i in range(1, n + 1):
        #     if i not in nums:
        #         ans.append(i)
        
        # return ans
        pointer = 0

        while pointer < len(nums):
            num = nums[pointer]
            right_position = num -1
            if num == nums[right_position]:
                pointer += 1
            else:
                nums[pointer],nums[right_position] = nums[right_position],nums[pointer]

        ans = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans






        