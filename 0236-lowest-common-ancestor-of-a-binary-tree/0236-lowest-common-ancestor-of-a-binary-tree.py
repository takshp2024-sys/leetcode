# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if we reach a leaf or find p or q, return the current node
        if not root or root == p or root == q:
            return root
            
        # Recursively search the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right return a non-null value, it means p and q 
        # were found in different subtrees, so the current node is the LCA
        if left and right:
            return root
            
        # Otherwise, return whichever side found a match (or None if neither did)
        return left if left else right