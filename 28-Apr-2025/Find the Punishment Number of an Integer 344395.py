# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(num_str, target, index=0, current_sum=0):
            if index == len(num_str):
                return current_sum == target
            
            for j in range(index, len(num_str)):
                part = int(num_str[index:j+1])
                if current_sum + part > target:
                    break  
                if can_partition(num_str, target, j+1, current_sum + part):
                    return True
            return False

        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i):
                total += i * i
        return total


