# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the tree is empty, there is no path
        if not root:
            return False
            
        # If we reach a leaf node, check if the remaining sum matches the node's value
        if not root.left and not root.right:
            return targetSum == root.val
            
        # Recursively check the left and right subtrees with the updated target sum
        return (self.hasPathSum(root.left, targetSum - root.val) or 
                self.hasPathSum(root.right, targetSum - root.val))