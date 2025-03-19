# Problem: Convert Sorted Array to Binary Search Tree  - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(left, right):
            if left > right:  
                return None
            
            mid = (left + right) // 2  
            root = TreeNode(nums[mid])  
            root.left = dfs(left, mid - 1)  
            root.right = dfs(mid + 1, right)  

            return root
        
        return dfs(0, len(nums) - 1)  

