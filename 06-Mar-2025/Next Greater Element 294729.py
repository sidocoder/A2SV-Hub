# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = []
        ans = []
        for num in nums2:           
            while stack and num > stack[-1]:               
                x = stack.pop()
                d[x]= num
            stack.append(num)
        print(stack)  
        for num in nums1:
            if num in d:
                ans.append(d[num])
            else:
                ans.append(-1)
        return ans

        