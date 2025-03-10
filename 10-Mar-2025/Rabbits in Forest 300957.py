# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)  
        total = 0

        for num, freq in count.items():
            group_size = num + 1  
            groups = (freq + group_size - 1) // group_size 
            total += groups * group_size  

        return total
