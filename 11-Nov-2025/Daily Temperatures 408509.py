# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in range(len(temperatures))]

        for i,num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                top = stack.pop()
                ans[top] = i - top
            stack.append(i)

        return ans


        ###############################################
        # res = [0] * len(temperatures)
        # stack = []
        
        # for i in range(len(temperatures)):
        #     while stack and temperatures[i] > temperatures[stack[-1]]:
        #         p = stack.pop()
        #         res[p] = i - p
        #     stack.append(i)
        # return res

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []
#         ans = []
#         d = {}
#         for num in temperatures:           
#             while stack and num > stack[-1]:               
#                 x = stack.pop()
#                 d[x]= num
#             stack.append(num)
#         for i in range(len(temperatures)):
#             if temperatures[i] in d:
#                 number = d[temperatures[i]]
#                 index = temperatures.index(number)
#                 ans.append(index - i)
#                 del d[temperatures[i]] 
#             else:
#                 ans.append(0)
#         return ans