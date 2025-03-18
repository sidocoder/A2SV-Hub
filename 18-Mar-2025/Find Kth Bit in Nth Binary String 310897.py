# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s: str):
            inverted = ''
            for char in s:
                if char == '0':
                    inverted += '1'
                else:
                    inverted += '0'
            return inverted
        def reverse(s: str):
            return s[::-1]
        s = '0'
        for i in range(n):
            s += '1' + reverse(invert(s))
        return s[k - 1]
        