# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            level_values = []
            nodes_at_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                nodes_at_level.append(node)
                level_values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level % 2 == 1:
                level_values.reverse()
                
                for i in range(level_size):
                    nodes_at_level[i].val = level_values[i]
            
            level += 1
        
        return root
        