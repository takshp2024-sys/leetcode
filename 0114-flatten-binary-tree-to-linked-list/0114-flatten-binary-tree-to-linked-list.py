# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        
        while current:
            # If the current node has a left child
            if current.left:
                # Find the rightmost node of the left subtree (predecessor)
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                    
                # Connect the original right subtree to the right of the predecessor
                predecessor.right = current.right
                
                # Move the left subtree to the right
                current.right = current.left
                current.left = None
                
            # Move to the next node
            current = current.right