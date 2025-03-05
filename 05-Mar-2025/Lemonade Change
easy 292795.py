# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashh = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                hashh[5] += 1 
            elif bill == 10:
                if hashh[5] > 0:
                    hashh[5] -= 1 
                    hashh[10] += 1  
                else:
                    return False
            elif bill == 20:
                if hashh[10] > 0 and hashh[5] > 0:
                    hashh[10] -= 1 
                    hashh[5] -= 1
                      
                elif hashh[5] >= 3:
                    hashh[5] -= 3 
                else:
                    return False
        return True


       

      