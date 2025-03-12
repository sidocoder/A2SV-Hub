# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def operation(a, b, c):
            
            if c == '*':
                return a *b
            elif c == "/":
                return int(a / b)        
            elif c == "-":
                return a - b
            elif c == '+':
                return a + b

        stack = []
        for char in tokens:
            if char.lstrip('-').isdigit():
                stack.append(int(char))
            else:
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()                
                    stack.append(operation(a, b, char))
        return stack[0]
                
       