# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
      
        left, right = 1, min(ranks) * (cars ** 2) 
        while left < right:
            mid = (left + right) // 2
            total_cars = sum(int(math.sqrt(mid // rank)) for rank in ranks)
            
            if total_cars >= cars:
                right = mid 
            else:
                left = mid + 1 
        return left
            