# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):
            # An empty tree is a valid BST
            if not node:
                return True
                
            # If the node's value violates the allowed range, it's not a BST
            if node.val <= low or node.val >= high:
                return False
                
            # Recursively check the left and right subtrees with updated bounds
            # For the left subtree, the maximum allowed value becomes node.val
            # For the right subtree, the minimum allowed value becomes node.val
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
                    
        # Start with the full range of 32-bit integers
        return validate(root, float('-inf'), float('inf'))