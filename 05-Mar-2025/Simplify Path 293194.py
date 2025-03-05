# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lst = path.split('/')
        for dirr in lst:
            if dirr == '..':
                if stack:
                    stack.pop()
            
            elif dirr == '' or dirr == '.':
                continue
            else:
                stack.append(dirr)

        return "/" + '/'.join(stack)