from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = deque([(root, 1)])  # Store tuples of (node, current_depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # If we reach a leaf node, return its depth immediately
            if not node.left and not node.right:
                return depth
                
            # Add children to the queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
                
        return 0