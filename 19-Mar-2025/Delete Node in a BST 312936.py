# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minvalue(self, node: TreeNode) -> TreeNode:
        curr = node
        while curr.left:
            curr = curr.left
        return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:        
            root.right = self.deleteNode(root.right,key)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right


            temp = self.minvalue(root.right)
            root.val = temp.val

            root.right = self.deleteNode(root.right,temp.val)
        return root

        


        