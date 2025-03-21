# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def zigzag(node, level, ans):
            if not node:
                return
            if len(ans) <= level:
                ans += [[]]
            zigzag(node.left, level + 1, ans)
            zigzag(node.right, level + 1, ans)
            if level % 2 == 0:
                ans[level].append(node.val)
            else:
                ans[level].insert(0,node.val)
        zigzag(root,0,ans)
        return ans
           

        

        