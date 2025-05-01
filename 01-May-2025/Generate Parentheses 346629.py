# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for j in range(i):
                for inside in dp[j]:
                    for outside in dp[i - 1 - j]:
                        dp[i].append(f"({inside}){outside}")

        return dp[n]
