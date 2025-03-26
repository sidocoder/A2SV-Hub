# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            total, needed_days = 0, 1
            for w in weights:
                if total + w > capacity:
                    needed_days += 1
                    total = 0
                total += w
            return needed_days <= days

        return bisect.bisect_left(range(max(weights), sum(weights) + 1), True, key=canShip) + max(weights)
