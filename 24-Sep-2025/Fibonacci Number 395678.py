# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        return self.fib(n-1) + self.fib(n-2)