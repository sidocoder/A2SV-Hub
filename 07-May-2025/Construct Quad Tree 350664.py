# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def is_uniform(x1, y1, size):
            first_val = grid[x1][y1]
            for i in range(x1, x1 + size):
                for j in range(y1, y1 + size):
                    if grid[i][j] != first_val:
                        return False, None
            return True, first_val

        def build(x, y, size):
            uniform, value = is_uniform(x, y, size)
            if uniform:
                return Node(bool(value), True, None, None, None, None)

            half = size // 2
            topLeft = build(x, y, half)
            topRight = build(x, y + half, half)
            bottomLeft = build(x + half, y, half)
            bottomRight = build(x + half, y + half, half)
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        n = len(grid)
        return build(0, 0, n)

        