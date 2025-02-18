# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # letters = 'abcdefghijklmnopqrstuvwxyz'
        # s = list(s)
        # # result = ''

        # for start, end, value in shifts:
                     
        #     for i in range(start,end + 1):
        #         if s[i] in letters:                        
        #             index = letters.index(s[i]) 
        #             if value == 1:             
        #                 s[i] = letters[(index + 1) % len(letters)]
        #             if value == 0:                            
        #                 s[i] = letters[(index - 1) % len(letters)]

        # return "".join(s) 
        


        letters = 'abcdefghijklmnopqrstuvwxyz'
        n = len(s)
        shift_array = [0] * (n + 1)  

        for start, end, value in shifts:
            if value == 1:
                shift_array[start] += 1
                shift_array[end + 1] -= 1
            else:
                shift_array[start] -= 1
                shift_array[end + 1] += 1

    
        current_shift = 0
        s = list(s)  
        for i in range(n):
            current_shift += shift_array[i]  
            new_char = chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a')) 
            s[i] = new_char 

        return "".join(s)






