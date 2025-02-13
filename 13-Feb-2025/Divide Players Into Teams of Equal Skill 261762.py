# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]
        
        sum_of_all = sum(skill)
        if sum_of_all % (n // 2) != 0:
            return -1  
        
        target = sum_of_all // (n // 2)  
        skill_sum = 0
        
        skill.sort()  
        left, right = 0, n - 1
        
        while left < right:
            summ = skill[left] + skill[right]
            if summ != target:
                return -1  
            skill_sum += skill[left] * skill[right]
            left += 1
            right -= 1 

        return skill_sum
