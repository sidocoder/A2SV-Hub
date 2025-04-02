# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if not root:
                return

            traverse(root.left)
            tree.append(root.val)
            traverse(root.right)
        def construct(left,right):
            if left > right:
                return None
            mid =(left + right) // 2
            return TreeNode(tree[mid], construct(left,mid - 1),construct(mid + 1, right))
        tree = []
        traverse(root)
        return construct(0,len(tree) - 1)