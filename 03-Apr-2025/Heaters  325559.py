# Problem: Heaters  - https://leetcode.com/problems/heaters/


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        min_radius = 0
        
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            
            left_heater = heaters[idx - 1] if idx > 0 else float('-inf')
            right_heater = heaters[idx] if idx < len(heaters) else float('inf')
            
            closest_distance = min(abs(house - left_heater), abs(house - right_heater))
            min_radius = max(min_radius, closest_distance)
        
        return min_radius
