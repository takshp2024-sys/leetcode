# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Base case 1: If both nodes are None, they are identical
        if not p and not q:
            return True
            
        # Base case 2: If one is None and the other isn't, they are not identical
        if not p or not q:
            return False
            
        # Base case 3: If the values don't match, they are not identical
        if p.val != q.val:
            return False
            
        # Recursive case: Check if both left and right subtrees are identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)