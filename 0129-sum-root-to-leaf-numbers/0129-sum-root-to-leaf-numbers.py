# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode], current_number: int) -> int:
            # Base case: if the node is None, return 0 (no valid path)
            if not node:
                return 0
                
            # Update the current number with the current node's value
            current_number = current_number * 10 + node.val
            
            # If it's a leaf node, return the current number
            if not node.left and not node.right:
                return current_number
                
            # Recursively sum the numbers from the left and right subtrees
            return dfs(node.left, current_number) + dfs(node.right, current_number)
            
        return dfs(root, 0)