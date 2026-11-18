from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            # Iterate through all nodes at the current level
            for i in range(level_size):
                node = queue.popleft()
                
                # If this is the last node in the current level, it's visible from the right
                if i == level_size - 1:
                    result.append(node.val)
                    
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result