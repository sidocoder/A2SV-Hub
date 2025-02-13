# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))

        while left <= right:
            curr_sum = left * left + right * right
            if curr_sum == c:
                return True
            elif curr_sum < c:
                left += 1
            else:
                right -= 1

        return False
