# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.running_sum = 0  

        def reverse_inorder(node: Optional[TreeNode]):
            if not node:
                return
            
            reverse_inorder(node.right)
            
            self.running_sum += node.val
            node.val = self.running_sum
            
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root
