# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        children = [0] * k

        def backtrack(index):
            if index == n:
                return max(children)

            min_unfairness = float('inf')
            for i in range(k):
                children[i] += cookies[index]
                min_unfairness = min(min_unfairness, backtrack(index + 1))
                children[i] -= cookies[index]

                if children[i] == 0: 
                    break
            return min_unfairness

        return backtrack(0)