# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # for key, value in count.items():
        #     if value == 1:
        #         return key
        
        pre =[0]
        curr_num = 0
        for i in range(len(nums)):
            curr_num ^= nums[i]
            pre.append(curr_num)
        return pre[-1]
