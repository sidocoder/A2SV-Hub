# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
    def sumOfSquares(self, n: int) -> int: 
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        return output


            
        # sum = 0
        # while sum != 1:
        #     for num in str(n):
                
        #         if num not in hashh:
        #             hashh[num] = int(num) ** 2
        #             sum += hashh[num]
        #         else:
        #             value = hashh[num]
        #             sum += value

        # print(sum)


            


       

        # summ = 0
                   
        # for c in str(n):
        #     summ = summ + pow(int(c),2)
        # number = summ
        # print(number)
            
        