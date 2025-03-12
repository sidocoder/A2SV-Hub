# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # dic = {')': '('}
        # stack = []
        # count = 0

        # for c in s:
        #     if c not in dic:
        #         stack.append(c)
        #     else:
        #         if stack[-1] == dic[c]:
        #             stack.pop()
        #             count += 1
        # return count
        stack = [0]  

        for char in s:
            if char == '(':  
                stack.append(0)  
            else:  
                last = stack.pop()  
                if last == 0:  
                    stack[-1] += 1  
                else:
                    stack[-1] += 2 * last  

        return stack[0]

                

                

            