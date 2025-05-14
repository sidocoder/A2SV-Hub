# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        pre = [0]

        curr_num = 0
        for i in range(len(arr)):
            curr_num ^= arr[i]
            pre.append(curr_num)
       
            
        for left,right in queries:
            ans.append(pre[right + 1] ^ pre[left])
        return ans
        