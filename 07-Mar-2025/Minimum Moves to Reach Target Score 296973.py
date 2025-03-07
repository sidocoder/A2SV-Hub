# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 0:
            if target % 2 != 0:
                count += 1
                target -= 1
            elif maxDoubles:
                target=target // 2
                maxDoubles -= 1
                count += 1
            else:
                return count + target - 1
        return count-1
        
        
