# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        n = len(arr)

        prev_smaller = [-1] * n
        next_smaller = [n] * n

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        for i in range(n):
            left_contrib = i - prev_smaller[i]
            right_contrib = next_smaller[i] - i
            result = (result + arr[i] * left_contrib * right_contrib) % MOD

        return result