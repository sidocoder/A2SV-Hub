# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_value = max(costs)
        count = [0] * (max_value + 1)
        
        for cost in costs:
            count[cost] += 1
        
        sorted_costs =[]
        for i in range(len(count)):
            sorted_costs.extend([i] * count[i])

        summ = 0
        count = 0
        for i in range(len(sorted_costs)):
            summ += sorted_costs[i]            
            if summ > coins:
                break
            else:
                count += 1
        return count

                
    


        