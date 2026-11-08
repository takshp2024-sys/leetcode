"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
            
        # Start with the root node
        leftmost = root
        
        # While we haven't reached the leaf level
        while leftmost.left:
            # 'head' will traverse the current level using the 'next' pointers
            head = leftmost
            while head:
                # 1. Connect the left child to the right child of the same parent
                head.left.next = head.right
                
                # 2. Connect the right child to the left child of the next parent (if it exists)
                if head.next:
                    head.right.next = head.next.left
                    
                # Move to the next node in the current level
                head = head.next
                
            # Move to the leftmost node of the next level
            leftmost = leftmost.left
            
        return root