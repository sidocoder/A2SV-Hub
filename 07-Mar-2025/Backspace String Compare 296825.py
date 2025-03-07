# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for num in s:
            if stack1 and num == '#':
                stack1.pop()
            if num == '#':
                continue
            stack1.append(num)
        for num in t:
            if stack2 and num == '#':
                stack2.pop()
            if num == '#':
                continue
            stack2.append(num)

        return stack1 == stack2

    


        