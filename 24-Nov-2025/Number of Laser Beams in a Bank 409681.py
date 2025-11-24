# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        device_counts = []
        
        for row in bank:
            ones = row.count('1')
            if ones > 0:
                device_counts.append(ones)
        
        beams = 0
        for i in range(1, len(device_counts)):
            beams += device_counts[i] * device_counts[i-1]
        
        return beams