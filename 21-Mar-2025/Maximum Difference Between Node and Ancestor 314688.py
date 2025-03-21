# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node,ans,_min,_max):
            if not node:
                return 0
            _min = min(_min,node.val)
            _max = max(_max,node.val)

            ans = max(ans,abs(_min - _max))

            left = dfs(node.left,ans,_min,_max)
            right = dfs(node.right,ans,_min,_max)
            return max(left, right, ans)
        return dfs(root,0, root.val, root.val)
        
        
        
        