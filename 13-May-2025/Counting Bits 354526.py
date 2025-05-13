# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        # for i in range(n+1):
        #     ans.append(bin(i).count('1'))
        # return ans

        for num in range(n + 1):
            count = 0
            for i in range(32):
                if num & (1 << i):
                    count += 1
            ans.append(count)
        return ans



        