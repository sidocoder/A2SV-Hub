# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, key):
            if not node or node.val == key:
                return node
            if node.val > key:
                return dfs(node.left,key)
            else:
                return dfs(node.right,key)
            
        return dfs(root,val)
            
        