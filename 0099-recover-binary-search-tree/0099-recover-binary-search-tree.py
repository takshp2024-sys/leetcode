# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None
        
        def inorder(node):
            if not node:
                return
                
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node
            if self.prev and self.prev.val > node.val:
                # First time we see an inversion, 'prev' is the first misplaced node
                if not self.first:
                    self.first = self.prev
                # The current node is the second misplaced node
                self.second = node
                
            # Update prev for the next node
            self.prev = node
            
            # Traverse right subtree
            inorder(node.right)
            
        # Perform in-order traversal to find the two swapped nodes
        inorder(root)
        
        # Swap the values of the two identified nodes
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val