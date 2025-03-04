# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: abs(x[0] - x[1]) ,reverse= True )
        n = len(costs)
        total_cost = 0
        count_a, count_b= 0,0
        city_a, city_b = 0,0
        for cost_a,cost_b in costs:
            if cost_a < cost_b:
                if count_a < n //2:
                    count_a += 1
                    total_cost += cost_a
                else:
                    total_cost += cost_b
                    count_b += 1
            else:
                if count_b < n//2:
                    count_b += 1
                    total_cost += cost_b
                else:
                    total_cost += cost_a
                    count_a == 1
                        
           
        return total_cost
        

        differences = []
        for cost_a, cost_b in costs:
            diff = abs(cost_a - cost_b)
           



        