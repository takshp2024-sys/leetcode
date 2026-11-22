# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        
        while current:
            # If both p and q are greater than the current node, LCA is in the right subtree
            if p.val > current.val and q.val > current.val:
                current = current.right
            # If both p and q are less than the current node, LCA is in the left subtree
            elif p.val < current.val and q.val < current.val:
                current = current.left
            # Otherwise, we have found the split point (or one node is the ancestor of the other)
            else:
                return current