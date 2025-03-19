# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
            
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                temp = ''
                while stack[-1] != '[':                    
                    temp = stack.pop() + temp
                
                stack.pop()
                intgr = ''
                while stack and stack[-1].isdigit():
                    intgr = stack.pop() + intgr
                stack.append(int(intgr) * temp)
                print(temp)
        return "".join(stack)
    
        

                    

















            # res = ''
            # for char in s:            
            #     if char.isdigit():
            #         multiplier = int(char)
            #         while stack:
            #             stack.pop()
            #     elif char == '[':
            #         continue
            #     elif char == ']':
            #         res += ''.join(stack)* multiplier
            #     else:
            #         stack.append(char)
            # return res
        # return multiplier(s)
        # stac =[]
        # for char in s:
        #     if char.isdigit():
        #         multiplier = int(char)
        #         while char != ']':
        #             if char == '[':
        #                 continue
        #             stac.append(char)
        

        # multiplier = []
        # stack = []
        # res = ''
        
        # for char in s:  
            
        #     temp = ''          
        #     if char.isdigit():
        #         multiplier.append(int(char))
        #     elif char == ']':
        #         while char != '[':
        #             if stack:
        #                 removed = stack.pop()
        #             temp += removed
        #         res += temp* multiplier
        #         if multiplier:
        #             multiplier.pop()
        #         if stack:
        #             stack.pop()
        #         stack.append(res)
        #     else:
        #         stack.append(char)
        # return 