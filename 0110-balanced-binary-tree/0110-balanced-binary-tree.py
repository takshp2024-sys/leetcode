# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_height(node: Optional[TreeNode]) -> int:
            # Base case: an empty tree has a height of 0
            if not node:
                return 0
                
            # Recursively get the height of the left subtree
            left_height = check_height(node.left)
            # If the left subtree is unbalanced, propagate the -1 upwards
            if left_height == -1:
                return -1
                
            # Recursively get the height of the right subtree
            right_height = check_height(node.right)
            # If the right subtree is unbalanced, propagate the -1 upwards
            if right_height == -1:
                return -1
                
            # Check if the current node is balanced
            if abs(left_height - right_height) > 1:
                return -1
                
            # If balanced, return the height of this subtree
            return max(left_height, right_height) + 1
            
        # The tree is balanced if the helper function does not return -1
        return check_height(root) != -1