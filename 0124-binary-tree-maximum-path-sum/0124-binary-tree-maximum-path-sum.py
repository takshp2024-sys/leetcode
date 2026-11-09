# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the global maximum to negative infinity to handle negative values
        self.max_sum = float('-inf')
        
        def max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
                
            # Recursively get the maximum gain from left and right subtrees.
            # We use max(0, gain) because if a subtree's contribution is negative, 
            # we are better off not including it in the path.
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # The maximum path sum that passes through the current node as the highest node
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # For the return value, we can only choose one side (left or right) 
            # to continue the path upwards to the parent.
            return node.val + max(left_gain, right_gain)
            
        max_gain(root)
        return self.max_sum