# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node,summ, cnt):
            if not node:
                return [0,0]
            
            left = dfs(node.left,summ,cnt)
            right = dfs(node.right, summ, cnt)
            curr_sum = left[0] + right[0] + node.val
            curr_cnt = left[1] + right[1] + 1

            average = curr_sum // curr_cnt
            if average == node.val:
                self.count += 1
            return [curr_sum,curr_cnt]
        dfs(root,0,0)
        return self.count