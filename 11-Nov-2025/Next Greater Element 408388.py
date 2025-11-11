# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        ans = []

        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                next_greater[top] = num
            stack.append(num)
        
        for char in nums1:
            if char in next_greater:
                ans.append(next_greater[char])
            else:
                ans.append(-1)

        return ans





        # ------------------------------------------------------------
        # n = len(nums2)
        # ans = []
        # for num in nums1:
        #     j = nums2.index(num)
        #     if j == (n - 1):
        #         ans.append(-1)
        #     lists = nums2[j + 1:]
        #     for char in lists:
        #         if char > num:
        #             ans.append(char)
        #             break
        #         elif len(ans) < len(nums1):
        #             ans.append(-1)
        # return ans

        