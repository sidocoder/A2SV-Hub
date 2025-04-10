# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        if k > sum(candies):
            return 0

        left = 1
        right = max(candies)

        best = 0
        while left <= right:
            mid = left + (right - left) // 2
            count = 0
            for i in range(n):
                count += candies[i] // mid
            if count < k:
                right = mid - 1
            elif count >= k:
                best = max(best,mid)
                left = mid + 1
        return best





        